from controlboxPORIS import *

class controlbox_physical(controlboxPORIS):
    # Go to ARCGengIIIPORIS.py, navigate to the ##### Action triggers ##### section
    # which is normally at the bottom of the class, and copy here the methods 
    # to start overriding them, in order to convert the virtual device into a physical one
    # Once this class has any content, remove the pass clause

    pass


thismodel = controlbox_physical(12)

print("Let's test our model ",thismodel.getRoot().getName())
print("Current mode is ",thismodel.getRoot().getSelectedMode().getName())

