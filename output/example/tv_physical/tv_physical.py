from tvPORIS import *

class tv_physical(tvPORIS):
    dummy = "You should override the action triggers here"
    # Go to ARCGengIIIPORIS.py, navigate to the ##### Action triggers ##### section
    # which is normally at the bottom of the class, and copy here the methods 
    # to start overriding them, in order to convert the virtual device into a physical one
    # Once this class has any content, remove the dummy attribute


thismodel = tv_physical()

print("Let's test our model ",thismodel.root.name)
print("\nCurrent mode is ",thismodel.get_TVMode().name)
print("\nSetting mode Antena")
thismodel.root.setMode(thismodel.mdTVMode_Antena)
print("\nCurrent mode is ",thismodel.get_TVMode().name)
print("\nCurrent Canal is",thismodel.get_CanalDouble())
print("\nCurrent Canal Mode is",thismodel.get_CanalMode().name)
print("\nSetting canal 16")
thismodel.set_CanalDouble(16)
print("\nCurrent Canal is",thismodel.get_CanalDouble())
print("\nSetting canal 99")
thismodel.set_CanalDouble(99)
print("\nSetting Antena mode Digital")
thismodel.set_AntenaMode(thismodel.mdAntenaMode_Digital)
print("\nCurrent Canal Mode is",thismodel.get_CanalMode().name)
print("\nCurrent Canal is",thismodel.get_CanalDouble())
print("\nSetting canal 99")
thismodel.set_CanalDouble(99)
print("\nCurrent Canal Mode is",thismodel.get_CanalMode().name)
print("\nCurrent Canal is",thismodel.get_CanalDouble())
print("\nSetting Antena mode Analógico")
thismodel.set_AntenaMode(thismodel.mdAntenaMode_Analogico)
print("\nCurrent Canal Mode is",thismodel.get_CanalMode().name)
print("\nCurrent Canal is",thismodel.get_CanalDouble())
