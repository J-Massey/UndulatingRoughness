# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
import os
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'PVD Reader'
cwd = '/ssdfs/users/jmom1n15/phase_shift'
fluidvtipvd = PVDReader(registrationName='fluid.vti.pvd', FileName=f'{cwd}/16x16/1024/fluid.vti.pvd')
fluidvtipvd.CellArrays = []
fluidvtipvd.PointArrays = ['Velocity', 'Pressure']
fluidvtipvd.ColumnArrays = []

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
fluidvtipvdDisplay = Show(fluidvtipvd, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
fluidvtipvdDisplay.Selection = None
fluidvtipvdDisplay.Representation = 'Outline'
fluidvtipvdDisplay.ColorArrayName = ['POINTS', '']
fluidvtipvdDisplay.LookupTable = None
fluidvtipvdDisplay.MapScalars = 1
fluidvtipvdDisplay.MultiComponentsMapping = 0
fluidvtipvdDisplay.InterpolateScalarsBeforeMapping = 1
fluidvtipvdDisplay.Opacity = 1.0
fluidvtipvdDisplay.PointSize = 2.0
fluidvtipvdDisplay.LineWidth = 1.0
fluidvtipvdDisplay.RenderLinesAsTubes = 0
fluidvtipvdDisplay.RenderPointsAsSpheres = 0
fluidvtipvdDisplay.Interpolation = 'Gouraud'
fluidvtipvdDisplay.Specular = 0.0
fluidvtipvdDisplay.SpecularColor = [1.0, 1.0, 1.0]
fluidvtipvdDisplay.SpecularPower = 100.0
fluidvtipvdDisplay.Luminosity = 0.0
fluidvtipvdDisplay.Ambient = 0.0
fluidvtipvdDisplay.Diffuse = 1.0
fluidvtipvdDisplay.Roughness = 0.3
fluidvtipvdDisplay.Metallic = 0.0
fluidvtipvdDisplay.EdgeTint = [1.0, 1.0, 1.0]
fluidvtipvdDisplay.Anisotropy = 0.0
fluidvtipvdDisplay.AnisotropyRotation = 0.0
fluidvtipvdDisplay.BaseIOR = 1.5
fluidvtipvdDisplay.CoatStrength = 0.0
fluidvtipvdDisplay.CoatIOR = 2.0
fluidvtipvdDisplay.CoatRoughness = 0.0
fluidvtipvdDisplay.CoatColor = [1.0, 1.0, 1.0]
fluidvtipvdDisplay.SelectTCoordArray = 'None'
fluidvtipvdDisplay.SelectNormalArray = 'None'
fluidvtipvdDisplay.SelectTangentArray = 'None'
fluidvtipvdDisplay.Texture = None
fluidvtipvdDisplay.RepeatTextures = 1
fluidvtipvdDisplay.InterpolateTextures = 0
fluidvtipvdDisplay.SeamlessU = 0
fluidvtipvdDisplay.SeamlessV = 0
fluidvtipvdDisplay.UseMipmapTextures = 0
fluidvtipvdDisplay.ShowTexturesOnBackface = 1
fluidvtipvdDisplay.BaseColorTexture = None
fluidvtipvdDisplay.NormalTexture = None
fluidvtipvdDisplay.NormalScale = 1.0
fluidvtipvdDisplay.CoatNormalTexture = None
fluidvtipvdDisplay.CoatNormalScale = 1.0
fluidvtipvdDisplay.MaterialTexture = None
fluidvtipvdDisplay.OcclusionStrength = 1.0
fluidvtipvdDisplay.AnisotropyTexture = None
fluidvtipvdDisplay.EmissiveTexture = None
fluidvtipvdDisplay.EmissiveFactor = [1.0, 1.0, 1.0]
fluidvtipvdDisplay.FlipTextures = 0
fluidvtipvdDisplay.BackfaceRepresentation = 'Follow Frontface'
fluidvtipvdDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
fluidvtipvdDisplay.BackfaceOpacity = 1.0
fluidvtipvdDisplay.Position = [0.0, 0.0, 0.0]
fluidvtipvdDisplay.Scale = [1.0, 1.0, 1.0]
fluidvtipvdDisplay.Orientation = [0.0, 0.0, 0.0]
fluidvtipvdDisplay.Origin = [0.0, 0.0, 0.0]
fluidvtipvdDisplay.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
fluidvtipvdDisplay.Pickable = 1
fluidvtipvdDisplay.Triangulate = 0
fluidvtipvdDisplay.UseShaderReplacements = 0
fluidvtipvdDisplay.ShaderReplacements = ''
fluidvtipvdDisplay.NonlinearSubdivisionLevel = 1
fluidvtipvdDisplay.UseDataPartitions = 0
fluidvtipvdDisplay.OSPRayUseScaleArray = 'All Approximate'
fluidvtipvdDisplay.OSPRayScaleArray = 'Pressure'
fluidvtipvdDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
fluidvtipvdDisplay.OSPRayMaterial = 'None'
fluidvtipvdDisplay.BlockSelectors = ['/']
fluidvtipvdDisplay.BlockColors = []
fluidvtipvdDisplay.BlockOpacities = []
fluidvtipvdDisplay.Orient = 0
fluidvtipvdDisplay.OrientationMode = 'Direction'
fluidvtipvdDisplay.SelectOrientationVectors = 'Velocity'
fluidvtipvdDisplay.Scaling = 0
fluidvtipvdDisplay.ScaleMode = 'No Data Scaling Off'
fluidvtipvdDisplay.ScaleFactor = 307.20000000000005
fluidvtipvdDisplay.SelectScaleArray = 'Pressure'
fluidvtipvdDisplay.GlyphType = 'Arrow'
fluidvtipvdDisplay.UseGlyphTable = 0
fluidvtipvdDisplay.GlyphTableIndexArray = 'Pressure'
fluidvtipvdDisplay.UseCompositeGlyphTable = 0
fluidvtipvdDisplay.UseGlyphCullingAndLOD = 0
fluidvtipvdDisplay.LODValues = []
fluidvtipvdDisplay.ColorByLODIndex = 0
fluidvtipvdDisplay.GaussianRadius = 15.36
fluidvtipvdDisplay.ShaderPreset = 'Sphere'
fluidvtipvdDisplay.CustomTriangleScale = 3
fluidvtipvdDisplay.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
fluidvtipvdDisplay.Emissive = 0
fluidvtipvdDisplay.ScaleByArray = 0
fluidvtipvdDisplay.SetScaleArray = ['POINTS', 'Pressure']
fluidvtipvdDisplay.ScaleArrayComponent = ''
fluidvtipvdDisplay.UseScaleFunction = 1
fluidvtipvdDisplay.ScaleTransferFunction = 'PiecewiseFunction'
fluidvtipvdDisplay.OpacityByArray = 0
fluidvtipvdDisplay.OpacityArray = ['POINTS', 'Pressure']
fluidvtipvdDisplay.OpacityArrayComponent = ''
fluidvtipvdDisplay.OpacityTransferFunction = 'PiecewiseFunction'
fluidvtipvdDisplay.DataAxesGrid = 'GridAxesRepresentation'
fluidvtipvdDisplay.SelectionCellLabelBold = 0
fluidvtipvdDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
fluidvtipvdDisplay.SelectionCellLabelFontFamily = 'Arial'
fluidvtipvdDisplay.SelectionCellLabelFontFile = ''
fluidvtipvdDisplay.SelectionCellLabelFontSize = 18
fluidvtipvdDisplay.SelectionCellLabelItalic = 0
fluidvtipvdDisplay.SelectionCellLabelJustification = 'Left'
fluidvtipvdDisplay.SelectionCellLabelOpacity = 1.0
fluidvtipvdDisplay.SelectionCellLabelShadow = 0
fluidvtipvdDisplay.SelectionPointLabelBold = 0
fluidvtipvdDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
fluidvtipvdDisplay.SelectionPointLabelFontFamily = 'Arial'
fluidvtipvdDisplay.SelectionPointLabelFontFile = ''
fluidvtipvdDisplay.SelectionPointLabelFontSize = 18
fluidvtipvdDisplay.SelectionPointLabelItalic = 0
fluidvtipvdDisplay.SelectionPointLabelJustification = 'Left'
fluidvtipvdDisplay.SelectionPointLabelOpacity = 1.0
fluidvtipvdDisplay.SelectionPointLabelShadow = 0
fluidvtipvdDisplay.PolarAxes = 'PolarAxesRepresentation'
fluidvtipvdDisplay.ScalarOpacityUnitDistance = 10.076780877341227
fluidvtipvdDisplay.ScalarOpacityFunction = None
fluidvtipvdDisplay.UseSeparateOpacityArray = 0
fluidvtipvdDisplay.OpacityArrayName = ['POINTS', 'Pressure']
fluidvtipvdDisplay.OpacityComponent = ''
fluidvtipvdDisplay.VolumeRenderingMode = 'Smart'
fluidvtipvdDisplay.Shade = 0
fluidvtipvdDisplay.BlendMode = 'Composite'
fluidvtipvdDisplay.IsosurfaceValues = [0.6992536187171936]
fluidvtipvdDisplay.SliceFunction = 'Plane'
fluidvtipvdDisplay.UseCropping = 0
fluidvtipvdDisplay.CroppingOrigin = [0.0, 0.0, 0.0]
fluidvtipvdDisplay.CroppingScale = [1.0, 1.0, 1.0]
fluidvtipvdDisplay.SliceMode = 'XY Plane'
fluidvtipvdDisplay.Slice = 32

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
fluidvtipvdDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
fluidvtipvdDisplay.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
fluidvtipvdDisplay.GlyphType.TipResolution = 6
fluidvtipvdDisplay.GlyphType.TipRadius = 0.1
fluidvtipvdDisplay.GlyphType.TipLength = 0.35
fluidvtipvdDisplay.GlyphType.ShaftResolution = 6
fluidvtipvdDisplay.GlyphType.ShaftRadius = 0.03
fluidvtipvdDisplay.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
fluidvtipvdDisplay.ScaleTransferFunction.Points = [-1.0521329641342163, 0.0, 0.5, 0.0, 2.4506402015686035, 1.0, 0.5, 0.0]
fluidvtipvdDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
fluidvtipvdDisplay.OpacityTransferFunction.Points = [-1.0521329641342163, 0.0, 0.5, 0.0, 2.4506402015686035, 1.0, 0.5, 0.0]
fluidvtipvdDisplay.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fluidvtipvdDisplay.DataAxesGrid.XTitle = 'X Axis'
fluidvtipvdDisplay.DataAxesGrid.YTitle = 'Y Axis'
fluidvtipvdDisplay.DataAxesGrid.ZTitle = 'Z Axis'
fluidvtipvdDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
fluidvtipvdDisplay.DataAxesGrid.XTitleFontFile = ''
fluidvtipvdDisplay.DataAxesGrid.XTitleBold = 0
fluidvtipvdDisplay.DataAxesGrid.XTitleItalic = 0
fluidvtipvdDisplay.DataAxesGrid.XTitleFontSize = 12
fluidvtipvdDisplay.DataAxesGrid.XTitleShadow = 0
fluidvtipvdDisplay.DataAxesGrid.XTitleOpacity = 1.0
fluidvtipvdDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
fluidvtipvdDisplay.DataAxesGrid.YTitleFontFile = ''
fluidvtipvdDisplay.DataAxesGrid.YTitleBold = 0
fluidvtipvdDisplay.DataAxesGrid.YTitleItalic = 0
fluidvtipvdDisplay.DataAxesGrid.YTitleFontSize = 12
fluidvtipvdDisplay.DataAxesGrid.YTitleShadow = 0
fluidvtipvdDisplay.DataAxesGrid.YTitleOpacity = 1.0
fluidvtipvdDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
fluidvtipvdDisplay.DataAxesGrid.ZTitleFontFile = ''
fluidvtipvdDisplay.DataAxesGrid.ZTitleBold = 0
fluidvtipvdDisplay.DataAxesGrid.ZTitleItalic = 0
fluidvtipvdDisplay.DataAxesGrid.ZTitleFontSize = 12
fluidvtipvdDisplay.DataAxesGrid.ZTitleShadow = 0
fluidvtipvdDisplay.DataAxesGrid.ZTitleOpacity = 1.0
fluidvtipvdDisplay.DataAxesGrid.FacesToRender = 63
fluidvtipvdDisplay.DataAxesGrid.CullBackface = 0
fluidvtipvdDisplay.DataAxesGrid.CullFrontface = 1
fluidvtipvdDisplay.DataAxesGrid.ShowGrid = 0
fluidvtipvdDisplay.DataAxesGrid.ShowEdges = 1
fluidvtipvdDisplay.DataAxesGrid.ShowTicks = 1
fluidvtipvdDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
fluidvtipvdDisplay.DataAxesGrid.AxesToLabel = 63
fluidvtipvdDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
fluidvtipvdDisplay.DataAxesGrid.XLabelFontFile = ''
fluidvtipvdDisplay.DataAxesGrid.XLabelBold = 0
fluidvtipvdDisplay.DataAxesGrid.XLabelItalic = 0
fluidvtipvdDisplay.DataAxesGrid.XLabelFontSize = 12
fluidvtipvdDisplay.DataAxesGrid.XLabelShadow = 0
fluidvtipvdDisplay.DataAxesGrid.XLabelOpacity = 1.0
fluidvtipvdDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
fluidvtipvdDisplay.DataAxesGrid.YLabelFontFile = ''
fluidvtipvdDisplay.DataAxesGrid.YLabelBold = 0
fluidvtipvdDisplay.DataAxesGrid.YLabelItalic = 0
fluidvtipvdDisplay.DataAxesGrid.YLabelFontSize = 12
fluidvtipvdDisplay.DataAxesGrid.YLabelShadow = 0
fluidvtipvdDisplay.DataAxesGrid.YLabelOpacity = 1.0
fluidvtipvdDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
fluidvtipvdDisplay.DataAxesGrid.ZLabelFontFile = ''
fluidvtipvdDisplay.DataAxesGrid.ZLabelBold = 0
fluidvtipvdDisplay.DataAxesGrid.ZLabelItalic = 0
fluidvtipvdDisplay.DataAxesGrid.ZLabelFontSize = 12
fluidvtipvdDisplay.DataAxesGrid.ZLabelShadow = 0
fluidvtipvdDisplay.DataAxesGrid.ZLabelOpacity = 1.0
fluidvtipvdDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
fluidvtipvdDisplay.DataAxesGrid.XAxisPrecision = 2
fluidvtipvdDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
fluidvtipvdDisplay.DataAxesGrid.XAxisLabels = []
fluidvtipvdDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
fluidvtipvdDisplay.DataAxesGrid.YAxisPrecision = 2
fluidvtipvdDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
fluidvtipvdDisplay.DataAxesGrid.YAxisLabels = []
fluidvtipvdDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
fluidvtipvdDisplay.DataAxesGrid.ZAxisPrecision = 2
fluidvtipvdDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
fluidvtipvdDisplay.DataAxesGrid.ZAxisLabels = []
fluidvtipvdDisplay.DataAxesGrid.UseCustomBounds = 0
fluidvtipvdDisplay.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fluidvtipvdDisplay.PolarAxes.Visibility = 0
fluidvtipvdDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
fluidvtipvdDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
fluidvtipvdDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
fluidvtipvdDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
fluidvtipvdDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
fluidvtipvdDisplay.PolarAxes.EnableCustomRange = 0
fluidvtipvdDisplay.PolarAxes.CustomRange = [0.0, 1.0]
fluidvtipvdDisplay.PolarAxes.PolarAxisVisibility = 1
fluidvtipvdDisplay.PolarAxes.RadialAxesVisibility = 1
fluidvtipvdDisplay.PolarAxes.DrawRadialGridlines = 1
fluidvtipvdDisplay.PolarAxes.PolarArcsVisibility = 1
fluidvtipvdDisplay.PolarAxes.DrawPolarArcsGridlines = 1
fluidvtipvdDisplay.PolarAxes.NumberOfRadialAxes = 0
fluidvtipvdDisplay.PolarAxes.AutoSubdividePolarAxis = 1
fluidvtipvdDisplay.PolarAxes.NumberOfPolarAxis = 0
fluidvtipvdDisplay.PolarAxes.MinimumRadius = 0.0
fluidvtipvdDisplay.PolarAxes.MinimumAngle = 0.0
fluidvtipvdDisplay.PolarAxes.MaximumAngle = 90.0
fluidvtipvdDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
fluidvtipvdDisplay.PolarAxes.Ratio = 1.0
fluidvtipvdDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
fluidvtipvdDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
fluidvtipvdDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
fluidvtipvdDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
fluidvtipvdDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
fluidvtipvdDisplay.PolarAxes.PolarAxisTitleVisibility = 1
fluidvtipvdDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
fluidvtipvdDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
fluidvtipvdDisplay.PolarAxes.PolarLabelVisibility = 1
fluidvtipvdDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
fluidvtipvdDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
fluidvtipvdDisplay.PolarAxes.RadialLabelVisibility = 1
fluidvtipvdDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
fluidvtipvdDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
fluidvtipvdDisplay.PolarAxes.RadialUnitsVisibility = 1
fluidvtipvdDisplay.PolarAxes.ScreenSize = 10.0
fluidvtipvdDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
fluidvtipvdDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
fluidvtipvdDisplay.PolarAxes.PolarAxisTitleFontFile = ''
fluidvtipvdDisplay.PolarAxes.PolarAxisTitleBold = 0
fluidvtipvdDisplay.PolarAxes.PolarAxisTitleItalic = 0
fluidvtipvdDisplay.PolarAxes.PolarAxisTitleShadow = 0
fluidvtipvdDisplay.PolarAxes.PolarAxisTitleFontSize = 12
fluidvtipvdDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
fluidvtipvdDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
fluidvtipvdDisplay.PolarAxes.PolarAxisLabelFontFile = ''
fluidvtipvdDisplay.PolarAxes.PolarAxisLabelBold = 0
fluidvtipvdDisplay.PolarAxes.PolarAxisLabelItalic = 0
fluidvtipvdDisplay.PolarAxes.PolarAxisLabelShadow = 0
fluidvtipvdDisplay.PolarAxes.PolarAxisLabelFontSize = 12
fluidvtipvdDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
fluidvtipvdDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
fluidvtipvdDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
fluidvtipvdDisplay.PolarAxes.LastRadialAxisTextBold = 0
fluidvtipvdDisplay.PolarAxes.LastRadialAxisTextItalic = 0
fluidvtipvdDisplay.PolarAxes.LastRadialAxisTextShadow = 0
fluidvtipvdDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
fluidvtipvdDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
fluidvtipvdDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
fluidvtipvdDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
fluidvtipvdDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
fluidvtipvdDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
fluidvtipvdDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
fluidvtipvdDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
fluidvtipvdDisplay.PolarAxes.EnableDistanceLOD = 1
fluidvtipvdDisplay.PolarAxes.DistanceLODThreshold = 0.7
fluidvtipvdDisplay.PolarAxes.EnableViewAngleLOD = 1
fluidvtipvdDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
fluidvtipvdDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
fluidvtipvdDisplay.PolarAxes.PolarTicksVisibility = 1
fluidvtipvdDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
fluidvtipvdDisplay.PolarAxes.TickLocation = 'Both'
fluidvtipvdDisplay.PolarAxes.AxisTickVisibility = 1
fluidvtipvdDisplay.PolarAxes.AxisMinorTickVisibility = 0
fluidvtipvdDisplay.PolarAxes.ArcTickVisibility = 1
fluidvtipvdDisplay.PolarAxes.ArcMinorTickVisibility = 0
fluidvtipvdDisplay.PolarAxes.DeltaAngleMajor = 10.0
fluidvtipvdDisplay.PolarAxes.DeltaAngleMinor = 5.0
fluidvtipvdDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
fluidvtipvdDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
fluidvtipvdDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
fluidvtipvdDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
fluidvtipvdDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
fluidvtipvdDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
fluidvtipvdDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
fluidvtipvdDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
fluidvtipvdDisplay.PolarAxes.ArcMajorTickSize = 0.0
fluidvtipvdDisplay.PolarAxes.ArcTickRatioSize = 0.3
fluidvtipvdDisplay.PolarAxes.ArcMajorTickThickness = 1.0
fluidvtipvdDisplay.PolarAxes.ArcTickRatioThickness = 0.5
fluidvtipvdDisplay.PolarAxes.Use2DMode = 0
fluidvtipvdDisplay.PolarAxes.UseLogAxis = 0

# init the 'Plane' selected for 'SliceFunction'
fluidvtipvdDisplay.SliceFunction.Origin = [1026.0, 1.0, 130.0]
fluidvtipvdDisplay.SliceFunction.Normal = [1.0, 0.0, 0.0]
fluidvtipvdDisplay.SliceFunction.Offset = 0.0

# reset view to fit data
renderView1.ResetCamera(False)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Gradient'
gradient1 = Gradient(registrationName='Gradient1', Input=fluidvtipvd)
gradient1.ScalarArray = ['POINTS', 'Pressure']
gradient1.BoundaryMethod = 'Non-Smoothed'
gradient1.Dimensionality = 'Three'
gradient1.ComputeGradient = 1
gradient1.ResultArrayName = 'Gradient'
gradient1.FasterApproximation = 0
gradient1.ComputeDivergence = 0
gradient1.DivergenceArrayName = 'Divergence'
gradient1.ComputeVorticity = 0
gradient1.VorticityArrayName = 'Vorticity'
gradient1.ComputeQCriterion = 0
gradient1.QCriterionArrayName = 'Q Criterion'
gradient1.ContributingCellOption = 'Dataset Max'
gradient1.ReplacementValueOption = 'NaN'

# Properties modified on gradient1
gradient1.ScalarArray = ['POINTS', 'Velocity']
gradient1.ComputeGradient = 0
gradient1.ComputeVorticity = 1
gradient1.ComputeQCriterion = 1

# show data in view
gradient1Display = Show(gradient1, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
gradient1Display.Selection = None
gradient1Display.Representation = 'Outline'
gradient1Display.ColorArrayName = ['POINTS', '']
gradient1Display.LookupTable = None
gradient1Display.MapScalars = 1
gradient1Display.MultiComponentsMapping = 0
gradient1Display.InterpolateScalarsBeforeMapping = 1
gradient1Display.Opacity = 1.0
gradient1Display.PointSize = 2.0
gradient1Display.LineWidth = 1.0
gradient1Display.RenderLinesAsTubes = 0
gradient1Display.RenderPointsAsSpheres = 0
gradient1Display.Interpolation = 'Gouraud'
gradient1Display.Specular = 0.0
gradient1Display.SpecularColor = [1.0, 1.0, 1.0]
gradient1Display.SpecularPower = 100.0
gradient1Display.Luminosity = 0.0
gradient1Display.Ambient = 0.0
gradient1Display.Diffuse = 1.0
gradient1Display.Roughness = 0.3
gradient1Display.Metallic = 0.0
gradient1Display.EdgeTint = [1.0, 1.0, 1.0]
gradient1Display.Anisotropy = 0.0
gradient1Display.AnisotropyRotation = 0.0
gradient1Display.BaseIOR = 1.5
gradient1Display.CoatStrength = 0.0
gradient1Display.CoatIOR = 2.0
gradient1Display.CoatRoughness = 0.0
gradient1Display.CoatColor = [1.0, 1.0, 1.0]
gradient1Display.SelectTCoordArray = 'None'
gradient1Display.SelectNormalArray = 'None'
gradient1Display.SelectTangentArray = 'None'
gradient1Display.Texture = None
gradient1Display.RepeatTextures = 1
gradient1Display.InterpolateTextures = 0
gradient1Display.SeamlessU = 0
gradient1Display.SeamlessV = 0
gradient1Display.UseMipmapTextures = 0
gradient1Display.ShowTexturesOnBackface = 1
gradient1Display.BaseColorTexture = None
gradient1Display.NormalTexture = None
gradient1Display.NormalScale = 1.0
gradient1Display.CoatNormalTexture = None
gradient1Display.CoatNormalScale = 1.0
gradient1Display.MaterialTexture = None
gradient1Display.OcclusionStrength = 1.0
gradient1Display.AnisotropyTexture = None
gradient1Display.EmissiveTexture = None
gradient1Display.EmissiveFactor = [1.0, 1.0, 1.0]
gradient1Display.FlipTextures = 0
gradient1Display.BackfaceRepresentation = 'Follow Frontface'
gradient1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
gradient1Display.BackfaceOpacity = 1.0
gradient1Display.Position = [0.0, 0.0, 0.0]
gradient1Display.Scale = [1.0, 1.0, 1.0]
gradient1Display.Orientation = [0.0, 0.0, 0.0]
gradient1Display.Origin = [0.0, 0.0, 0.0]
gradient1Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
gradient1Display.Pickable = 1
gradient1Display.Triangulate = 0
gradient1Display.UseShaderReplacements = 0
gradient1Display.ShaderReplacements = ''
gradient1Display.NonlinearSubdivisionLevel = 1
gradient1Display.UseDataPartitions = 0
gradient1Display.OSPRayUseScaleArray = 'All Approximate'
gradient1Display.OSPRayScaleArray = 'Pressure'
gradient1Display.OSPRayScaleFunction = 'PiecewiseFunction'
gradient1Display.OSPRayMaterial = 'None'
gradient1Display.BlockSelectors = ['/']
gradient1Display.BlockColors = []
gradient1Display.BlockOpacities = []
gradient1Display.Orient = 0
gradient1Display.OrientationMode = 'Direction'
gradient1Display.SelectOrientationVectors = 'Velocity'
gradient1Display.Scaling = 0
gradient1Display.ScaleMode = 'No Data Scaling Off'
gradient1Display.ScaleFactor = 307.20000000000005
gradient1Display.SelectScaleArray = 'Pressure'
gradient1Display.GlyphType = 'Arrow'
gradient1Display.UseGlyphTable = 0
gradient1Display.GlyphTableIndexArray = 'Pressure'
gradient1Display.UseCompositeGlyphTable = 0
gradient1Display.UseGlyphCullingAndLOD = 0
gradient1Display.LODValues = []
gradient1Display.ColorByLODIndex = 0
gradient1Display.GaussianRadius = 15.36
gradient1Display.ShaderPreset = 'Sphere'
gradient1Display.CustomTriangleScale = 3
gradient1Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
gradient1Display.Emissive = 0
gradient1Display.ScaleByArray = 0
gradient1Display.SetScaleArray = ['POINTS', 'Pressure']
gradient1Display.ScaleArrayComponent = ''
gradient1Display.UseScaleFunction = 1
gradient1Display.ScaleTransferFunction = 'PiecewiseFunction'
gradient1Display.OpacityByArray = 0
gradient1Display.OpacityArray = ['POINTS', 'Pressure']
gradient1Display.OpacityArrayComponent = ''
gradient1Display.OpacityTransferFunction = 'PiecewiseFunction'
gradient1Display.DataAxesGrid = 'GridAxesRepresentation'
gradient1Display.SelectionCellLabelBold = 0
gradient1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
gradient1Display.SelectionCellLabelFontFamily = 'Arial'
gradient1Display.SelectionCellLabelFontFile = ''
gradient1Display.SelectionCellLabelFontSize = 18
gradient1Display.SelectionCellLabelItalic = 0
gradient1Display.SelectionCellLabelJustification = 'Left'
gradient1Display.SelectionCellLabelOpacity = 1.0
gradient1Display.SelectionCellLabelShadow = 0
gradient1Display.SelectionPointLabelBold = 0
gradient1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
gradient1Display.SelectionPointLabelFontFamily = 'Arial'
gradient1Display.SelectionPointLabelFontFile = ''
gradient1Display.SelectionPointLabelFontSize = 18
gradient1Display.SelectionPointLabelItalic = 0
gradient1Display.SelectionPointLabelJustification = 'Left'
gradient1Display.SelectionPointLabelOpacity = 1.0
gradient1Display.SelectionPointLabelShadow = 0
gradient1Display.PolarAxes = 'PolarAxesRepresentation'
gradient1Display.ScalarOpacityUnitDistance = 10.076780877341227
gradient1Display.ScalarOpacityFunction = None
gradient1Display.UseSeparateOpacityArray = 0
gradient1Display.OpacityArrayName = ['POINTS', 'Pressure']
gradient1Display.OpacityComponent = ''
gradient1Display.VolumeRenderingMode = 'Smart'
gradient1Display.Shade = 0
gradient1Display.BlendMode = 'Composite'
gradient1Display.IsosurfaceValues = [0.6992536187171936]
gradient1Display.SliceFunction = 'Plane'
gradient1Display.UseCropping = 0
gradient1Display.CroppingOrigin = [0.0, 0.0, 0.0]
gradient1Display.CroppingScale = [1.0, 1.0, 1.0]
gradient1Display.SliceMode = 'XY Plane'
gradient1Display.Slice = 32

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
gradient1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
gradient1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
gradient1Display.GlyphType.TipResolution = 6
gradient1Display.GlyphType.TipRadius = 0.1
gradient1Display.GlyphType.TipLength = 0.35
gradient1Display.GlyphType.ShaftResolution = 6
gradient1Display.GlyphType.ShaftRadius = 0.03
gradient1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
gradient1Display.ScaleTransferFunction.Points = [-1.0521329641342163, 0.0, 0.5, 0.0, 2.4506402015686035, 1.0, 0.5, 0.0]
gradient1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
gradient1Display.OpacityTransferFunction.Points = [-1.0521329641342163, 0.0, 0.5, 0.0, 2.4506402015686035, 1.0, 0.5, 0.0]
gradient1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
gradient1Display.DataAxesGrid.XTitle = 'X Axis'
gradient1Display.DataAxesGrid.YTitle = 'Y Axis'
gradient1Display.DataAxesGrid.ZTitle = 'Z Axis'
gradient1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
gradient1Display.DataAxesGrid.XTitleFontFile = ''
gradient1Display.DataAxesGrid.XTitleBold = 0
gradient1Display.DataAxesGrid.XTitleItalic = 0
gradient1Display.DataAxesGrid.XTitleFontSize = 12
gradient1Display.DataAxesGrid.XTitleShadow = 0
gradient1Display.DataAxesGrid.XTitleOpacity = 1.0
gradient1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
gradient1Display.DataAxesGrid.YTitleFontFile = ''
gradient1Display.DataAxesGrid.YTitleBold = 0
gradient1Display.DataAxesGrid.YTitleItalic = 0
gradient1Display.DataAxesGrid.YTitleFontSize = 12
gradient1Display.DataAxesGrid.YTitleShadow = 0
gradient1Display.DataAxesGrid.YTitleOpacity = 1.0
gradient1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
gradient1Display.DataAxesGrid.ZTitleFontFile = ''
gradient1Display.DataAxesGrid.ZTitleBold = 0
gradient1Display.DataAxesGrid.ZTitleItalic = 0
gradient1Display.DataAxesGrid.ZTitleFontSize = 12
gradient1Display.DataAxesGrid.ZTitleShadow = 0
gradient1Display.DataAxesGrid.ZTitleOpacity = 1.0
gradient1Display.DataAxesGrid.FacesToRender = 63
gradient1Display.DataAxesGrid.CullBackface = 0
gradient1Display.DataAxesGrid.CullFrontface = 1
gradient1Display.DataAxesGrid.ShowGrid = 0
gradient1Display.DataAxesGrid.ShowEdges = 1
gradient1Display.DataAxesGrid.ShowTicks = 1
gradient1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
gradient1Display.DataAxesGrid.AxesToLabel = 63
gradient1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
gradient1Display.DataAxesGrid.XLabelFontFile = ''
gradient1Display.DataAxesGrid.XLabelBold = 0
gradient1Display.DataAxesGrid.XLabelItalic = 0
gradient1Display.DataAxesGrid.XLabelFontSize = 12
gradient1Display.DataAxesGrid.XLabelShadow = 0
gradient1Display.DataAxesGrid.XLabelOpacity = 1.0
gradient1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
gradient1Display.DataAxesGrid.YLabelFontFile = ''
gradient1Display.DataAxesGrid.YLabelBold = 0
gradient1Display.DataAxesGrid.YLabelItalic = 0
gradient1Display.DataAxesGrid.YLabelFontSize = 12
gradient1Display.DataAxesGrid.YLabelShadow = 0
gradient1Display.DataAxesGrid.YLabelOpacity = 1.0
gradient1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
gradient1Display.DataAxesGrid.ZLabelFontFile = ''
gradient1Display.DataAxesGrid.ZLabelBold = 0
gradient1Display.DataAxesGrid.ZLabelItalic = 0
gradient1Display.DataAxesGrid.ZLabelFontSize = 12
gradient1Display.DataAxesGrid.ZLabelShadow = 0
gradient1Display.DataAxesGrid.ZLabelOpacity = 1.0
gradient1Display.DataAxesGrid.XAxisNotation = 'Mixed'
gradient1Display.DataAxesGrid.XAxisPrecision = 2
gradient1Display.DataAxesGrid.XAxisUseCustomLabels = 0
gradient1Display.DataAxesGrid.XAxisLabels = []
gradient1Display.DataAxesGrid.YAxisNotation = 'Mixed'
gradient1Display.DataAxesGrid.YAxisPrecision = 2
gradient1Display.DataAxesGrid.YAxisUseCustomLabels = 0
gradient1Display.DataAxesGrid.YAxisLabels = []
gradient1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
gradient1Display.DataAxesGrid.ZAxisPrecision = 2
gradient1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
gradient1Display.DataAxesGrid.ZAxisLabels = []
gradient1Display.DataAxesGrid.UseCustomBounds = 0
gradient1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
gradient1Display.PolarAxes.Visibility = 0
gradient1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
gradient1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
gradient1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
gradient1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
gradient1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
gradient1Display.PolarAxes.EnableCustomRange = 0
gradient1Display.PolarAxes.CustomRange = [0.0, 1.0]
gradient1Display.PolarAxes.PolarAxisVisibility = 1
gradient1Display.PolarAxes.RadialAxesVisibility = 1
gradient1Display.PolarAxes.DrawRadialGridlines = 1
gradient1Display.PolarAxes.PolarArcsVisibility = 1
gradient1Display.PolarAxes.DrawPolarArcsGridlines = 1
gradient1Display.PolarAxes.NumberOfRadialAxes = 0
gradient1Display.PolarAxes.AutoSubdividePolarAxis = 1
gradient1Display.PolarAxes.NumberOfPolarAxis = 0
gradient1Display.PolarAxes.MinimumRadius = 0.0
gradient1Display.PolarAxes.MinimumAngle = 0.0
gradient1Display.PolarAxes.MaximumAngle = 90.0
gradient1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
gradient1Display.PolarAxes.Ratio = 1.0
gradient1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
gradient1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
gradient1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
gradient1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
gradient1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
gradient1Display.PolarAxes.PolarAxisTitleVisibility = 1
gradient1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
gradient1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
gradient1Display.PolarAxes.PolarLabelVisibility = 1
gradient1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
gradient1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
gradient1Display.PolarAxes.RadialLabelVisibility = 1
gradient1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
gradient1Display.PolarAxes.RadialLabelLocation = 'Bottom'
gradient1Display.PolarAxes.RadialUnitsVisibility = 1
gradient1Display.PolarAxes.ScreenSize = 10.0
gradient1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
gradient1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
gradient1Display.PolarAxes.PolarAxisTitleFontFile = ''
gradient1Display.PolarAxes.PolarAxisTitleBold = 0
gradient1Display.PolarAxes.PolarAxisTitleItalic = 0
gradient1Display.PolarAxes.PolarAxisTitleShadow = 0
gradient1Display.PolarAxes.PolarAxisTitleFontSize = 12
gradient1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
gradient1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
gradient1Display.PolarAxes.PolarAxisLabelFontFile = ''
gradient1Display.PolarAxes.PolarAxisLabelBold = 0
gradient1Display.PolarAxes.PolarAxisLabelItalic = 0
gradient1Display.PolarAxes.PolarAxisLabelShadow = 0
gradient1Display.PolarAxes.PolarAxisLabelFontSize = 12
gradient1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
gradient1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
gradient1Display.PolarAxes.LastRadialAxisTextFontFile = ''
gradient1Display.PolarAxes.LastRadialAxisTextBold = 0
gradient1Display.PolarAxes.LastRadialAxisTextItalic = 0
gradient1Display.PolarAxes.LastRadialAxisTextShadow = 0
gradient1Display.PolarAxes.LastRadialAxisTextFontSize = 12
gradient1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
gradient1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
gradient1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
gradient1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
gradient1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
gradient1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
gradient1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
gradient1Display.PolarAxes.EnableDistanceLOD = 1
gradient1Display.PolarAxes.DistanceLODThreshold = 0.7
gradient1Display.PolarAxes.EnableViewAngleLOD = 1
gradient1Display.PolarAxes.ViewAngleLODThreshold = 0.7
gradient1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
gradient1Display.PolarAxes.PolarTicksVisibility = 1
gradient1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
gradient1Display.PolarAxes.TickLocation = 'Both'
gradient1Display.PolarAxes.AxisTickVisibility = 1
gradient1Display.PolarAxes.AxisMinorTickVisibility = 0
gradient1Display.PolarAxes.ArcTickVisibility = 1
gradient1Display.PolarAxes.ArcMinorTickVisibility = 0
gradient1Display.PolarAxes.DeltaAngleMajor = 10.0
gradient1Display.PolarAxes.DeltaAngleMinor = 5.0
gradient1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
gradient1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
gradient1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
gradient1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
gradient1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
gradient1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
gradient1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
gradient1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
gradient1Display.PolarAxes.ArcMajorTickSize = 0.0
gradient1Display.PolarAxes.ArcTickRatioSize = 0.3
gradient1Display.PolarAxes.ArcMajorTickThickness = 1.0
gradient1Display.PolarAxes.ArcTickRatioThickness = 0.5
gradient1Display.PolarAxes.Use2DMode = 0
gradient1Display.PolarAxes.UseLogAxis = 0

# init the 'Plane' selected for 'SliceFunction'
gradient1Display.SliceFunction.Origin = [1026.0, 1.0, 130.0]
gradient1Display.SliceFunction.Normal = [1.0, 0.0, 0.0]
gradient1Display.SliceFunction.Offset = 0.0

# hide data in view
Hide(fluidvtipvd, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on renderView1
renderView1.EnableRayTracing = 1

# Properties modified on renderView1
renderView1.UseColorPaletteForBackground = 0

# Properties modified on renderView1
renderView1.Background = [1.0, 1.0, 1.0]

# hide data in view
Hide(gradient1, renderView1)

# create a new 'Contour'
contour1 = Contour(registrationName='Contour1', Input=gradient1)
contour1.ContourBy = ['POINTS', 'Pressure']
contour1.ComputeNormals = 1
contour1.ComputeGradients = 0
contour1.ComputeScalars = 1
contour1.OutputPointsPrecision = 'Same as input'
contour1.GenerateTriangles = 1
contour1.Isosurfaces = [0.6992536187171936]
contour1.PointMergeMethod = 'Uniform Binning'

# init the 'Uniform Binning' selected for 'PointMergeMethod'
contour1.PointMergeMethod.Divisions = [50, 50, 50]
contour1.PointMergeMethod.Numberofpointsperbucket = 8

# Properties modified on contour1
contour1.ContourBy = ['POINTS', 'Q Criterion']
contour1.ComputeNormals = 0
contour1.GenerateTriangles = 0
contour1.Isosurfaces = [0.001]

# show data in view
contour1Display = Show(contour1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'QCriterion'
qCriterionLUT = GetColorTransferFunction('QCriterion')
qCriterionLUT.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
qCriterionLUT.InterpretValuesAsCategories = 0
qCriterionLUT.AnnotationsInitialized = 0
qCriterionLUT.ShowCategoricalColorsinDataRangeOnly = 0
qCriterionLUT.RescaleOnVisibilityChange = 0
qCriterionLUT.EnableOpacityMapping = 0
qCriterionLUT.RGBPoints = [0.0010000000474974513, 0.231373, 0.298039, 0.752941, 0.001000119256787002, 0.865003, 0.865003, 0.865003, 0.0010002384660765529, 0.705882, 0.0156863, 0.14902]
qCriterionLUT.UseLogScale = 0
qCriterionLUT.UseOpacityControlPointsFreehandDrawing = 0
qCriterionLUT.ShowDataHistogram = 0
qCriterionLUT.AutomaticDataHistogramComputation = 0
qCriterionLUT.DataHistogramNumberOfBins = 10
qCriterionLUT.ColorSpace = 'Diverging'
qCriterionLUT.UseBelowRangeColor = 0
qCriterionLUT.BelowRangeColor = [0.0, 0.0, 0.0]
qCriterionLUT.UseAboveRangeColor = 0
qCriterionLUT.AboveRangeColor = [0.5, 0.5, 0.5]
qCriterionLUT.NanColor = [1.0, 1.0, 0.0]
qCriterionLUT.NanOpacity = 1.0
qCriterionLUT.Discretize = 1
qCriterionLUT.NumberOfTableValues = 256
qCriterionLUT.ScalarRangeInitialized = 1.0
qCriterionLUT.HSVWrap = 0
qCriterionLUT.VectorComponent = 0
qCriterionLUT.VectorMode = 'Magnitude'
qCriterionLUT.AllowDuplicateScalars = 1
qCriterionLUT.Annotations = []
qCriterionLUT.ActiveAnnotatedValues = []
qCriterionLUT.IndexedColors = []
qCriterionLUT.IndexedOpacities = []

# trace defaults for the display properties.
contour1Display.Selection = None
contour1Display.Representation = 'Surface'
contour1Display.ColorArrayName = ['POINTS', 'Q Criterion']
contour1Display.LookupTable = qCriterionLUT
contour1Display.MapScalars = 1
contour1Display.MultiComponentsMapping = 0
contour1Display.InterpolateScalarsBeforeMapping = 1
contour1Display.Opacity = 1.0
contour1Display.PointSize = 2.0
contour1Display.LineWidth = 1.0
contour1Display.RenderLinesAsTubes = 0
contour1Display.RenderPointsAsSpheres = 0
contour1Display.Interpolation = 'Gouraud'
contour1Display.Specular = 0.0
contour1Display.SpecularColor = [1.0, 1.0, 1.0]
contour1Display.SpecularPower = 100.0
contour1Display.Luminosity = 0.0
contour1Display.Ambient = 0.0
contour1Display.Diffuse = 1.0
contour1Display.Roughness = 0.3
contour1Display.Metallic = 0.0
contour1Display.EdgeTint = [1.0, 1.0, 1.0]
contour1Display.Anisotropy = 0.0
contour1Display.AnisotropyRotation = 0.0
contour1Display.BaseIOR = 1.5
contour1Display.CoatStrength = 0.0
contour1Display.CoatIOR = 2.0
contour1Display.CoatRoughness = 0.0
contour1Display.CoatColor = [1.0, 1.0, 1.0]
contour1Display.SelectTCoordArray = 'None'
contour1Display.SelectNormalArray = 'None'
contour1Display.SelectTangentArray = 'None'
contour1Display.Texture = None
contour1Display.RepeatTextures = 1
contour1Display.InterpolateTextures = 0
contour1Display.SeamlessU = 0
contour1Display.SeamlessV = 0
contour1Display.UseMipmapTextures = 0
contour1Display.ShowTexturesOnBackface = 1
contour1Display.BaseColorTexture = None
contour1Display.NormalTexture = None
contour1Display.NormalScale = 1.0
contour1Display.CoatNormalTexture = None
contour1Display.CoatNormalScale = 1.0
contour1Display.MaterialTexture = None
contour1Display.OcclusionStrength = 1.0
contour1Display.AnisotropyTexture = None
contour1Display.EmissiveTexture = None
contour1Display.EmissiveFactor = [1.0, 1.0, 1.0]
contour1Display.FlipTextures = 0
contour1Display.BackfaceRepresentation = 'Follow Frontface'
contour1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
contour1Display.BackfaceOpacity = 1.0
contour1Display.Position = [0.0, 0.0, 0.0]
contour1Display.Scale = [1.0, 1.0, 1.0]
contour1Display.Orientation = [0.0, 0.0, 0.0]
contour1Display.Origin = [0.0, 0.0, 0.0]
contour1Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
contour1Display.Pickable = 1
contour1Display.Triangulate = 0
contour1Display.UseShaderReplacements = 0
contour1Display.ShaderReplacements = ''
contour1Display.NonlinearSubdivisionLevel = 1
contour1Display.UseDataPartitions = 0
contour1Display.OSPRayUseScaleArray = 'All Approximate'
contour1Display.OSPRayScaleArray = 'Q Criterion'
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.OSPRayMaterial = 'None'
contour1Display.BlockSelectors = ['/']
contour1Display.BlockColors = []
contour1Display.BlockOpacities = []
contour1Display.Orient = 0
contour1Display.OrientationMode = 'Direction'
contour1Display.SelectOrientationVectors = 'Velocity'
contour1Display.Scaling = 0
contour1Display.ScaleMode = 'No Data Scaling Off'
contour1Display.ScaleFactor = 145.2976487636566
contour1Display.SelectScaleArray = 'Q Criterion'
contour1Display.GlyphType = 'Arrow'
contour1Display.UseGlyphTable = 0
contour1Display.GlyphTableIndexArray = 'Q Criterion'
contour1Display.UseCompositeGlyphTable = 0
contour1Display.UseGlyphCullingAndLOD = 0
contour1Display.LODValues = []
contour1Display.ColorByLODIndex = 0
contour1Display.GaussianRadius = 7.2648824381828305
contour1Display.ShaderPreset = 'Sphere'
contour1Display.CustomTriangleScale = 3
contour1Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
contour1Display.Emissive = 0
contour1Display.ScaleByArray = 0
contour1Display.SetScaleArray = ['POINTS', 'Q Criterion']
contour1Display.ScaleArrayComponent = ''
contour1Display.UseScaleFunction = 1
contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display.OpacityByArray = 0
contour1Display.OpacityArray = ['POINTS', 'Q Criterion']
contour1Display.OpacityArrayComponent = ''
contour1Display.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display.DataAxesGrid = 'GridAxesRepresentation'
contour1Display.SelectionCellLabelBold = 0
contour1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
contour1Display.SelectionCellLabelFontFamily = 'Arial'
contour1Display.SelectionCellLabelFontFile = ''
contour1Display.SelectionCellLabelFontSize = 18
contour1Display.SelectionCellLabelItalic = 0
contour1Display.SelectionCellLabelJustification = 'Left'
contour1Display.SelectionCellLabelOpacity = 1.0
contour1Display.SelectionCellLabelShadow = 0
contour1Display.SelectionPointLabelBold = 0
contour1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
contour1Display.SelectionPointLabelFontFamily = 'Arial'
contour1Display.SelectionPointLabelFontFile = ''
contour1Display.SelectionPointLabelFontSize = 18
contour1Display.SelectionPointLabelItalic = 0
contour1Display.SelectionPointLabelJustification = 'Left'
contour1Display.SelectionPointLabelOpacity = 1.0
contour1Display.SelectionPointLabelShadow = 0
contour1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
contour1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
contour1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
contour1Display.GlyphType.TipResolution = 6
contour1Display.GlyphType.TipRadius = 0.1
contour1Display.GlyphType.TipLength = 0.35
contour1Display.GlyphType.ShaftResolution = 6
contour1Display.GlyphType.ShaftRadius = 0.03
contour1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display.ScaleTransferFunction.Points = [0.0010000000474974513, 0.0, 0.5, 0.0, 0.0010002384660765529, 1.0, 0.5, 0.0]
contour1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display.OpacityTransferFunction.Points = [0.0010000000474974513, 0.0, 0.5, 0.0, 0.0010002384660765529, 1.0, 0.5, 0.0]
contour1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
contour1Display.DataAxesGrid.XTitle = 'X Axis'
contour1Display.DataAxesGrid.YTitle = 'Y Axis'
contour1Display.DataAxesGrid.ZTitle = 'Z Axis'
contour1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
contour1Display.DataAxesGrid.XTitleFontFile = ''
contour1Display.DataAxesGrid.XTitleBold = 0
contour1Display.DataAxesGrid.XTitleItalic = 0
contour1Display.DataAxesGrid.XTitleFontSize = 12
contour1Display.DataAxesGrid.XTitleShadow = 0
contour1Display.DataAxesGrid.XTitleOpacity = 1.0
contour1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
contour1Display.DataAxesGrid.YTitleFontFile = ''
contour1Display.DataAxesGrid.YTitleBold = 0
contour1Display.DataAxesGrid.YTitleItalic = 0
contour1Display.DataAxesGrid.YTitleFontSize = 12
contour1Display.DataAxesGrid.YTitleShadow = 0
contour1Display.DataAxesGrid.YTitleOpacity = 1.0
contour1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
contour1Display.DataAxesGrid.ZTitleFontFile = ''
contour1Display.DataAxesGrid.ZTitleBold = 0
contour1Display.DataAxesGrid.ZTitleItalic = 0
contour1Display.DataAxesGrid.ZTitleFontSize = 12
contour1Display.DataAxesGrid.ZTitleShadow = 0
contour1Display.DataAxesGrid.ZTitleOpacity = 1.0
contour1Display.DataAxesGrid.FacesToRender = 63
contour1Display.DataAxesGrid.CullBackface = 0
contour1Display.DataAxesGrid.CullFrontface = 1
contour1Display.DataAxesGrid.ShowGrid = 0
contour1Display.DataAxesGrid.ShowEdges = 1
contour1Display.DataAxesGrid.ShowTicks = 1
contour1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
contour1Display.DataAxesGrid.AxesToLabel = 63
contour1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
contour1Display.DataAxesGrid.XLabelFontFile = ''
contour1Display.DataAxesGrid.XLabelBold = 0
contour1Display.DataAxesGrid.XLabelItalic = 0
contour1Display.DataAxesGrid.XLabelFontSize = 12
contour1Display.DataAxesGrid.XLabelShadow = 0
contour1Display.DataAxesGrid.XLabelOpacity = 1.0
contour1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
contour1Display.DataAxesGrid.YLabelFontFile = ''
contour1Display.DataAxesGrid.YLabelBold = 0
contour1Display.DataAxesGrid.YLabelItalic = 0
contour1Display.DataAxesGrid.YLabelFontSize = 12
contour1Display.DataAxesGrid.YLabelShadow = 0
contour1Display.DataAxesGrid.YLabelOpacity = 1.0
contour1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
contour1Display.DataAxesGrid.ZLabelFontFile = ''
contour1Display.DataAxesGrid.ZLabelBold = 0
contour1Display.DataAxesGrid.ZLabelItalic = 0
contour1Display.DataAxesGrid.ZLabelFontSize = 12
contour1Display.DataAxesGrid.ZLabelShadow = 0
contour1Display.DataAxesGrid.ZLabelOpacity = 1.0
contour1Display.DataAxesGrid.XAxisNotation = 'Mixed'
contour1Display.DataAxesGrid.XAxisPrecision = 2
contour1Display.DataAxesGrid.XAxisUseCustomLabels = 0
contour1Display.DataAxesGrid.XAxisLabels = []
contour1Display.DataAxesGrid.YAxisNotation = 'Mixed'
contour1Display.DataAxesGrid.YAxisPrecision = 2
contour1Display.DataAxesGrid.YAxisUseCustomLabels = 0
contour1Display.DataAxesGrid.YAxisLabels = []
contour1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
contour1Display.DataAxesGrid.ZAxisPrecision = 2
contour1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
contour1Display.DataAxesGrid.ZAxisLabels = []
contour1Display.DataAxesGrid.UseCustomBounds = 0
contour1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
contour1Display.PolarAxes.Visibility = 0
contour1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
contour1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
contour1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
contour1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
contour1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
contour1Display.PolarAxes.EnableCustomRange = 0
contour1Display.PolarAxes.CustomRange = [0.0, 1.0]
contour1Display.PolarAxes.PolarAxisVisibility = 1
contour1Display.PolarAxes.RadialAxesVisibility = 1
contour1Display.PolarAxes.DrawRadialGridlines = 1
contour1Display.PolarAxes.PolarArcsVisibility = 1
contour1Display.PolarAxes.DrawPolarArcsGridlines = 1
contour1Display.PolarAxes.NumberOfRadialAxes = 0
contour1Display.PolarAxes.AutoSubdividePolarAxis = 1
contour1Display.PolarAxes.NumberOfPolarAxis = 0
contour1Display.PolarAxes.MinimumRadius = 0.0
contour1Display.PolarAxes.MinimumAngle = 0.0
contour1Display.PolarAxes.MaximumAngle = 90.0
contour1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
contour1Display.PolarAxes.Ratio = 1.0
contour1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
contour1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
contour1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
contour1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
contour1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
contour1Display.PolarAxes.PolarAxisTitleVisibility = 1
contour1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
contour1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
contour1Display.PolarAxes.PolarLabelVisibility = 1
contour1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
contour1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
contour1Display.PolarAxes.RadialLabelVisibility = 1
contour1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
contour1Display.PolarAxes.RadialLabelLocation = 'Bottom'
contour1Display.PolarAxes.RadialUnitsVisibility = 1
contour1Display.PolarAxes.ScreenSize = 10.0
contour1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
contour1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
contour1Display.PolarAxes.PolarAxisTitleFontFile = ''
contour1Display.PolarAxes.PolarAxisTitleBold = 0
contour1Display.PolarAxes.PolarAxisTitleItalic = 0
contour1Display.PolarAxes.PolarAxisTitleShadow = 0
contour1Display.PolarAxes.PolarAxisTitleFontSize = 12
contour1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
contour1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
contour1Display.PolarAxes.PolarAxisLabelFontFile = ''
contour1Display.PolarAxes.PolarAxisLabelBold = 0
contour1Display.PolarAxes.PolarAxisLabelItalic = 0
contour1Display.PolarAxes.PolarAxisLabelShadow = 0
contour1Display.PolarAxes.PolarAxisLabelFontSize = 12
contour1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
contour1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
contour1Display.PolarAxes.LastRadialAxisTextFontFile = ''
contour1Display.PolarAxes.LastRadialAxisTextBold = 0
contour1Display.PolarAxes.LastRadialAxisTextItalic = 0
contour1Display.PolarAxes.LastRadialAxisTextShadow = 0
contour1Display.PolarAxes.LastRadialAxisTextFontSize = 12
contour1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
contour1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
contour1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
contour1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
contour1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
contour1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
contour1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
contour1Display.PolarAxes.EnableDistanceLOD = 1
contour1Display.PolarAxes.DistanceLODThreshold = 0.7
contour1Display.PolarAxes.EnableViewAngleLOD = 1
contour1Display.PolarAxes.ViewAngleLODThreshold = 0.7
contour1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
contour1Display.PolarAxes.PolarTicksVisibility = 1
contour1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
contour1Display.PolarAxes.TickLocation = 'Both'
contour1Display.PolarAxes.AxisTickVisibility = 1
contour1Display.PolarAxes.AxisMinorTickVisibility = 0
contour1Display.PolarAxes.ArcTickVisibility = 1
contour1Display.PolarAxes.ArcMinorTickVisibility = 0
contour1Display.PolarAxes.DeltaAngleMajor = 10.0
contour1Display.PolarAxes.DeltaAngleMinor = 5.0
contour1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
contour1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
contour1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
contour1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
contour1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
contour1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
contour1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
contour1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
contour1Display.PolarAxes.ArcMajorTickSize = 0.0
contour1Display.PolarAxes.ArcTickRatioSize = 0.3
contour1Display.PolarAxes.ArcMajorTickThickness = 1.0
contour1Display.PolarAxes.ArcTickRatioThickness = 0.5
contour1Display.PolarAxes.Use2DMode = 0
contour1Display.PolarAxes.UseLogAxis = 0

# reset view to fit data
renderView1.ResetCamera(False)

# show color bar/color legend
contour1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get opacity transfer function/opacity map for 'QCriterion'
qCriterionPWF = GetOpacityTransferFunction('QCriterion')
qCriterionPWF.Points = [0.0010000000474974513, 0.0, 0.5, 0.0, 0.0010002384660765529, 1.0, 0.5, 0.0]
qCriterionPWF.AllowDuplicateScalars = 1
qCriterionPWF.UseLogScale = 0
qCriterionPWF.ScalarRangeInitialized = 1

# set scalar coloring
ColorBy(contour1Display, ('POINTS', 'Vorticity', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(qCriterionLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
contour1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
contour1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Vorticity'
vorticityLUT = GetColorTransferFunction('Vorticity')
vorticityLUT.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
vorticityLUT.InterpretValuesAsCategories = 0
vorticityLUT.AnnotationsInitialized = 0
vorticityLUT.ShowCategoricalColorsinDataRangeOnly = 0
vorticityLUT.RescaleOnVisibilityChange = 0
vorticityLUT.EnableOpacityMapping = 0
vorticityLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 0.15107190905083193, 0.865003, 0.865003, 0.865003, 0.30214381810166385, 0.705882, 0.0156863, 0.14902]
vorticityLUT.UseLogScale = 0
vorticityLUT.UseOpacityControlPointsFreehandDrawing = 0
vorticityLUT.ShowDataHistogram = 0
vorticityLUT.AutomaticDataHistogramComputation = 0
vorticityLUT.DataHistogramNumberOfBins = 10
vorticityLUT.ColorSpace = 'Diverging'
vorticityLUT.UseBelowRangeColor = 0
vorticityLUT.BelowRangeColor = [0.0, 0.0, 0.0]
vorticityLUT.UseAboveRangeColor = 0
vorticityLUT.AboveRangeColor = [0.5, 0.5, 0.5]
vorticityLUT.NanColor = [1.0, 1.0, 0.0]
vorticityLUT.NanOpacity = 1.0
vorticityLUT.Discretize = 1
vorticityLUT.NumberOfTableValues = 256
vorticityLUT.ScalarRangeInitialized = 1.0
vorticityLUT.HSVWrap = 0
vorticityLUT.VectorComponent = 0
vorticityLUT.VectorMode = 'Magnitude'
vorticityLUT.AllowDuplicateScalars = 1
vorticityLUT.Annotations = []
vorticityLUT.ActiveAnnotatedValues = []
vorticityLUT.IndexedColors = []
vorticityLUT.IndexedOpacities = []

# get opacity transfer function/opacity map for 'Vorticity'
vorticityPWF = GetOpacityTransferFunction('Vorticity')
vorticityPWF.Points = [0.0, 0.0, 0.5, 0.0, 0.30214381810166385, 1.0, 0.5, 0.0]
vorticityPWF.AllowDuplicateScalars = 1
vorticityPWF.UseLogScale = 0
vorticityPWF.ScalarRangeInitialized = 1

# set scalar coloring
ColorBy(contour1Display, ('POINTS', 'Vorticity', 'Z'))

# rescale color and/or opacity maps used to exactly fit the current data range
contour1Display.RescaleTransferFunctionToDataRange(False, False)

# Update a scalar bar component title.
UpdateScalarBarsComponentTitle(vorticityLUT, contour1Display)

# Hide orientation axes
renderView1.OrientationAxesVisibility = 0

# hide color bar/color legend
contour1Display.SetScalarBarVisibility(renderView1, False)

# create a new 'PVD Reader'
bodyFvtipvd = PVDReader(registrationName='bodyF.vti.pvd', FileName=f'{cwd}/16x16/1024/bodyF.vti.pvd')
bodyFvtipvd.CellArrays = []
bodyFvtipvd.PointArrays = ['Velocity', 'Pressure']
bodyFvtipvd.ColumnArrays = []

# show data in view
bodyFvtipvdDisplay = Show(bodyFvtipvd, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
bodyFvtipvdDisplay.Selection = None
bodyFvtipvdDisplay.Representation = 'Outline'
bodyFvtipvdDisplay.ColorArrayName = ['POINTS', '']
bodyFvtipvdDisplay.LookupTable = None
bodyFvtipvdDisplay.MapScalars = 1
bodyFvtipvdDisplay.MultiComponentsMapping = 0
bodyFvtipvdDisplay.InterpolateScalarsBeforeMapping = 1
bodyFvtipvdDisplay.Opacity = 1.0
bodyFvtipvdDisplay.PointSize = 2.0
bodyFvtipvdDisplay.LineWidth = 1.0
bodyFvtipvdDisplay.RenderLinesAsTubes = 0
bodyFvtipvdDisplay.RenderPointsAsSpheres = 0
bodyFvtipvdDisplay.Interpolation = 'Gouraud'
bodyFvtipvdDisplay.Specular = 0.0
bodyFvtipvdDisplay.SpecularColor = [1.0, 1.0, 1.0]
bodyFvtipvdDisplay.SpecularPower = 100.0
bodyFvtipvdDisplay.Luminosity = 0.0
bodyFvtipvdDisplay.Ambient = 0.0
bodyFvtipvdDisplay.Diffuse = 1.0
bodyFvtipvdDisplay.Roughness = 0.3
bodyFvtipvdDisplay.Metallic = 0.0
bodyFvtipvdDisplay.EdgeTint = [1.0, 1.0, 1.0]
bodyFvtipvdDisplay.Anisotropy = 0.0
bodyFvtipvdDisplay.AnisotropyRotation = 0.0
bodyFvtipvdDisplay.BaseIOR = 1.5
bodyFvtipvdDisplay.CoatStrength = 0.0
bodyFvtipvdDisplay.CoatIOR = 2.0
bodyFvtipvdDisplay.CoatRoughness = 0.0
bodyFvtipvdDisplay.CoatColor = [1.0, 1.0, 1.0]
bodyFvtipvdDisplay.SelectTCoordArray = 'None'
bodyFvtipvdDisplay.SelectNormalArray = 'None'
bodyFvtipvdDisplay.SelectTangentArray = 'None'
bodyFvtipvdDisplay.Texture = None
bodyFvtipvdDisplay.RepeatTextures = 1
bodyFvtipvdDisplay.InterpolateTextures = 0
bodyFvtipvdDisplay.SeamlessU = 0
bodyFvtipvdDisplay.SeamlessV = 0
bodyFvtipvdDisplay.UseMipmapTextures = 0
bodyFvtipvdDisplay.ShowTexturesOnBackface = 1
bodyFvtipvdDisplay.BaseColorTexture = None
bodyFvtipvdDisplay.NormalTexture = None
bodyFvtipvdDisplay.NormalScale = 1.0
bodyFvtipvdDisplay.CoatNormalTexture = None
bodyFvtipvdDisplay.CoatNormalScale = 1.0
bodyFvtipvdDisplay.MaterialTexture = None
bodyFvtipvdDisplay.OcclusionStrength = 1.0
bodyFvtipvdDisplay.AnisotropyTexture = None
bodyFvtipvdDisplay.EmissiveTexture = None
bodyFvtipvdDisplay.EmissiveFactor = [1.0, 1.0, 1.0]
bodyFvtipvdDisplay.FlipTextures = 0
bodyFvtipvdDisplay.BackfaceRepresentation = 'Follow Frontface'
bodyFvtipvdDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
bodyFvtipvdDisplay.BackfaceOpacity = 1.0
bodyFvtipvdDisplay.Position = [0.0, 0.0, 0.0]
bodyFvtipvdDisplay.Scale = [1.0, 1.0, 1.0]
bodyFvtipvdDisplay.Orientation = [0.0, 0.0, 0.0]
bodyFvtipvdDisplay.Origin = [0.0, 0.0, 0.0]
bodyFvtipvdDisplay.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
bodyFvtipvdDisplay.Pickable = 1
bodyFvtipvdDisplay.Triangulate = 0
bodyFvtipvdDisplay.UseShaderReplacements = 0
bodyFvtipvdDisplay.ShaderReplacements = ''
bodyFvtipvdDisplay.NonlinearSubdivisionLevel = 1
bodyFvtipvdDisplay.UseDataPartitions = 0
bodyFvtipvdDisplay.OSPRayUseScaleArray = 'All Approximate'
bodyFvtipvdDisplay.OSPRayScaleArray = 'Pressure'
bodyFvtipvdDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
bodyFvtipvdDisplay.OSPRayMaterial = 'None'
bodyFvtipvdDisplay.BlockSelectors = ['/']
bodyFvtipvdDisplay.BlockColors = []
bodyFvtipvdDisplay.BlockOpacities = []
bodyFvtipvdDisplay.Orient = 0
bodyFvtipvdDisplay.OrientationMode = 'Direction'
bodyFvtipvdDisplay.SelectOrientationVectors = 'Velocity'
bodyFvtipvdDisplay.Scaling = 0
bodyFvtipvdDisplay.ScaleMode = 'No Data Scaling Off'
bodyFvtipvdDisplay.ScaleFactor = 307.20000000000005
bodyFvtipvdDisplay.SelectScaleArray = 'Pressure'
bodyFvtipvdDisplay.GlyphType = 'Arrow'
bodyFvtipvdDisplay.UseGlyphTable = 0
bodyFvtipvdDisplay.GlyphTableIndexArray = 'Pressure'
bodyFvtipvdDisplay.UseCompositeGlyphTable = 0
bodyFvtipvdDisplay.UseGlyphCullingAndLOD = 0
bodyFvtipvdDisplay.LODValues = []
bodyFvtipvdDisplay.ColorByLODIndex = 0
bodyFvtipvdDisplay.GaussianRadius = 15.36
bodyFvtipvdDisplay.ShaderPreset = 'Sphere'
bodyFvtipvdDisplay.CustomTriangleScale = 3
bodyFvtipvdDisplay.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
bodyFvtipvdDisplay.Emissive = 0
bodyFvtipvdDisplay.ScaleByArray = 0
bodyFvtipvdDisplay.SetScaleArray = ['POINTS', 'Pressure']
bodyFvtipvdDisplay.ScaleArrayComponent = ''
bodyFvtipvdDisplay.UseScaleFunction = 1
bodyFvtipvdDisplay.ScaleTransferFunction = 'PiecewiseFunction'
bodyFvtipvdDisplay.OpacityByArray = 0
bodyFvtipvdDisplay.OpacityArray = ['POINTS', 'Pressure']
bodyFvtipvdDisplay.OpacityArrayComponent = ''
bodyFvtipvdDisplay.OpacityTransferFunction = 'PiecewiseFunction'
bodyFvtipvdDisplay.DataAxesGrid = 'GridAxesRepresentation'
bodyFvtipvdDisplay.SelectionCellLabelBold = 0
bodyFvtipvdDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
bodyFvtipvdDisplay.SelectionCellLabelFontFamily = 'Arial'
bodyFvtipvdDisplay.SelectionCellLabelFontFile = ''
bodyFvtipvdDisplay.SelectionCellLabelFontSize = 18
bodyFvtipvdDisplay.SelectionCellLabelItalic = 0
bodyFvtipvdDisplay.SelectionCellLabelJustification = 'Left'
bodyFvtipvdDisplay.SelectionCellLabelOpacity = 1.0
bodyFvtipvdDisplay.SelectionCellLabelShadow = 0
bodyFvtipvdDisplay.SelectionPointLabelBold = 0
bodyFvtipvdDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
bodyFvtipvdDisplay.SelectionPointLabelFontFamily = 'Arial'
bodyFvtipvdDisplay.SelectionPointLabelFontFile = ''
bodyFvtipvdDisplay.SelectionPointLabelFontSize = 18
bodyFvtipvdDisplay.SelectionPointLabelItalic = 0
bodyFvtipvdDisplay.SelectionPointLabelJustification = 'Left'
bodyFvtipvdDisplay.SelectionPointLabelOpacity = 1.0
bodyFvtipvdDisplay.SelectionPointLabelShadow = 0
bodyFvtipvdDisplay.PolarAxes = 'PolarAxesRepresentation'
bodyFvtipvdDisplay.ScalarOpacityUnitDistance = 10.076780877341227
bodyFvtipvdDisplay.ScalarOpacityFunction = None
bodyFvtipvdDisplay.UseSeparateOpacityArray = 0
bodyFvtipvdDisplay.OpacityArrayName = ['POINTS', 'Pressure']
bodyFvtipvdDisplay.OpacityComponent = ''
bodyFvtipvdDisplay.VolumeRenderingMode = 'Smart'
bodyFvtipvdDisplay.Shade = 0
bodyFvtipvdDisplay.BlendMode = 'Composite'
bodyFvtipvdDisplay.IsosurfaceValues = [777.9980182647705]
bodyFvtipvdDisplay.SliceFunction = 'Plane'
bodyFvtipvdDisplay.UseCropping = 0
bodyFvtipvdDisplay.CroppingOrigin = [0.0, 0.0, 0.0]
bodyFvtipvdDisplay.CroppingScale = [1.0, 1.0, 1.0]
bodyFvtipvdDisplay.SliceMode = 'XY Plane'
bodyFvtipvdDisplay.Slice = 32

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
bodyFvtipvdDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
bodyFvtipvdDisplay.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
bodyFvtipvdDisplay.GlyphType.TipResolution = 6
bodyFvtipvdDisplay.GlyphType.TipRadius = 0.1
bodyFvtipvdDisplay.GlyphType.TipLength = 0.35
bodyFvtipvdDisplay.GlyphType.ShaftResolution = 6
bodyFvtipvdDisplay.GlyphType.ShaftRadius = 0.03
bodyFvtipvdDisplay.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
bodyFvtipvdDisplay.ScaleTransferFunction.Points = [-23.781307220458984, 0.0, 0.5, 0.0, 1579.77734375, 1.0, 0.5, 0.0]
bodyFvtipvdDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
bodyFvtipvdDisplay.OpacityTransferFunction.Points = [-23.781307220458984, 0.0, 0.5, 0.0, 1579.77734375, 1.0, 0.5, 0.0]
bodyFvtipvdDisplay.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
bodyFvtipvdDisplay.DataAxesGrid.XTitle = 'X Axis'
bodyFvtipvdDisplay.DataAxesGrid.YTitle = 'Y Axis'
bodyFvtipvdDisplay.DataAxesGrid.ZTitle = 'Z Axis'
bodyFvtipvdDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
bodyFvtipvdDisplay.DataAxesGrid.XTitleFontFile = ''
bodyFvtipvdDisplay.DataAxesGrid.XTitleBold = 0
bodyFvtipvdDisplay.DataAxesGrid.XTitleItalic = 0
bodyFvtipvdDisplay.DataAxesGrid.XTitleFontSize = 12
bodyFvtipvdDisplay.DataAxesGrid.XTitleShadow = 0
bodyFvtipvdDisplay.DataAxesGrid.XTitleOpacity = 1.0
bodyFvtipvdDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
bodyFvtipvdDisplay.DataAxesGrid.YTitleFontFile = ''
bodyFvtipvdDisplay.DataAxesGrid.YTitleBold = 0
bodyFvtipvdDisplay.DataAxesGrid.YTitleItalic = 0
bodyFvtipvdDisplay.DataAxesGrid.YTitleFontSize = 12
bodyFvtipvdDisplay.DataAxesGrid.YTitleShadow = 0
bodyFvtipvdDisplay.DataAxesGrid.YTitleOpacity = 1.0
bodyFvtipvdDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
bodyFvtipvdDisplay.DataAxesGrid.ZTitleFontFile = ''
bodyFvtipvdDisplay.DataAxesGrid.ZTitleBold = 0
bodyFvtipvdDisplay.DataAxesGrid.ZTitleItalic = 0
bodyFvtipvdDisplay.DataAxesGrid.ZTitleFontSize = 12
bodyFvtipvdDisplay.DataAxesGrid.ZTitleShadow = 0
bodyFvtipvdDisplay.DataAxesGrid.ZTitleOpacity = 1.0
bodyFvtipvdDisplay.DataAxesGrid.FacesToRender = 63
bodyFvtipvdDisplay.DataAxesGrid.CullBackface = 0
bodyFvtipvdDisplay.DataAxesGrid.CullFrontface = 1
bodyFvtipvdDisplay.DataAxesGrid.ShowGrid = 0
bodyFvtipvdDisplay.DataAxesGrid.ShowEdges = 1
bodyFvtipvdDisplay.DataAxesGrid.ShowTicks = 1
bodyFvtipvdDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
bodyFvtipvdDisplay.DataAxesGrid.AxesToLabel = 63
bodyFvtipvdDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
bodyFvtipvdDisplay.DataAxesGrid.XLabelFontFile = ''
bodyFvtipvdDisplay.DataAxesGrid.XLabelBold = 0
bodyFvtipvdDisplay.DataAxesGrid.XLabelItalic = 0
bodyFvtipvdDisplay.DataAxesGrid.XLabelFontSize = 12
bodyFvtipvdDisplay.DataAxesGrid.XLabelShadow = 0
bodyFvtipvdDisplay.DataAxesGrid.XLabelOpacity = 1.0
bodyFvtipvdDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
bodyFvtipvdDisplay.DataAxesGrid.YLabelFontFile = ''
bodyFvtipvdDisplay.DataAxesGrid.YLabelBold = 0
bodyFvtipvdDisplay.DataAxesGrid.YLabelItalic = 0
bodyFvtipvdDisplay.DataAxesGrid.YLabelFontSize = 12
bodyFvtipvdDisplay.DataAxesGrid.YLabelShadow = 0
bodyFvtipvdDisplay.DataAxesGrid.YLabelOpacity = 1.0
bodyFvtipvdDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
bodyFvtipvdDisplay.DataAxesGrid.ZLabelFontFile = ''
bodyFvtipvdDisplay.DataAxesGrid.ZLabelBold = 0
bodyFvtipvdDisplay.DataAxesGrid.ZLabelItalic = 0
bodyFvtipvdDisplay.DataAxesGrid.ZLabelFontSize = 12
bodyFvtipvdDisplay.DataAxesGrid.ZLabelShadow = 0
bodyFvtipvdDisplay.DataAxesGrid.ZLabelOpacity = 1.0
bodyFvtipvdDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
bodyFvtipvdDisplay.DataAxesGrid.XAxisPrecision = 2
bodyFvtipvdDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
bodyFvtipvdDisplay.DataAxesGrid.XAxisLabels = []
bodyFvtipvdDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
bodyFvtipvdDisplay.DataAxesGrid.YAxisPrecision = 2
bodyFvtipvdDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
bodyFvtipvdDisplay.DataAxesGrid.YAxisLabels = []
bodyFvtipvdDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
bodyFvtipvdDisplay.DataAxesGrid.ZAxisPrecision = 2
bodyFvtipvdDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
bodyFvtipvdDisplay.DataAxesGrid.ZAxisLabels = []
bodyFvtipvdDisplay.DataAxesGrid.UseCustomBounds = 0
bodyFvtipvdDisplay.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
bodyFvtipvdDisplay.PolarAxes.Visibility = 0
bodyFvtipvdDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
bodyFvtipvdDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
bodyFvtipvdDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
bodyFvtipvdDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
bodyFvtipvdDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
bodyFvtipvdDisplay.PolarAxes.EnableCustomRange = 0
bodyFvtipvdDisplay.PolarAxes.CustomRange = [0.0, 1.0]
bodyFvtipvdDisplay.PolarAxes.PolarAxisVisibility = 1
bodyFvtipvdDisplay.PolarAxes.RadialAxesVisibility = 1
bodyFvtipvdDisplay.PolarAxes.DrawRadialGridlines = 1
bodyFvtipvdDisplay.PolarAxes.PolarArcsVisibility = 1
bodyFvtipvdDisplay.PolarAxes.DrawPolarArcsGridlines = 1
bodyFvtipvdDisplay.PolarAxes.NumberOfRadialAxes = 0
bodyFvtipvdDisplay.PolarAxes.AutoSubdividePolarAxis = 1
bodyFvtipvdDisplay.PolarAxes.NumberOfPolarAxis = 0
bodyFvtipvdDisplay.PolarAxes.MinimumRadius = 0.0
bodyFvtipvdDisplay.PolarAxes.MinimumAngle = 0.0
bodyFvtipvdDisplay.PolarAxes.MaximumAngle = 90.0
bodyFvtipvdDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
bodyFvtipvdDisplay.PolarAxes.Ratio = 1.0
bodyFvtipvdDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
bodyFvtipvdDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
bodyFvtipvdDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
bodyFvtipvdDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
bodyFvtipvdDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
bodyFvtipvdDisplay.PolarAxes.PolarAxisTitleVisibility = 1
bodyFvtipvdDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
bodyFvtipvdDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
bodyFvtipvdDisplay.PolarAxes.PolarLabelVisibility = 1
bodyFvtipvdDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
bodyFvtipvdDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
bodyFvtipvdDisplay.PolarAxes.RadialLabelVisibility = 1
bodyFvtipvdDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
bodyFvtipvdDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
bodyFvtipvdDisplay.PolarAxes.RadialUnitsVisibility = 1
bodyFvtipvdDisplay.PolarAxes.ScreenSize = 10.0
bodyFvtipvdDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
bodyFvtipvdDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
bodyFvtipvdDisplay.PolarAxes.PolarAxisTitleFontFile = ''
bodyFvtipvdDisplay.PolarAxes.PolarAxisTitleBold = 0
bodyFvtipvdDisplay.PolarAxes.PolarAxisTitleItalic = 0
bodyFvtipvdDisplay.PolarAxes.PolarAxisTitleShadow = 0
bodyFvtipvdDisplay.PolarAxes.PolarAxisTitleFontSize = 12
bodyFvtipvdDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
bodyFvtipvdDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
bodyFvtipvdDisplay.PolarAxes.PolarAxisLabelFontFile = ''
bodyFvtipvdDisplay.PolarAxes.PolarAxisLabelBold = 0
bodyFvtipvdDisplay.PolarAxes.PolarAxisLabelItalic = 0
bodyFvtipvdDisplay.PolarAxes.PolarAxisLabelShadow = 0
bodyFvtipvdDisplay.PolarAxes.PolarAxisLabelFontSize = 12
bodyFvtipvdDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
bodyFvtipvdDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
bodyFvtipvdDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
bodyFvtipvdDisplay.PolarAxes.LastRadialAxisTextBold = 0
bodyFvtipvdDisplay.PolarAxes.LastRadialAxisTextItalic = 0
bodyFvtipvdDisplay.PolarAxes.LastRadialAxisTextShadow = 0
bodyFvtipvdDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
bodyFvtipvdDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
bodyFvtipvdDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
bodyFvtipvdDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
bodyFvtipvdDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
bodyFvtipvdDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
bodyFvtipvdDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
bodyFvtipvdDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
bodyFvtipvdDisplay.PolarAxes.EnableDistanceLOD = 1
bodyFvtipvdDisplay.PolarAxes.DistanceLODThreshold = 0.7
bodyFvtipvdDisplay.PolarAxes.EnableViewAngleLOD = 1
bodyFvtipvdDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
bodyFvtipvdDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
bodyFvtipvdDisplay.PolarAxes.PolarTicksVisibility = 1
bodyFvtipvdDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
bodyFvtipvdDisplay.PolarAxes.TickLocation = 'Both'
bodyFvtipvdDisplay.PolarAxes.AxisTickVisibility = 1
bodyFvtipvdDisplay.PolarAxes.AxisMinorTickVisibility = 0
bodyFvtipvdDisplay.PolarAxes.ArcTickVisibility = 1
bodyFvtipvdDisplay.PolarAxes.ArcMinorTickVisibility = 0
bodyFvtipvdDisplay.PolarAxes.DeltaAngleMajor = 10.0
bodyFvtipvdDisplay.PolarAxes.DeltaAngleMinor = 5.0
bodyFvtipvdDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
bodyFvtipvdDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
bodyFvtipvdDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
bodyFvtipvdDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
bodyFvtipvdDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
bodyFvtipvdDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
bodyFvtipvdDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
bodyFvtipvdDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
bodyFvtipvdDisplay.PolarAxes.ArcMajorTickSize = 0.0
bodyFvtipvdDisplay.PolarAxes.ArcTickRatioSize = 0.3
bodyFvtipvdDisplay.PolarAxes.ArcMajorTickThickness = 1.0
bodyFvtipvdDisplay.PolarAxes.ArcTickRatioThickness = 0.5
bodyFvtipvdDisplay.PolarAxes.Use2DMode = 0
bodyFvtipvdDisplay.PolarAxes.UseLogAxis = 0

# init the 'Plane' selected for 'SliceFunction'
bodyFvtipvdDisplay.SliceFunction.Origin = [1026.0, 1.0, 130.0]
bodyFvtipvdDisplay.SliceFunction.Normal = [1.0, 0.0, 0.0]
bodyFvtipvdDisplay.SliceFunction.Offset = 0.0

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Iso Volume'
isoVolume1 = IsoVolume(registrationName='IsoVolume1', Input=bodyFvtipvd)
isoVolume1.InputScalars = ['POINTS', 'Pressure']
isoVolume1.ThresholdRange = [-23.781307220458984, 1579.77734375]

# Properties modified on isoVolume1
isoVolume1.ThresholdRange = [-23.781307220458984, 1.0]

# show data in view
isoVolume1Display = Show(isoVolume1, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'Pressure'
pressureLUT = GetColorTransferFunction('Pressure')
pressureLUT.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
pressureLUT.InterpretValuesAsCategories = 0
pressureLUT.AnnotationsInitialized = 0
pressureLUT.ShowCategoricalColorsinDataRangeOnly = 0
pressureLUT.RescaleOnVisibilityChange = 0
pressureLUT.EnableOpacityMapping = 0
pressureLUT.RGBPoints = [-23.781307220458984, 0.231373, 0.298039, 0.752941, -11.390653610229492, 0.865003, 0.865003, 0.865003, 1.0, 0.705882, 0.0156863, 0.14902]
pressureLUT.UseLogScale = 0
pressureLUT.UseOpacityControlPointsFreehandDrawing = 0
pressureLUT.ShowDataHistogram = 0
pressureLUT.AutomaticDataHistogramComputation = 0
pressureLUT.DataHistogramNumberOfBins = 10
pressureLUT.ColorSpace = 'Diverging'
pressureLUT.UseBelowRangeColor = 0
pressureLUT.BelowRangeColor = [0.0, 0.0, 0.0]
pressureLUT.UseAboveRangeColor = 0
pressureLUT.AboveRangeColor = [0.5, 0.5, 0.5]
pressureLUT.NanColor = [1.0, 1.0, 0.0]
pressureLUT.NanOpacity = 1.0
pressureLUT.Discretize = 1
pressureLUT.NumberOfTableValues = 256
pressureLUT.ScalarRangeInitialized = 1.0
pressureLUT.HSVWrap = 0
pressureLUT.VectorComponent = 0
pressureLUT.VectorMode = 'Magnitude'
pressureLUT.AllowDuplicateScalars = 1
pressureLUT.Annotations = []
pressureLUT.ActiveAnnotatedValues = []
pressureLUT.IndexedColors = []
pressureLUT.IndexedOpacities = []

# get opacity transfer function/opacity map for 'Pressure'
pressurePWF = GetOpacityTransferFunction('Pressure')
pressurePWF.Points = [-23.781307220458984, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
pressurePWF.AllowDuplicateScalars = 1
pressurePWF.UseLogScale = 0
pressurePWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
isoVolume1Display.Selection = None
isoVolume1Display.Representation = 'Surface'
isoVolume1Display.ColorArrayName = ['POINTS', 'Pressure']
isoVolume1Display.LookupTable = pressureLUT
isoVolume1Display.MapScalars = 1
isoVolume1Display.MultiComponentsMapping = 0
isoVolume1Display.InterpolateScalarsBeforeMapping = 1
isoVolume1Display.Opacity = 1.0
isoVolume1Display.PointSize = 2.0
isoVolume1Display.LineWidth = 1.0
isoVolume1Display.RenderLinesAsTubes = 0
isoVolume1Display.RenderPointsAsSpheres = 0
isoVolume1Display.Interpolation = 'Gouraud'
isoVolume1Display.Specular = 0.0
isoVolume1Display.SpecularColor = [1.0, 1.0, 1.0]
isoVolume1Display.SpecularPower = 100.0
isoVolume1Display.Luminosity = 0.0
isoVolume1Display.Ambient = 0.0
isoVolume1Display.Diffuse = 1.0
isoVolume1Display.Roughness = 0.3
isoVolume1Display.Metallic = 0.0
isoVolume1Display.EdgeTint = [1.0, 1.0, 1.0]
isoVolume1Display.Anisotropy = 0.0
isoVolume1Display.AnisotropyRotation = 0.0
isoVolume1Display.BaseIOR = 1.5
isoVolume1Display.CoatStrength = 0.0
isoVolume1Display.CoatIOR = 2.0
isoVolume1Display.CoatRoughness = 0.0
isoVolume1Display.CoatColor = [1.0, 1.0, 1.0]
isoVolume1Display.SelectTCoordArray = 'None'
isoVolume1Display.SelectNormalArray = 'None'
isoVolume1Display.SelectTangentArray = 'None'
isoVolume1Display.Texture = None
isoVolume1Display.RepeatTextures = 1
isoVolume1Display.InterpolateTextures = 0
isoVolume1Display.SeamlessU = 0
isoVolume1Display.SeamlessV = 0
isoVolume1Display.UseMipmapTextures = 0
isoVolume1Display.ShowTexturesOnBackface = 1
isoVolume1Display.BaseColorTexture = None
isoVolume1Display.NormalTexture = None
isoVolume1Display.NormalScale = 1.0
isoVolume1Display.CoatNormalTexture = None
isoVolume1Display.CoatNormalScale = 1.0
isoVolume1Display.MaterialTexture = None
isoVolume1Display.OcclusionStrength = 1.0
isoVolume1Display.AnisotropyTexture = None
isoVolume1Display.EmissiveTexture = None
isoVolume1Display.EmissiveFactor = [1.0, 1.0, 1.0]
isoVolume1Display.FlipTextures = 0
isoVolume1Display.BackfaceRepresentation = 'Follow Frontface'
isoVolume1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
isoVolume1Display.BackfaceOpacity = 1.0
isoVolume1Display.Position = [0.0, 0.0, 0.0]
isoVolume1Display.Scale = [1.0, 1.0, 1.0]
isoVolume1Display.Orientation = [0.0, 0.0, 0.0]
isoVolume1Display.Origin = [0.0, 0.0, 0.0]
isoVolume1Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
isoVolume1Display.Pickable = 1
isoVolume1Display.Triangulate = 0
isoVolume1Display.UseShaderReplacements = 0
isoVolume1Display.ShaderReplacements = ''
isoVolume1Display.NonlinearSubdivisionLevel = 1
isoVolume1Display.UseDataPartitions = 0
isoVolume1Display.OSPRayUseScaleArray = 'All Approximate'
isoVolume1Display.OSPRayScaleArray = 'Pressure'
isoVolume1Display.OSPRayScaleFunction = 'PiecewiseFunction'
isoVolume1Display.OSPRayMaterial = 'None'
isoVolume1Display.BlockSelectors = ['/']
isoVolume1Display.BlockColors = []
isoVolume1Display.BlockOpacities = []
isoVolume1Display.Orient = 0
isoVolume1Display.OrientationMode = 'Direction'
isoVolume1Display.SelectOrientationVectors = 'Velocity'
isoVolume1Display.Scaling = 0
isoVolume1Display.ScaleMode = 'No Data Scaling Off'
isoVolume1Display.ScaleFactor = 102.60000000000001
isoVolume1Display.SelectScaleArray = 'Pressure'
isoVolume1Display.GlyphType = 'Arrow'
isoVolume1Display.UseGlyphTable = 0
isoVolume1Display.GlyphTableIndexArray = 'Pressure'
isoVolume1Display.UseCompositeGlyphTable = 0
isoVolume1Display.UseGlyphCullingAndLOD = 0
isoVolume1Display.LODValues = []
isoVolume1Display.ColorByLODIndex = 0
isoVolume1Display.GaussianRadius = 5.13
isoVolume1Display.ShaderPreset = 'Sphere'
isoVolume1Display.CustomTriangleScale = 3
isoVolume1Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
isoVolume1Display.Emissive = 0
isoVolume1Display.ScaleByArray = 0
isoVolume1Display.SetScaleArray = ['POINTS', 'Pressure']
isoVolume1Display.ScaleArrayComponent = ''
isoVolume1Display.UseScaleFunction = 1
isoVolume1Display.ScaleTransferFunction = 'PiecewiseFunction'
isoVolume1Display.OpacityByArray = 0
isoVolume1Display.OpacityArray = ['POINTS', 'Pressure']
isoVolume1Display.OpacityArrayComponent = ''
isoVolume1Display.OpacityTransferFunction = 'PiecewiseFunction'
isoVolume1Display.DataAxesGrid = 'GridAxesRepresentation'
isoVolume1Display.SelectionCellLabelBold = 0
isoVolume1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
isoVolume1Display.SelectionCellLabelFontFamily = 'Arial'
isoVolume1Display.SelectionCellLabelFontFile = ''
isoVolume1Display.SelectionCellLabelFontSize = 18
isoVolume1Display.SelectionCellLabelItalic = 0
isoVolume1Display.SelectionCellLabelJustification = 'Left'
isoVolume1Display.SelectionCellLabelOpacity = 1.0
isoVolume1Display.SelectionCellLabelShadow = 0
isoVolume1Display.SelectionPointLabelBold = 0
isoVolume1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
isoVolume1Display.SelectionPointLabelFontFamily = 'Arial'
isoVolume1Display.SelectionPointLabelFontFile = ''
isoVolume1Display.SelectionPointLabelFontSize = 18
isoVolume1Display.SelectionPointLabelItalic = 0
isoVolume1Display.SelectionPointLabelJustification = 'Left'
isoVolume1Display.SelectionPointLabelOpacity = 1.0
isoVolume1Display.SelectionPointLabelShadow = 0
isoVolume1Display.PolarAxes = 'PolarAxesRepresentation'
isoVolume1Display.ScalarOpacityFunction = pressurePWF
isoVolume1Display.ScalarOpacityUnitDistance = 13.113227421400477
isoVolume1Display.UseSeparateOpacityArray = 0
isoVolume1Display.OpacityArrayName = ['POINTS', 'Pressure']
isoVolume1Display.OpacityComponent = ''
isoVolume1Display.SelectMapper = 'Projected tetra'
isoVolume1Display.SamplingDimensions = [128, 128, 128]
isoVolume1Display.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'python/3.9
isoVolume1Display.GlyphType.TipRadius = 0.1
isoVolume1Display.GlyphType.TipLength = 0.35
isoVolume1Display.GlyphType.ShaftResolution = 6
isoVolume1Display.GlyphType.ShaftRadius = 0.03
isoVolume1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
isoVolume1Display.ScaleTransferFunction.Points = [-23.781307220458984, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
isoVolume1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
isoVolume1Display.OpacityTransferFunction.Points = [-23.781307220458984, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
isoVolume1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
isoVolume1Display.DataAxesGrid.XTitle = 'X Axis'
isoVolume1Display.DataAxesGrid.YTitle = 'Y Axis'
isoVolume1Display.DataAxesGrid.ZTitle = 'Z Axis'
isoVolume1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
isoVolume1Display.DataAxesGrid.XTitleFontFile = ''
isoVolume1Display.DataAxesGrid.XTitleBold = 0
isoVolume1Display.DataAxesGrid.XTitleItalic = 0
isoVolume1Display.DataAxesGrid.XTitleFontSize = 12
isoVolume1Display.DataAxesGrid.XTitleShadow = 0
isoVolume1Display.DataAxesGrid.XTitleOpacity = 1.0
isoVolume1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
isoVolume1Display.DataAxesGrid.YTitleFontFile = ''
isoVolume1Display.DataAxesGrid.YTitleBold = 0
isoVolume1Display.DataAxesGrid.YTitleItalic = 0
isoVolume1Display.DataAxesGrid.YTitleFontSize = 12
isoVolume1Display.DataAxesGrid.YTitleShadow = 0
isoVolume1Display.DataAxesGrid.YTitleOpacity = 1.0
isoVolume1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
isoVolume1Display.DataAxesGrid.ZTitleFontFile = ''
isoVolume1Display.DataAxesGrid.ZTitleBold = 0
isoVolume1Display.DataAxesGrid.ZTitleItalic = 0
isoVolume1Display.DataAxesGrid.ZTitleFontSize = 12
isoVolume1Display.DataAxesGrid.ZTitleShadow = 0
isoVolume1Display.DataAxesGrid.ZTitleOpacity = 1.0
isoVolume1Display.DataAxesGrid.FacesToRender = 63
isoVolume1Display.DataAxesGrid.CullBackface = 0
isoVolume1Display.DataAxesGrid.CullFrontface = 1
isoVolume1Display.DataAxesGrid.ShowGrid = 0
isoVolume1Display.DataAxesGrid.ShowEdges = 1
isoVolume1Display.DataAxesGrid.ShowTicks = 1
isoVolume1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
isoVolume1Display.DataAxesGrid.AxesToLabel = 63
isoVolume1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
isoVolume1Display.DataAxesGrid.XLabelFontFile = ''
isoVolume1Display.DataAxesGrid.XLabelBold = 0
isoVolume1Display.DataAxesGrid.XLabelItalic = 0
isoVolume1Display.DataAxesGrid.XLabelFontSize = 12
isoVolume1Display.DataAxesGrid.XLabelShadow = 0
isoVolume1Display.DataAxesGrid.XLabelOpacity = 1.0
isoVolume1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
isoVolume1Display.DataAxesGrid.YLabelFontFile = ''
isoVolume1Display.DataAxesGrid.YLabelBold = 0
isoVolume1Display.DataAxesGrid.YLabelItalic = 0
isoVolume1Display.DataAxesGrid.YLabelFontSize = 12
isoVolume1Display.DataAxesGrid.YLabelShadow = 0
isoVolume1Display.DataAxesGrid.YLabelOpacity = 1.0
isoVolume1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
isoVolume1Display.DataAxesGrid.ZLabelFontFile = ''
isoVolume1Display.DataAxesGrid.ZLabelBold = 0
isoVolume1Display.DataAxesGrid.ZLabelItalic = 0
isoVolume1Display.DataAxesGrid.ZLabelFontSize = 12
isoVolume1Display.DataAxesGrid.ZLabelShadow = 0
isoVolume1Display.DataAxesGrid.ZLabelOpacity = 1.0
isoVolume1Display.DataAxesGrid.XAxisNotation = 'Mixed'
isoVolume1Display.DataAxesGrid.XAxisPrecision = 2
isoVolume1Display.DataAxesGrid.XAxisUseCustomLabels = 0
isoVolume1Display.DataAxesGrid.XAxisLabels = []
isoVolume1Display.DataAxesGrid.YAxisNotation = 'Mixed'
isoVolume1Display.DataAxesGrid.YAxisPrecision = 2
isoVolume1Display.DataAxesGrid.YAxisUseCustomLabels = 0
isoVolume1Display.DataAxesGrid.YAxisLabels = []
isoVolume1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
isoVolume1Display.DataAxesGrid.ZAxisPrecision = 2
isoVolume1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
isoVolume1Display.DataAxesGrid.ZAxisLabels = []
isoVolume1Display.DataAxesGrid.UseCustomBounds = 0
isoVolume1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
isoVolume1Display.PolarAxes.Visibility = 0
isoVolume1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
isoVolume1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
isoVolume1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
isoVolume1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
isoVolume1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
isoVolume1Display.PolarAxes.EnableCustomRange = 0
isoVolume1Display.PolarAxes.CustomRange = [0.0, 1.0]
isoVolume1Display.PolarAxes.PolarAxisVisibility = 1
isoVolume1Display.PolarAxes.RadialAxesVisibility = 1
isoVolume1Display.PolarAxes.DrawRadialGridlines = 1
isoVolume1Display.PolarAxes.PolarArcsVisibility = 1
isoVolume1Display.PolarAxes.DrawPolarArcsGridlines = 1
isoVolume1Display.PolarAxes.NumberOfRadialAxes = 0
isoVolume1Display.PolarAxes.AutoSubdividePolarAxis = 1
isoVolume1Display.PolarAxes.NumberOfPolarAxis = 0
isoVolume1Display.PolarAxes.MinimumRadius = 0.0
isoVolume1Display.PolarAxes.MinimumAngle = 0.0
isoVolume1Display.PolarAxes.MaximumAngle = 90.0
isoVolume1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
isoVolume1Display.PolarAxes.Ratio = 1.0
isoVolume1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
isoVolume1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
isoVolume1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
isoVolume1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
isoVolume1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
isoVolume1Display.PolarAxes.PolarAxisTitleVisibility = 1
isoVolume1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
isoVolume1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
isoVolume1Display.PolarAxes.PolarLabelVisibility = 1
isoVolume1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
isoVolume1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
isoVolume1Display.PolarAxes.RadialLabelVisibility = 1
isoVolume1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
isoVolume1Display.PolarAxes.RadialLabelLocation = 'Bottom'
isoVolume1Display.PolarAxes.RadialUnitsVisibility = 1
isoVolume1Display.PolarAxes.ScreenSize = 10.0
isoVolume1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
isoVolume1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
isoVolume1Display.PolarAxes.PolarAxisTitleFontFile = ''
isoVolume1Display.PolarAxes.PolarAxisTitleBold = 0
isoVolume1Display.PolarAxes.PolarAxisTitleItalic = 0
isoVolume1Display.PolarAxes.PolarAxisTitleShadow = 0
isoVolume1Display.PolarAxes.PolarAxisTitleFontSize = 12
isoVolume1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
isoVolume1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
isoVolume1Display.PolarAxes.PolarAxisLabelFontFile = ''
isoVolume1Display.PolarAxes.PolarAxisLabelBold = 0
isoVolume1Display.PolarAxes.PolarAxisLabelItalic = 0
isoVolume1Display.PolarAxes.PolarAxisLabelShadow = 0
isoVolume1Display.PolarAxes.PolarAxisLabelFontSize = 12
isoVolume1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
isoVolume1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
isoVolume1Display.PolarAxes.LastRadialAxisTextFontFile = ''
isoVolume1Display.PolarAxes.LastRadialAxisTextBold = 0
isoVolume1Display.PolarAxes.LastRadialAxisTextItalic = 0
isoVolume1Display.PolarAxes.LastRadialAxisTextShadow = 0
isoVolume1Display.PolarAxes.LastRadialAxisTextFontSize = 12
isoVolume1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
isoVolume1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
isoVolume1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
isoVolume1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
isoVolume1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
isoVolume1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
isoVolume1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
isoVolume1Display.PolarAxes.EnableDistanceLOD = 1
isoVolume1Display.PolarAxes.DistanceLODThreshold = 0.7
isoVolume1Display.PolarAxes.EnableViewAngleLOD = 1
isoVolume1Display.PolarAxes.ViewAngleLODThreshold = 0.7
isoVolume1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
isoVolume1Display.PolarAxes.PolarTicksVisibility = 1
isoVolume1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
isoVolume1Display.PolarAxes.TickLocation = 'Both'
isoVolume1Display.PolarAxes.AxisTickVisibility = 1
isoVolume1Display.PolarAxes.AxisMinorTickVisibility = 0
isoVolume1Display.PolarAxes.ArcTickVisibility = 1
isoVolume1Display.PolarAxes.ArcMinorTickVisibility = 0
isoVolume1Display.PolarAxes.DeltaAngleMajor = 10.0
isoVolume1Display.PolarAxes.DeltaAngleMinor = 5.0
isoVolume1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
isoVolume1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
isoVolume1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
isoVolume1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
isoVolume1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
isoVolume1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
isoVolume1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
isoVolume1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
isoVolume1Display.PolarAxes.ArcMajorTickSize = 0.0
isoVolume1Display.PolarAxes.ArcTickRatioSize = 0.3
isoVolume1Display.PolarAxes.ArcMajorTickThickness = 1.0
isoVolume1Display.PolarAxes.ArcTickRatioThickness = 0.5
isoVolume1Display.PolarAxes.Use2DMode = 0
isoVolume1Display.PolarAxes.UseLogAxis = 0

# show color bar/color legend
isoVolume1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# turn off scalar coloring
ColorBy(isoVolume1Display, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pressureLUT, renderView1)

# change solid color
isoVolume1Display.AmbientColor = [1.0, 0.0, 1.0]
isoVolume1Display.DiffuseColor = [1.0, 0.0, 1.0]

# hide data in view
Hide(bodyFvtipvd, renderView1)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(3231, 1776)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [194.3658998500419, 749.5641884142361, 1475.1188301907046]
renderView1.CameraFocalPoint = [668.6891609697723, -30.493087062549947, 92.21519291352416]
renderView1.CameraViewUp = [0.1565966571699244, 0.8822625856573528, -0.44394843947513474]
renderView1.CameraParallelScale = 759.7911936302287

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
SaveScreenshot(f'test.png', renderView1, ImageResolution=[2815, 1542])