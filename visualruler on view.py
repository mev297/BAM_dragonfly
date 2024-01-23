from ORSModel import VisualRuler, orsVect
from OrsLibraries.workingcontext import WorkingContext
from ORSServiceClass.preferencesapplier.preferencesApplyManager import PreferencesApplyManager
currentView = WorkingContext.getCurrentView(None)
rectangle = currentView.getViewBoundedPlaneInWorldCoordinates()
ruler = VisualRuler()
#This is to apply the preference to the
PreferencesApplyManager.applyPreferencesOn(ruler)
ruler.addControlPoint(rectangle.getOrigin() , currentView.getCurrentTimeStep(),None)
ruler.addControlPoint(rectangle.getOriginOpposite() , currentView.getCurrentTimeStep(),None)
ruler.setTitle('aRuler')
ruler.publish()
print('ruler length:'+repr(ruler.getLength(currentView.getCurrentTimeStep(), None)))