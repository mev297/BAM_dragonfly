#First, we split the scene:

from OrsPythonPlugins.OrsLayoutManager.OrsLayoutManager import OrsLayoutManager
layout_manager = OrsLayoutManager()
layout_manager.setSceneLayout(2, vertical=False)
layout_manager.deletePlugin()

#Next, we will get the layout of scenes:

from OrsHelpers.layoutHelper import LayoutHelper
layout_of_scenes = LayoutHelper.getTopLayoutOfContext(None)

#Each scene can have it’s own layout. Each scene layout is in order from left to right, or top to bottom. If you have a horizontal layout of scenes and you want the left most scene, you would choose the 1st layout from the layout of scenes:

scene_layouts = layout_of_scenes.getAllChildLayout()
left_scene = scene_layouts[0]

#To get the views of a layout:

views = left_scene.getAllChildViews()

#To set one of the views to 3D:

from COMWrapper.ORS_def import CxvView_Mode
view = views[0]
view.setViewMode(CxvView_Mode.CXVVIEW_MODE_3D)

#To display an object in the layout, assuming that you have a Channel:

from OrsHelpers.datasethelper import DatasetHelper
DatasetHelper.setIsVisibleIn2D(channel, view, True)
DatasetHelper.fitToView(channel, view)

#To get the channels in the layout, you can ask each of the views, but generally, asking one of the views is fine:

from ORSModel import VisualChannel, Channel
visualChannels = view.getAllVisibleChildrenOfClass(VisualChannel.getClassNameStatic())
channels = [vc.getFirstParentOfClass(Channel.getClassNameStatic()) for vc in visualChannels]