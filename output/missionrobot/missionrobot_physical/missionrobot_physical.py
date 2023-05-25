from missionrobotPORIS import *

class missionrobot_physical(missionrobotPORIS):
    # Go to ARCGengIIIPORIS.py, navigate to the ##### Action triggers ##### section
    # which is normally at the bottom of the class, and copy here the methods 
    # to start overriding them, in order to convert the virtual device into a physical one
    # Once this class has any content, remove the pass clause

    pass

def calculateSpeed(vl):
    candidate = vl.getName().split('_')[1]
    if candidate == "":
        candidate = "-"+vl.getName().split('_')[2]

    return candidate


thismodel = missionrobot_physical()

print("Let's test our model ",thismodel.root.getName())
print("Current robot mode is ",thismodel.root.getSelectedMode().getName())
print("")
print("Setting the robot mode as active")
thismodel.set_MissionRobotMode(thismodel.mdMissionRobotMode_Active)
print("Current robot mode is ",thismodel.root.getSelectedMode().getName())
print("Current fragment is ",thismodel.get_PathMode().getName())
print("Current sensor decision is ",thismodel.get_DecisionMode().getName())
print("Current linefollower mode is ",thismodel.get_LineFollowerMode().getName())
vl = thismodel.get_LeftWheelSpeed()
print("Current left wheel speed is ",calculateSpeed(vl))
vl = thismodel.get_RightWheelSpeed()
print("Current right wheel speed is ",calculateSpeed(vl))
print("Current NextStep is ",thismodel.get_NextStepMode().getName())
print("")
print("Setting the sensor decision as WBW")
thismodel.set_DecisionMode(thismodel.mdDecisionMode_WBW_01)
print("Current linefollower mode is ",thismodel.get_LineFollowerMode().getName())
vl = thismodel.get_LeftWheelSpeed()
print("Current left wheel speed is ",calculateSpeed(vl))
vl = thismodel.get_RightWheelSpeed()
print("Current right wheel speed is ",calculateSpeed(vl))
print("Current NextStep is ",thismodel.get_NextStepMode().getName())
print("")
print("Setting the sensor decision as WBB")
thismodel.set_DecisionMode(thismodel.mdDecisionMode_WBB_01)
print("Current linefollower mode is ",thismodel.get_LineFollowerMode().getName())
vl = thismodel.get_LeftWheelSpeed()
print("Current left wheel speed is ",calculateSpeed(vl))
vl = thismodel.get_RightWheelSpeed()
print("Current right wheel speed is ",calculateSpeed(vl))
print("Current NextStep is ",thismodel.get_NextStepMode().getName())
