from collections import deque

import numpy as np
from scipy import signal
from scipy.interpolate import interp1d


def _resample(t, u):
    """
    Regularise the time interval and fit cubic function to u.
    Returns:
        Resampled u,t
    """
    u = u - np.mean(u)
    u_function = interp1d(t, u, kind="quadratic")
    t_min, t_max = np.min(t), np.max(t)
    dt = (t_max - t_min) / len(t)
    t = np.arange(t_min, t_max, dt)[
        :-1
    ]  # Regularize t and Skip last, can be problematic if > than t_max
    u = u_function(t)  # Regularize u
    return t, u[:-1]


def _resample_error(t, u):
    """
    Determine the L2 error in the interpolation of the original time series.
    This will help to quantify the noise threshold of the spectra.
    Args:
        t: time
        u: u

    Returns:
        L2 error in the resampling process
    """
    t_hat, u_hat = _resample(t, u)
    return np.sum((t_hat - t[: len(t_hat)]) ** 2 + (u_hat - u[: len(t_hat)]) ** 2)


def _window(a):
    w = signal.windows.hann(len(a))
    return a * w


def _tuk_window(a, alpha=0.5):
    w = signal.windows.tukey(len(a), alpha=alpha)
    return a * w


def _downsample_avg(arr, n):
    """
    Average every n elements a 1D array.
    :param arr: 1D array.
    :param n: size of the averaging subarray.
    :return: Downsampled-averaged 1D array.
    """
    end = n * int(len(arr) / n)
    return np.mean(arr[:end].reshape(-1, n), 1)


def _downsample_simple(arr, n):
    """
    Skip n elements of a 1D array.
    :param arr: 1D array.
    :param n: integer which defines the skips.
    :return: Downsampled 1D array.
    """
    return arr[::n]


def _low_pass_filter(u):
    """
    Apply a low-pass filter to u.
    :param u: Temporal signal 1D.
    :return: Windowed signal.
    """
    b, a = signal.butter(
        3, 0.4, "low"
    )  # 2nd arg: Fraction of fs that wants to be filtered
    return signal.filtfilt(b, a, u)


class FreqConv:
    """
    This is a class that holds functions to determine the convergence of a time series using the ensembled freq
    spectra.
    """

    def __init__(self, t, u, n=4, OL=0.5):
        self.t = t
        self.u = u
        self.n = n
        self.OL = OL

    def freq(self, t, u, **kwargs):
        """
        Returns the FFT of u together with the associated frequency after resampling the signal evenly.
        :param t: Time series.
        :param u: Signal series.
        :param kwargs:
            resample: Boolean to resample the signal evenly spaced in time.
            lowpass: Boolean to apply a low-pass filter to the transformed signal.
            windowing: Boolean to apply a windowing function to the temporal signal.
            downsample: Integer (where 0=False) for the number of points to average on the downsampling procedure.
            expanding_windowing: Boolean that changes the output to a list of uk and freqs representing an expanding
                                window so that we can see convergence to a manifold
        :return: freqs 1D array and uk 1D array.
        """
        resample = kwargs.get("resample", True)
        lowpass = kwargs.get("lowpass", False)
        windowing = kwargs.get("windowing", True)
        tukey_windowing = kwargs.get("tukey_windowing", False)
        downsample = kwargs.get("downsample", 0)

        if tukey_windowing:
            windowing = False
            u = _tuk_window(self.u)
        # Re-sample u on a evenly spaced time series (constant dt)
        if resample:
            u, t = _resample(t, u)
            t_min, t_max = np.min(t), np.max(t)
            dt = (t_max - t_min) / len(t)
        else:
            t_min, t_max = np.min(t), np.max(t)
            dt = (t_max - t_min) / len(t)

        if windowing:
            u = _window(u)  # Windowing
        if lowpass:
            u = _low_pass_filter(u)  # Signal filtering for high frequencies

        # Compute power fft and associated frequencies
        uk = 1 / (t_max - t_min) * np.fft.fft(u)
        freqs = np.fft.fftfreq(uk.size, d=dt)
        uk = uk * np.conj(uk)
        uk = uk.real

        # Downsample averaging
        if downsample > 0:
            uk = _downsample_avg(uk, downsample)
            freqs = _downsample_avg(freqs, downsample)
            uk = uk[:-1]
            freqs = freqs[:-1]

        # Take only nyquist frequency and get rid of sampling rate
        freqs = freqs[freqs > 0]
        uk = uk[: len(freqs)]
        return freqs, abs(uk)

    def ensemble(self, **kwargs):
        """
        This is a function that takes a Hann window of signal at discrete intervals and returns the frequency spec
        for each window, as well as the mean and var for these ffts. It then takes an ensembled average of these
        windows to show the convergence of a spectra.
        Args:
            torch: Time series
            u: Signal Series
            **kwargs:
                resample: Boolean to resample the signal evenly spaced in time.
                lowpass: Boolean to apply a low-pass filter to the transformed signal.
                windowing: Boolean to apply a windowing function to the temporal signal.
                downsample: Integer (where 0=False) for the number of points to average on the downsampling procedure.
        :return: uks_labelled: list of

        Returns:
                uks_labelled: n dimensional list of (label, uk) tuple where the label is the window
                fs : n dimensional list of frequencies
        """
        # Split the signal into it's constituent windows
        u_partial_ol_list = self._split_overlap(self.u)
        t_partial_ol_list = self._split_overlap(self.t)

        uk_ensemble_avg = deque()
        freqs_ensemble_avg = deque()
        area = deque()
        tmp_f = deque()
        tmp_uk = deque()
        ind_wind_area = deque()
        for idx, tup in enumerate(list(zip(t_partial_ol_list, u_partial_ol_list))):
            t, u = tup[0], tup[1]
            if idx > 0:
                u = u - np.mean(u_partial_ol_list[0:idx])
            else:
                u = u - np.mean(u)
            u_function = interp1d(t, u, kind="cubic")
            t_min, t_max = np.min(t), np.max(t)
            dt = (t_max - t_min) / len(t)
            t = np.arange(t_min, t_max + dt, dt)[
                0 : int(len(u) - 1)
            ]  # Regularize t and Skip last, can be problematic if > than t_max
            u = u_function(t)

            freqs, uk = self.freq(t=t, u=u, resample=False, windowing=True, **kwargs)
            ind_wind_area.append(np.trapz(uk, freqs))
            tmp_f.append(freqs)
            tmp_uk.append(uk)
            uk_mean = np.mean(tmp_uk, axis=0)
            uk_ensemble_avg.append((f"Window ${idx + 1}$", uk_mean))
            freqs_mean = np.mean(tmp_f, axis=0)
            freqs_ensemble_avg.append(freqs_mean)
            area.append(np.trapz(uk_mean, freqs_mean))
        return (
            np.array(uk_ensemble_avg, dtype=object),
            np.array(freqs_ensemble_avg, dtype=object),
            np.array(area),
        )

    def split(self, **kwargs):
        """
        Instead of ensemble this treats each time window as an independent spectra and returns them as a list.
        This serves better as a method of visually seeing whether the windows collapse onto eachother.
        Args:
            torch: Time series
            u: Signal Series
            **kwargs:
                resample: Boolean to resample the signal evenly spaced in time.
                lowpass: Boolean to apply a low-pass filter to the transformed signal.
                windowing: Boolean to apply a windowing function to the temporal signal.
                downsample: Integer (where 0=False) for the number of points to average on the downsampling procedure.
        :return: uks_labelled: list of

        Returns:
                uks_labelled: n dimensional list of (label, uk) tuple where the label is the window
                fs : n dimensional list of frequencies
        """
        # Split the signal into it's constituent windows
        u_partial_ol_list = self._split_overlap(self.u)
        t_partial_ol_list = self._split_overlap(self.t)

        rmss = []
        uk_wind, freqs_wind = [], []
        for idx, tup1 in enumerate(list(zip(t_partial_ol_list, u_partial_ol_list))):
            t, u = tup1[0], tup1[1]
            t, u = _resample(t, u)

            u_partial_ol_list = self._split_overlap(u, n=2, OL=0.8)
            t_partial_ol_list = self._split_overlap(t, n=2, OL=0.8)

            tmp_uk, tmp_f = [], []
            for tup2 in list(zip(t_partial_ol_list, u_partial_ol_list)):
                rmss.append(np.sqrt(np.mean((tup2[1] - np.mean(tup2[1])) ** 2)))
                freqs, uk = self.freq(
                    t=tup2[0], u=tup2[1], resample=False, windowing=True, **kwargs
                )
                tmp_f.append(freqs)
                tmp_uk.append(uk)

            uk_mean = np.mean(np.array(tmp_uk), axis=0)
            freqs_mean = np.mean(np.array(tmp_f), axis=0)

            freqs_wind.append(freqs_mean)
            uk_wind.append(
                (
                    r"$ t^{\star} ["
                    + str(int(round(np.min(t), 0)))
                    + ", "
                    + str(int(round(np.max(t), 0)))
                    + "]$",
                    uk_mean,
                )
            )

            # uk_mean = np.mean(tmp_uk, axis=0)
            # uk_ensemble_avg.append((f"Window ${idx+1}$", uk_mean))
            # freqs_mean = np.mean(tmp_f, axis=0)
            # freqs_ensemble_avg.append(freqs_mean)
            # area.append(np.trapz(uk_mean, freqs_mean))
        # ic(np.mean(np.array(rmss)), np.std(np.array(rmss)), (max(rmss)-min(rmss))/np.mean(rmss))
        return np.array(uk_wind, dtype=object), np.array(freqs_wind, dtype=object)

    def f_conv(self, cycles, **kwargs):
        """
        Find how the spectra converges to a steady value
        Args:
            cycles: The number of convection cycles to split the TS over
            **kwargs: arguments for parent methods

        Returns:
            RMS: RMS difference between adjacent spectra normalised by the integral of that spectra
            torch: 1d numpy array holding the times the windows are centred around

        """
        labelled_uks_e, fs_e, area = self.ensemble(**kwargs)
        uks_e = deque()
        for loop1 in labelled_uks_e:
            uks_e.append(loop1[1])

        uks_e = np.array(uks_e)

        off1 = uks_e[1:]
        off2 = uks_e[:-1]

        diff_rms = np.sqrt((off1 - off2) ** 2)
        rms = deque()
        for loop in zip(diff_rms, fs_e):
            rms.append(np.trapz(loop[0], loop[1]))
        rms = np.array(rms)

        normed_error = rms / area[1:]

        assert area[1:][-1] != 0, "Check time history, is your force oscillating?"

        window_t = np.linspace(min(self.t) + cycles, max(self.t), len(normed_error))
        return normed_error, window_t

    def welch(self, **kwargs):
        """
        Returns the FFT of u together with the associated frequency after resampling the signal evenly.
        In this case, an averages of the spectras is computed.
        :param t: Time series.
        :param u:  Signal series.
        :param n:  Number of splits of the original whole time signal.
        :param OL: Overlap of the splits to compute the time
        :param kwargs:
            lowpass: Boolean to apply a low-pass filte to the transformed signal.
            windowing: Boolean to apply a windowing function to the temporal signal.
            expanding_windowing: Boolean that changes the output to a list of uk and freqs representing an expanding window
            evaluation of the frequency signals
        :return: freqs 1D array and uk 1D array., with optional error as a 2d array
        """
        t, u = _resample(self.t, self.u)

        u_partial_list = self._split_overlap(u)
        t_partial_list = self._split_overlap(t)

        # rmss = np.array([np.sqrt(np.sum((u - np.mean(u)) ** 2) / len(u)) for u in u_partial_list])
        # print('\nRMS = ', np.mean(rmss), r'$\sigma = $', np.std(rmss)/np.mean(rmss))

        uk_bins = []
        frequency_bins = []
        for idx, tup in enumerate(list(zip(t_partial_list, u_partial_list))):
            freqs, uk = self.freq(
                t=tup[0], u=tup[1], resample=False, windowing=True, **kwargs
            )
            frequency_bins.append(freqs)
            uk_bins.append(uk)
        uk_bins, frequency_bins = np.array(uk_bins), np.array(frequency_bins)

        uk_mean = np.mean(np.array(uk_bins), axis=0)
        freqs_mean = np.mean(np.array(frequency_bins), axis=0)
        if kwargs.get("error"):
            return (
                freqs_mean,
                uk_mean,
                [np.max(uk_bins, axis=0), np.min(uk_bins, axis=0)],
            )
        elif kwargs.get("std"):
            return freqs_mean, uk_mean, np.std(uk_bins, axis=0)
        else:
            return freqs_mean, uk_mean

    def _split_overlap(self, a, n=None, OL=None):
        """
        :param a: array to split and overlap.
        :param n: number of splits of a.
        :param OL: overlap.
        :return: length_scale, a list of the splits of a in function of n and OL
        """
        if n is None:
            n = self.n
        if OL is None:
            OL = self.OL
        splits_size = a.size // n
        nOL = int(np.floor(splits_size * OL))
        skip = splits_size - nOL
        b = [a[i : i + splits_size] for i in range(0, len(a), skip)]
        c = deque()
        for i, item in enumerate(b):
            if len(item) == splits_size:
                c.append(item)
        return np.array(c)