from tvPORIS import *

class tv_physical(tvPORIS):
    dummy = "You should override the action triggers here"
    # Go to ARCGengIIIPORIS.py, navigate to the ##### Action triggers ##### section
    # which is normally at the bottom of the class, and copy here the methods 
    # to start overriding them, in order to convert the virtual device into a physical one
    # Once this class has any content, remove the dummy attribute


thismodel = tv_physical()

print("Let's test our model ",thismodel.name)
print("Current mode is ",thismodel.selectedMode.name)
thismodel.setMode(thismodel.mdTVMode_Antena)
print("Current mode is ",thismodel.selectedMode.name)
print("Current Canal is",thismodel.get_CanalDouble())
print("Current Canal Mode is",thismodel.get_CanalMode().name)
thismodel.set_CanalDouble(16)
print("Current Canal is",thismodel.get_CanalDouble())
thismodel.set_CanalDouble(99)
