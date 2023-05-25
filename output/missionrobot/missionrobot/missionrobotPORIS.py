from PORIS import *

class missionrobotPORIS:
    def __init__(self):
        idcounter = 1
        self.sysMissionRobot = PORISSys("MissionRobot")
        self.mdMissionRobotMode_UNKNOWN = PORISMode("MissionRobotMode_UNKNOWN")
        self.root = self.sysMissionRobot
        self.sysPath = PORISSys("Path")
        self.mdPathMode_UNKNOWN = PORISMode("PathMode_UNKNOWN")
        self.sysDecision = PORISSys("Decision")
        self.mdDecisionMode_UNKNOWN = PORISMode("DecisionMode_UNKNOWN")
        self.sysLineFollower = PORISSys("LineFollower")
        self.mdLineFollowerMode_UNKNOWN = PORISMode("LineFollowerMode_UNKNOWN")
        self.sysMobility = PORISSys("Mobility")
        self.mdMobilityMode_UNKNOWN = PORISMode("MobilityMode_UNKNOWN")
        self.prRightWheelSpeed = PORISParam("RightWheelSpeed")
        self.mdRightWheelSpeedMode_UNKNOWN = PORISMode("RightWheelSpeedMode_UNKNOWN")
        self.vlRightWheelSpeed_UNKNOWN = PORISValue("RightWheelSpeed_UNKNOWN")
        self.prLeftWheelSpeed = PORISParam("LeftWheelSpeed")
        self.mdLeftWheelSpeedMode_UNKNOWN = PORISMode("LeftWheelSpeedMode_UNKNOWN")
        self.vlLeftWheelSpeed_UNKNOWN = PORISValue("LeftWheelSpeed_UNKNOWN")
        self.sysNextStep = PORISSys("NextStep")
        self.mdNextStepMode_UNKNOWN = PORISMode("NextStepMode_UNKNOWN")
        self.mdPathMode_01_fragment = PORISMode("PathMode_01_fragment")
        self.mdPathMode_03_fragment = PORISMode("PathMode_03_fragment")
        self.mdPathMode_00_stop = PORISMode("PathMode_00_stop")
        self.mdMissionRobotMode_Inactive = PORISMode("MissionRobotMode_Inactive")
        self.mdMissionRobotMode_Active = PORISMode("MissionRobotMode_Active")
        self.mdDecisionMode_BBB_00 = PORISMode("DecisionMode_BBB_00")
        self.mdDecisionMode_BBB_01 = PORISMode("DecisionMode_BBB_01")
        self.mdDecisionMode_BBB_03 = PORISMode("DecisionMode_BBB_03")
        self.mdDecisionMode_BBW_00 = PORISMode("DecisionMode_BBW_00")
        self.mdDecisionMode_BBW_01 = PORISMode("DecisionMode_BBW_01")
        self.mdDecisionMode_BBW_03 = PORISMode("DecisionMode_BBW_03")
        self.mdDecisionMode_BWB_00 = PORISMode("DecisionMode_BWB_00")
        self.mdDecisionMode_BWB_01 = PORISMode("DecisionMode_BWB_01")
        self.mdDecisionMode_BWB_03 = PORISMode("DecisionMode_BWB_03")
        self.mdDecisionMode_BWW_00 = PORISMode("DecisionMode_BWW_00")
        self.mdDecisionMode_BWW_01 = PORISMode("DecisionMode_BWW_01")
        self.mdDecisionMode_BWW_03 = PORISMode("DecisionMode_BWW_03")
        self.mdDecisionMode_WBB_00 = PORISMode("DecisionMode_WBB_00")
        self.mdDecisionMode_WBB_01 = PORISMode("DecisionMode_WBB_01")
        self.mdDecisionMode_WBB_03 = PORISMode("DecisionMode_WBB_03")
        self.mdDecisionMode_WBW_00 = PORISMode("DecisionMode_WBW_00")
        self.mdDecisionMode_WBW_01 = PORISMode("DecisionMode_WBW_01")
        self.mdDecisionMode_WBW_03 = PORISMode("DecisionMode_WBW_03")
        self.mdDecisionMode_WWB_00 = PORISMode("DecisionMode_WWB_00")
        self.mdDecisionMode_WWB_01 = PORISMode("DecisionMode_WWB_01")
        self.mdDecisionMode_WWB_03 = PORISMode("DecisionMode_WWB_03")
        self.mdDecisionMode_WWW_00 = PORISMode("DecisionMode_WWW_00")
        self.mdDecisionMode_WWW_01 = PORISMode("DecisionMode_WWW_01")
        self.mdDecisionMode_WWW_03 = PORISMode("DecisionMode_WWW_03")
        self.mdLineFollowerMode_WBW = PORISMode("LineFollowerMode_WBW")
        self.mdRightWheelSpeedMode_Stop = PORISMode("RightWheelSpeedMode_Stop")
        self.mdRightWheelSpeedMode_Forward = PORISMode("RightWheelSpeedMode_Forward")
        self.mdRightWheelSpeedMode_Back = PORISMode("RightWheelSpeedMode_Back")
        self.vlRightWheelSpeed_0 = PORISValue("RightWheelSpeed_0")
        self.vlRightWheelSpeed_10 = PORISValue("RightWheelSpeed_10")
        self.vlRightWheelSpeed__10 = PORISValue("RightWheelSpeed__10")
        self.mdLeftWheelSpeedMode_Stop = PORISMode("LeftWheelSpeedMode_Stop")
        self.mdLeftWheelSpeedMode_Forward = PORISMode("LeftWheelSpeedMode_Forward")
        self.mdLeftWheelSpeedMode_Back = PORISMode("LeftWheelSpeedMode_Back")
        self.vlLeftWheelSpeed_0 = PORISValue("LeftWheelSpeed_0")
        self.vlLeftWheelSpeed_10 = PORISValue("LeftWheelSpeed_10")
        self.vlLeftWheelSpeed__10 = PORISValue("LeftWheelSpeed__10")
        self.mdMobilityMode_Forward = PORISMode("MobilityMode_Forward")
        self.mdMobilityMode_TurnRight = PORISMode("MobilityMode_TurnRight")
        self.mdMobilityMode_TurnLeft = PORISMode("MobilityMode_TurnLeft")
        self.mdMobilityMode_Stop = PORISMode("MobilityMode_Stop")
        self.mdMobilityMode_SoftLeft = PORISMode("MobilityMode_SoftLeft")
        self.mdMobilityMode_SoftRight = PORISMode("MobilityMode_SoftRight")
        self.mdNextStepMode_Yes = PORISMode("NextStepMode_Yes")
        self.mdMissionRobotMode_Engineering = PORISMode("MissionRobotMode_Engineering")
        self.mdPathMode_Engineering = PORISMode("PathMode_Engineering")
        self.mdDecisionMode_Engineering = PORISMode("DecisionMode_Engineering")
        self.mdMobilityMode_Engineering = PORISMode("MobilityMode_Engineering")

        self.sysMissionRobot.id = idcounter
        idcounter += 1
        self.sysMissionRobot.ident = "MissionRobot"
        self.sysMissionRobot.description = ""

        self.mdMissionRobotMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdMissionRobotMode_UNKNOWN.ident = "MissionRobotMode_UNKNOWN"
        self.mdMissionRobotMode_UNKNOWN.description = ""
        self.sysMissionRobot.addMode(self.mdMissionRobotMode_UNKNOWN)

        self.sysPath.id = idcounter
        idcounter += 1
        self.sysPath.ident = "Path"
        self.sysPath.description = ""
        self.sysMissionRobot.addSubsystem(self.sysPath)

        self.mdPathMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdPathMode_UNKNOWN.ident = "PathMode_UNKNOWN"
        self.mdPathMode_UNKNOWN.description = ""
        self.sysPath.addMode(self.mdPathMode_UNKNOWN)

        self.sysDecision.id = idcounter
        idcounter += 1
        self.sysDecision.ident = "Decision"
        self.sysDecision.description = ""
        self.sysPath.addSubsystem(self.sysDecision)

        self.mdDecisionMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdDecisionMode_UNKNOWN.ident = "DecisionMode_UNKNOWN"
        self.mdDecisionMode_UNKNOWN.description = ""
        self.sysDecision.addMode(self.mdDecisionMode_UNKNOWN)

        self.sysLineFollower.id = idcounter
        idcounter += 1
        self.sysLineFollower.ident = "LineFollower"
        self.sysLineFollower.description = ""
        self.sysDecision.addSubsystem(self.sysLineFollower)

        self.mdLineFollowerMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdLineFollowerMode_UNKNOWN.ident = "LineFollowerMode_UNKNOWN"
        self.mdLineFollowerMode_UNKNOWN.description = ""
        self.sysLineFollower.addMode(self.mdLineFollowerMode_UNKNOWN)

        self.sysMobility.id = idcounter
        idcounter += 1
        self.sysMobility.ident = "Mobility"
        self.sysMobility.description = ""
        self.sysDecision.addSubsystem(self.sysMobility)

        self.mdMobilityMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdMobilityMode_UNKNOWN.ident = "MobilityMode_UNKNOWN"
        self.mdMobilityMode_UNKNOWN.description = ""
        self.sysMobility.addMode(self.mdMobilityMode_UNKNOWN)

        self.prRightWheelSpeed.id = idcounter
        idcounter += 1
        self.prRightWheelSpeed.ident = "RightWheelSpeed"
        self.prRightWheelSpeed.description = ""
        self.sysMobility.addParam(self.prRightWheelSpeed)

        self.vlRightWheelSpeed_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlRightWheelSpeed_UNKNOWN.ident = "RightWheelSpeed_UNKNOWN"
        self.vlRightWheelSpeed_UNKNOWN.description = "Unknown value for RightWheelSpeed"
        self.prRightWheelSpeed.addValue(self.vlRightWheelSpeed_UNKNOWN)

        self.mdRightWheelSpeedMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdRightWheelSpeedMode_UNKNOWN.ident = "RightWheelSpeedMode_UNKNOWN"
        self.mdRightWheelSpeedMode_UNKNOWN.description = "Unknown mode for RightWheelSpeed"
        self.prRightWheelSpeed.addMode(self.mdRightWheelSpeedMode_UNKNOWN)
        self.mdRightWheelSpeedMode_UNKNOWN.addValue(self.vlRightWheelSpeed_UNKNOWN)
        self.mdMobilityMode_UNKNOWN.addSubMode(self.mdRightWheelSpeedMode_UNKNOWN)

        self.prLeftWheelSpeed.id = idcounter
        idcounter += 1
        self.prLeftWheelSpeed.ident = "LeftWheelSpeed"
        self.prLeftWheelSpeed.description = ""
        self.sysMobility.addParam(self.prLeftWheelSpeed)

        self.vlLeftWheelSpeed_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlLeftWheelSpeed_UNKNOWN.ident = "LeftWheelSpeed_UNKNOWN"
        self.vlLeftWheelSpeed_UNKNOWN.description = "Unknown value for LeftWheelSpeed"
        self.prLeftWheelSpeed.addValue(self.vlLeftWheelSpeed_UNKNOWN)

        self.mdLeftWheelSpeedMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdLeftWheelSpeedMode_UNKNOWN.ident = "LeftWheelSpeedMode_UNKNOWN"
        self.mdLeftWheelSpeedMode_UNKNOWN.description = "Unknown mode for LeftWheelSpeed"
        self.prLeftWheelSpeed.addMode(self.mdLeftWheelSpeedMode_UNKNOWN)
        self.mdLeftWheelSpeedMode_UNKNOWN.addValue(self.vlLeftWheelSpeed_UNKNOWN)
        self.mdMobilityMode_UNKNOWN.addSubMode(self.mdLeftWheelSpeedMode_UNKNOWN)

        self.sysNextStep.id = idcounter
        idcounter += 1
        self.sysNextStep.ident = "NextStep"
        self.sysNextStep.description = ""
        self.sysDecision.addSubsystem(self.sysNextStep)

        self.mdNextStepMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdNextStepMode_UNKNOWN.ident = "NextStepMode_UNKNOWN"
        self.mdNextStepMode_UNKNOWN.description = ""
        self.sysNextStep.addMode(self.mdNextStepMode_UNKNOWN)

        self.mdPathMode_01_fragment.id = idcounter
        idcounter += 1
        self.mdPathMode_01_fragment.ident = "PathMode_01_fragment"
        self.mdPathMode_01_fragment.description = ""
        self.sysPath.addMode(self.mdPathMode_01_fragment)

        self.mdPathMode_03_fragment.id = idcounter
        idcounter += 1
        self.mdPathMode_03_fragment.ident = "PathMode_03_fragment"
        self.mdPathMode_03_fragment.description = ""
        self.sysPath.addMode(self.mdPathMode_03_fragment)

        self.mdPathMode_00_stop.id = idcounter
        idcounter += 1
        self.mdPathMode_00_stop.ident = "PathMode_00_stop"
        self.mdPathMode_00_stop.description = ""
        self.sysPath.addMode(self.mdPathMode_00_stop)

        self.mdMissionRobotMode_Inactive.id = idcounter
        idcounter += 1
        self.mdMissionRobotMode_Inactive.ident = "MissionRobotMode_Inactive"
        self.mdMissionRobotMode_Inactive.description = ""
        self.sysMissionRobot.addMode(self.mdMissionRobotMode_Inactive)

        self.mdMissionRobotMode_Active.id = idcounter
        idcounter += 1
        self.mdMissionRobotMode_Active.ident = "MissionRobotMode_Active"
        self.mdMissionRobotMode_Active.description = ""
        self.sysMissionRobot.addMode(self.mdMissionRobotMode_Active)

        self.mdDecisionMode_BBB_00.id = idcounter
        idcounter += 1
        self.mdDecisionMode_BBB_00.ident = "DecisionMode_BBB_00"
        self.mdDecisionMode_BBB_00.description = ""
        self.sysDecision.addMode(self.mdDecisionMode_BBB_00)

        self.mdDecisionMode_BBB_01.id = idcounter
        idcounter += 1
        self.mdDecisionMode_BBB_01.ident = "DecisionMode_BBB_01"
        self.mdDecisionMode_BBB_01.description = ""
        self.sysDecision.addMode(self.mdDecisionMode_BBB_01)

        self.mdDecisionMode_BBB_03.id = idcounter
        idcounter += 1
        self.mdDecisionMode_BBB_03.ident = "DecisionMode_BBB_03"
        self.mdDecisionMode_BBB_03.description = ""
        self.sysDecision.addMode(self.mdDecisionMode_BBB_03)

        self.mdDecisionMode_BBW_00.id = idcounter
        idcounter += 1
        self.mdDecisionMode_BBW_00.ident = "DecisionMode_BBW_00"
        self.mdDecisionMode_BBW_00.description = ""
        self.sysDecision.addMode(self.mdDecisionMode_BBW_00)

        self.mdDecisionMode_BBW_01.id = idcounter
        idcounter += 1
        self.mdDecisionMode_BBW_01.ident = "DecisionMode_BBW_01"
        self.mdDecisionMode_BBW_01.description = ""
        self.sysDecision.addMode(self.mdDecisionMode_BBW_01)

        self.mdDecisionMode_BBW_03.id = idcounter
        idcounter += 1
        self.mdDecisionMode_BBW_03.ident = "DecisionMode_BBW_03"
        self.mdDecisionMode_BBW_03.description = ""
        self.sysDecision.addMode(self.mdDecisionMode_BBW_03)

        self.mdDecisionMode_BWB_00.id = idcounter
        idcounter += 1
        self.mdDecisionMode_BWB_00.ident = "DecisionMode_BWB_00"
        self.mdDecisionMode_BWB_00.description = ""
        self.sysDecision.addMode(self.mdDecisionMode_BWB_00)

        self.mdDecisionMode_BWB_01.id = idcounter
        idcounter += 1
        self.mdDecisionMode_BWB_01.ident = "DecisionMode_BWB_01"
        self.mdDecisionMode_BWB_01.description = ""
        self.sysDecision.addMode(self.mdDecisionMode_BWB_01)

        self.mdDecisionMode_BWB_03.id = idcounter
        idcounter += 1
        self.mdDecisionMode_BWB_03.ident = "DecisionMode_BWB_03"
        self.mdDecisionMode_BWB_03.description = ""
        self.sysDecision.addMode(self.mdDecisionMode_BWB_03)

        self.mdDecisionMode_BWW_00.id = idcounter
        idcounter += 1
        self.mdDecisionMode_BWW_00.ident = "DecisionMode_BWW_00"
        self.mdDecisionMode_BWW_00.description = ""
        self.sysDecision.addMode(self.mdDecisionMode_BWW_00)

        self.mdDecisionMode_BWW_01.id = idcounter
        idcounter += 1
        self.mdDecisionMode_BWW_01.ident = "DecisionMode_BWW_01"
        self.mdDecisionMode_BWW_01.description = ""
        self.sysDecision.addMode(self.mdDecisionMode_BWW_01)

        self.mdDecisionMode_BWW_03.id = idcounter
        idcounter += 1
        self.mdDecisionMode_BWW_03.ident = "DecisionMode_BWW_03"
        self.mdDecisionMode_BWW_03.description = ""
        self.sysDecision.addMode(self.mdDecisionMode_BWW_03)

        self.mdDecisionMode_WBB_00.id = idcounter
        idcounter += 1
        self.mdDecisionMode_WBB_00.ident = "DecisionMode_WBB_00"
        self.mdDecisionMode_WBB_00.description = ""
        self.sysDecision.addMode(self.mdDecisionMode_WBB_00)

        self.mdDecisionMode_WBB_01.id = idcounter
        idcounter += 1
        self.mdDecisionMode_WBB_01.ident = "DecisionMode_WBB_01"
        self.mdDecisionMode_WBB_01.description = ""
        self.sysDecision.addMode(self.mdDecisionMode_WBB_01)

        self.mdDecisionMode_WBB_03.id = idcounter
        idcounter += 1
        self.mdDecisionMode_WBB_03.ident = "DecisionMode_WBB_03"
        self.mdDecisionMode_WBB_03.description = ""
        self.sysDecision.addMode(self.mdDecisionMode_WBB_03)

        self.mdDecisionMode_WBW_00.id = idcounter
        idcounter += 1
        self.mdDecisionMode_WBW_00.ident = "DecisionMode_WBW_00"
        self.mdDecisionMode_WBW_00.description = ""
        self.sysDecision.addMode(self.mdDecisionMode_WBW_00)

        self.mdDecisionMode_WBW_01.id = idcounter
        idcounter += 1
        self.mdDecisionMode_WBW_01.ident = "DecisionMode_WBW_01"
        self.mdDecisionMode_WBW_01.description = ""
        self.sysDecision.addMode(self.mdDecisionMode_WBW_01)

        self.mdDecisionMode_WBW_03.id = idcounter
        idcounter += 1
        self.mdDecisionMode_WBW_03.ident = "DecisionMode_WBW_03"
        self.mdDecisionMode_WBW_03.description = ""
        self.sysDecision.addMode(self.mdDecisionMode_WBW_03)

        self.mdDecisionMode_WWB_00.id = idcounter
        idcounter += 1
        self.mdDecisionMode_WWB_00.ident = "DecisionMode_WWB_00"
        self.mdDecisionMode_WWB_00.description = ""
        self.sysDecision.addMode(self.mdDecisionMode_WWB_00)

        self.mdDecisionMode_WWB_01.id = idcounter
        idcounter += 1
        self.mdDecisionMode_WWB_01.ident = "DecisionMode_WWB_01"
        self.mdDecisionMode_WWB_01.description = ""
        self.sysDecision.addMode(self.mdDecisionMode_WWB_01)

        self.mdDecisionMode_WWB_03.id = idcounter
        idcounter += 1
        self.mdDecisionMode_WWB_03.ident = "DecisionMode_WWB_03"
        self.mdDecisionMode_WWB_03.description = ""
        self.sysDecision.addMode(self.mdDecisionMode_WWB_03)

        self.mdDecisionMode_WWW_00.id = idcounter
        idcounter += 1
        self.mdDecisionMode_WWW_00.ident = "DecisionMode_WWW_00"
        self.mdDecisionMode_WWW_00.description = ""
        self.sysDecision.addMode(self.mdDecisionMode_WWW_00)

        self.mdDecisionMode_WWW_01.id = idcounter
        idcounter += 1
        self.mdDecisionMode_WWW_01.ident = "DecisionMode_WWW_01"
        self.mdDecisionMode_WWW_01.description = ""
        self.sysDecision.addMode(self.mdDecisionMode_WWW_01)

        self.mdDecisionMode_WWW_03.id = idcounter
        idcounter += 1
        self.mdDecisionMode_WWW_03.ident = "DecisionMode_WWW_03"
        self.mdDecisionMode_WWW_03.description = ""
        self.sysDecision.addMode(self.mdDecisionMode_WWW_03)

        self.mdLineFollowerMode_WBW.id = idcounter
        idcounter += 1
        self.mdLineFollowerMode_WBW.ident = "LineFollowerMode_WBW"
        self.mdLineFollowerMode_WBW.description = ""
        self.sysLineFollower.addMode(self.mdLineFollowerMode_WBW)

        self.mdRightWheelSpeedMode_Stop.id = idcounter
        idcounter += 1
        self.mdRightWheelSpeedMode_Stop.ident = "RightWheelSpeedMode_Stop"
        self.mdRightWheelSpeedMode_Stop.description = ""
        self.prRightWheelSpeed.addMode(self.mdRightWheelSpeedMode_Stop)

        self.mdRightWheelSpeedMode_Forward.id = idcounter
        idcounter += 1
        self.mdRightWheelSpeedMode_Forward.ident = "RightWheelSpeedMode_Forward"
        self.mdRightWheelSpeedMode_Forward.description = ""
        self.prRightWheelSpeed.addMode(self.mdRightWheelSpeedMode_Forward)

        self.mdRightWheelSpeedMode_Back.id = idcounter
        idcounter += 1
        self.mdRightWheelSpeedMode_Back.ident = "RightWheelSpeedMode_Back"
        self.mdRightWheelSpeedMode_Back.description = ""
        self.prRightWheelSpeed.addMode(self.mdRightWheelSpeedMode_Back)

        self.vlRightWheelSpeed_0.id = idcounter
        idcounter += 1
        self.vlRightWheelSpeed_0.ident = "RightWheelSpeed_0"
        self.vlRightWheelSpeed_0.description = ""
        self.prRightWheelSpeed.addValue(self.vlRightWheelSpeed_0)

        self.vlRightWheelSpeed_10.id = idcounter
        idcounter += 1
        self.vlRightWheelSpeed_10.ident = "RightWheelSpeed_10"
        self.vlRightWheelSpeed_10.description = ""
        self.prRightWheelSpeed.addValue(self.vlRightWheelSpeed_10)

        self.vlRightWheelSpeed__10.id = idcounter
        idcounter += 1
        self.vlRightWheelSpeed__10.ident = "RightWheelSpeed__10"
        self.vlRightWheelSpeed__10.description = ""
        self.prRightWheelSpeed.addValue(self.vlRightWheelSpeed__10)

        self.mdLeftWheelSpeedMode_Stop.id = idcounter
        idcounter += 1
        self.mdLeftWheelSpeedMode_Stop.ident = "LeftWheelSpeedMode_Stop"
        self.mdLeftWheelSpeedMode_Stop.description = ""
        self.prLeftWheelSpeed.addMode(self.mdLeftWheelSpeedMode_Stop)

        self.mdLeftWheelSpeedMode_Forward.id = idcounter
        idcounter += 1
        self.mdLeftWheelSpeedMode_Forward.ident = "LeftWheelSpeedMode_Forward"
        self.mdLeftWheelSpeedMode_Forward.description = ""
        self.prLeftWheelSpeed.addMode(self.mdLeftWheelSpeedMode_Forward)

        self.mdLeftWheelSpeedMode_Back.id = idcounter
        idcounter += 1
        self.mdLeftWheelSpeedMode_Back.ident = "LeftWheelSpeedMode_Back"
        self.mdLeftWheelSpeedMode_Back.description = ""
        self.prLeftWheelSpeed.addMode(self.mdLeftWheelSpeedMode_Back)

        self.vlLeftWheelSpeed_0.id = idcounter
        idcounter += 1
        self.vlLeftWheelSpeed_0.ident = "LeftWheelSpeed_0"
        self.vlLeftWheelSpeed_0.description = ""
        self.prLeftWheelSpeed.addValue(self.vlLeftWheelSpeed_0)

        self.vlLeftWheelSpeed_10.id = idcounter
        idcounter += 1
        self.vlLeftWheelSpeed_10.ident = "LeftWheelSpeed_10"
        self.vlLeftWheelSpeed_10.description = ""
        self.prLeftWheelSpeed.addValue(self.vlLeftWheelSpeed_10)

        self.vlLeftWheelSpeed__10.id = idcounter
        idcounter += 1
        self.vlLeftWheelSpeed__10.ident = "LeftWheelSpeed__10"
        self.vlLeftWheelSpeed__10.description = ""
        self.prLeftWheelSpeed.addValue(self.vlLeftWheelSpeed__10)

        self.mdMobilityMode_Forward.id = idcounter
        idcounter += 1
        self.mdMobilityMode_Forward.ident = "MobilityMode_Forward"
        self.mdMobilityMode_Forward.description = ""
        self.sysMobility.addMode(self.mdMobilityMode_Forward)

        self.mdMobilityMode_TurnRight.id = idcounter
        idcounter += 1
        self.mdMobilityMode_TurnRight.ident = "MobilityMode_TurnRight"
        self.mdMobilityMode_TurnRight.description = ""
        self.sysMobility.addMode(self.mdMobilityMode_TurnRight)

        self.mdMobilityMode_TurnLeft.id = idcounter
        idcounter += 1
        self.mdMobilityMode_TurnLeft.ident = "MobilityMode_TurnLeft"
        self.mdMobilityMode_TurnLeft.description = ""
        self.sysMobility.addMode(self.mdMobilityMode_TurnLeft)

        self.mdMobilityMode_Stop.id = idcounter
        idcounter += 1
        self.mdMobilityMode_Stop.ident = "MobilityMode_Stop"
        self.mdMobilityMode_Stop.description = ""
        self.sysMobility.addMode(self.mdMobilityMode_Stop)

        self.mdMobilityMode_SoftLeft.id = idcounter
        idcounter += 1
        self.mdMobilityMode_SoftLeft.ident = "MobilityMode_SoftLeft"
        self.mdMobilityMode_SoftLeft.description = ""
        self.sysMobility.addMode(self.mdMobilityMode_SoftLeft)

        self.mdMobilityMode_SoftRight.id = idcounter
        idcounter += 1
        self.mdMobilityMode_SoftRight.ident = "MobilityMode_SoftRight"
        self.mdMobilityMode_SoftRight.description = ""
        self.sysMobility.addMode(self.mdMobilityMode_SoftRight)

        self.mdNextStepMode_Yes.id = idcounter
        idcounter += 1
        self.mdNextStepMode_Yes.ident = "NextStepMode_Yes"
        self.mdNextStepMode_Yes.description = ""
        self.sysNextStep.addMode(self.mdNextStepMode_Yes)

        self.mdMissionRobotMode_Engineering.id = idcounter
        idcounter += 1
        self.mdMissionRobotMode_Engineering.ident = "MissionRobotMode_Engineering"
        self.mdMissionRobotMode_Engineering.description = "MissionRobot engineering mode"
        self.sysMissionRobot.addMode(self.mdMissionRobotMode_Engineering)

        self.mdPathMode_Engineering.id = idcounter
        idcounter += 1
        self.mdPathMode_Engineering.ident = "PathMode_Engineering"
        self.mdPathMode_Engineering.description = "Path engineering mode"
        self.sysPath.addMode(self.mdPathMode_Engineering)

        self.mdDecisionMode_Engineering.id = idcounter
        idcounter += 1
        self.mdDecisionMode_Engineering.ident = "DecisionMode_Engineering"
        self.mdDecisionMode_Engineering.description = "Decision engineering mode"
        self.sysDecision.addMode(self.mdDecisionMode_Engineering)

        self.mdMobilityMode_Engineering.id = idcounter
        idcounter += 1
        self.mdMobilityMode_Engineering.ident = "MobilityMode_Engineering"
        self.mdMobilityMode_Engineering.description = "Mobility engineering mode"
        self.sysMobility.addMode(self.mdMobilityMode_Engineering)
        # Marcamos PathMode_00_stop como elegible para MissionRobotMode_Inactive
        self.mdMissionRobotMode_Inactive.addSubMode(self.mdPathMode_00_stop)
        # Marcamos PathMode_01_fragment como elegible para MissionRobotMode_Active
        self.mdMissionRobotMode_Active.addSubMode(self.mdPathMode_01_fragment)
        # Marcamos PathMode_03_fragment como elegible para MissionRobotMode_Active
        self.mdMissionRobotMode_Active.addSubMode(self.mdPathMode_03_fragment)
        # Marcamos PathMode_01_fragment como elegible para MissionRobotMode_Engineering
        self.mdMissionRobotMode_Engineering.addSubMode(self.mdPathMode_01_fragment)
        # Marcamos PathMode_03_fragment como elegible para MissionRobotMode_Engineering
        self.mdMissionRobotMode_Engineering.addSubMode(self.mdPathMode_03_fragment)
        # Marcamos PathMode_00_stop como elegible para MissionRobotMode_Engineering
        self.mdMissionRobotMode_Engineering.addSubMode(self.mdPathMode_00_stop)
        # Marcamos PathMode_Engineering como elegible para MissionRobotMode_Engineering
        self.mdMissionRobotMode_Engineering.addSubMode(self.mdPathMode_Engineering)
        # Marcamos DecisionMode_WWW_01 como elegible para PathMode_01_fragment
        self.mdPathMode_01_fragment.addSubMode(self.mdDecisionMode_WWW_01)
        # Marcamos DecisionMode_WWB_01 como elegible para PathMode_01_fragment
        self.mdPathMode_01_fragment.addSubMode(self.mdDecisionMode_WWB_01)
        # Marcamos DecisionMode_WBW_01 como elegible para PathMode_01_fragment
        self.mdPathMode_01_fragment.addSubMode(self.mdDecisionMode_WBW_01)
        # Marcamos DecisionMode_WBB_01 como elegible para PathMode_01_fragment
        self.mdPathMode_01_fragment.addSubMode(self.mdDecisionMode_WBB_01)
        # Marcamos DecisionMode_BWW_01 como elegible para PathMode_01_fragment
        self.mdPathMode_01_fragment.addSubMode(self.mdDecisionMode_BWW_01)
        # Marcamos DecisionMode_BWB_01 como elegible para PathMode_01_fragment
        self.mdPathMode_01_fragment.addSubMode(self.mdDecisionMode_BWB_01)
        # Marcamos DecisionMode_BBW_01 como elegible para PathMode_01_fragment
        self.mdPathMode_01_fragment.addSubMode(self.mdDecisionMode_BBW_01)
        # Marcamos DecisionMode_BBB_01 como elegible para PathMode_01_fragment
        self.mdPathMode_01_fragment.addSubMode(self.mdDecisionMode_BBB_01)
        # Marcamos DecisionMode_WWW_03 como elegible para PathMode_03_fragment
        self.mdPathMode_03_fragment.addSubMode(self.mdDecisionMode_WWW_03)
        # Marcamos DecisionMode_WWB_03 como elegible para PathMode_03_fragment
        self.mdPathMode_03_fragment.addSubMode(self.mdDecisionMode_WWB_03)
        # Marcamos DecisionMode_WBW_03 como elegible para PathMode_03_fragment
        self.mdPathMode_03_fragment.addSubMode(self.mdDecisionMode_WBW_03)
        # Marcamos DecisionMode_WBB_03 como elegible para PathMode_03_fragment
        self.mdPathMode_03_fragment.addSubMode(self.mdDecisionMode_WBB_03)
        # Marcamos DecisionMode_BWW_03 como elegible para PathMode_03_fragment
        self.mdPathMode_03_fragment.addSubMode(self.mdDecisionMode_BWW_03)
        # Marcamos DecisionMode_BWB_03 como elegible para PathMode_03_fragment
        self.mdPathMode_03_fragment.addSubMode(self.mdDecisionMode_BWB_03)
        # Marcamos DecisionMode_BBW_03 como elegible para PathMode_03_fragment
        self.mdPathMode_03_fragment.addSubMode(self.mdDecisionMode_BBW_03)
        # Marcamos DecisionMode_BBB_03 como elegible para PathMode_03_fragment
        self.mdPathMode_03_fragment.addSubMode(self.mdDecisionMode_BBB_03)
        # Marcamos DecisionMode_WWW_00 como elegible para PathMode_00_stop
        self.mdPathMode_00_stop.addSubMode(self.mdDecisionMode_WWW_00)
        # Marcamos DecisionMode_WWB_00 como elegible para PathMode_00_stop
        self.mdPathMode_00_stop.addSubMode(self.mdDecisionMode_WWB_00)
        # Marcamos DecisionMode_WBW_00 como elegible para PathMode_00_stop
        self.mdPathMode_00_stop.addSubMode(self.mdDecisionMode_WBW_00)
        # Marcamos DecisionMode_WBB_00 como elegible para PathMode_00_stop
        self.mdPathMode_00_stop.addSubMode(self.mdDecisionMode_WBB_00)
        # Marcamos DecisionMode_BWW_00 como elegible para PathMode_00_stop
        self.mdPathMode_00_stop.addSubMode(self.mdDecisionMode_BWW_00)
        # Marcamos DecisionMode_BWB_00 como elegible para PathMode_00_stop
        self.mdPathMode_00_stop.addSubMode(self.mdDecisionMode_BWB_00)
        # Marcamos DecisionMode_BBW_00 como elegible para PathMode_00_stop
        self.mdPathMode_00_stop.addSubMode(self.mdDecisionMode_BBW_00)
        # Marcamos DecisionMode_BBB_00 como elegible para PathMode_00_stop
        self.mdPathMode_00_stop.addSubMode(self.mdDecisionMode_BBB_00)
        # Marcamos DecisionMode_BBB_00 como elegible para PathMode_Engineering
        self.mdPathMode_Engineering.addSubMode(self.mdDecisionMode_BBB_00)
        # Marcamos DecisionMode_BBB_01 como elegible para PathMode_Engineering
        self.mdPathMode_Engineering.addSubMode(self.mdDecisionMode_BBB_01)
        # Marcamos DecisionMode_BBB_03 como elegible para PathMode_Engineering
        self.mdPathMode_Engineering.addSubMode(self.mdDecisionMode_BBB_03)
        # Marcamos DecisionMode_BBW_00 como elegible para PathMode_Engineering
        self.mdPathMode_Engineering.addSubMode(self.mdDecisionMode_BBW_00)
        # Marcamos DecisionMode_BBW_01 como elegible para PathMode_Engineering
        self.mdPathMode_Engineering.addSubMode(self.mdDecisionMode_BBW_01)
        # Marcamos DecisionMode_BBW_03 como elegible para PathMode_Engineering
        self.mdPathMode_Engineering.addSubMode(self.mdDecisionMode_BBW_03)
        # Marcamos DecisionMode_BWB_00 como elegible para PathMode_Engineering
        self.mdPathMode_Engineering.addSubMode(self.mdDecisionMode_BWB_00)
        # Marcamos DecisionMode_BWB_01 como elegible para PathMode_Engineering
        self.mdPathMode_Engineering.addSubMode(self.mdDecisionMode_BWB_01)
        # Marcamos DecisionMode_BWB_03 como elegible para PathMode_Engineering
        self.mdPathMode_Engineering.addSubMode(self.mdDecisionMode_BWB_03)
        # Marcamos DecisionMode_BWW_00 como elegible para PathMode_Engineering
        self.mdPathMode_Engineering.addSubMode(self.mdDecisionMode_BWW_00)
        # Marcamos DecisionMode_BWW_01 como elegible para PathMode_Engineering
        self.mdPathMode_Engineering.addSubMode(self.mdDecisionMode_BWW_01)
        # Marcamos DecisionMode_BWW_03 como elegible para PathMode_Engineering
        self.mdPathMode_Engineering.addSubMode(self.mdDecisionMode_BWW_03)
        # Marcamos DecisionMode_WBB_00 como elegible para PathMode_Engineering
        self.mdPathMode_Engineering.addSubMode(self.mdDecisionMode_WBB_00)
        # Marcamos DecisionMode_WBB_01 como elegible para PathMode_Engineering
        self.mdPathMode_Engineering.addSubMode(self.mdDecisionMode_WBB_01)
        # Marcamos DecisionMode_WBB_03 como elegible para PathMode_Engineering
        self.mdPathMode_Engineering.addSubMode(self.mdDecisionMode_WBB_03)
        # Marcamos DecisionMode_WBW_00 como elegible para PathMode_Engineering
        self.mdPathMode_Engineering.addSubMode(self.mdDecisionMode_WBW_00)
        # Marcamos DecisionMode_WBW_01 como elegible para PathMode_Engineering
        self.mdPathMode_Engineering.addSubMode(self.mdDecisionMode_WBW_01)
        # Marcamos DecisionMode_WBW_03 como elegible para PathMode_Engineering
        self.mdPathMode_Engineering.addSubMode(self.mdDecisionMode_WBW_03)
        # Marcamos DecisionMode_WWB_00 como elegible para PathMode_Engineering
        self.mdPathMode_Engineering.addSubMode(self.mdDecisionMode_WWB_00)
        # Marcamos DecisionMode_WWB_01 como elegible para PathMode_Engineering
        self.mdPathMode_Engineering.addSubMode(self.mdDecisionMode_WWB_01)
        # Marcamos DecisionMode_WWB_03 como elegible para PathMode_Engineering
        self.mdPathMode_Engineering.addSubMode(self.mdDecisionMode_WWB_03)
        # Marcamos DecisionMode_WWW_00 como elegible para PathMode_Engineering
        self.mdPathMode_Engineering.addSubMode(self.mdDecisionMode_WWW_00)
        # Marcamos DecisionMode_WWW_01 como elegible para PathMode_Engineering
        self.mdPathMode_Engineering.addSubMode(self.mdDecisionMode_WWW_01)
        # Marcamos DecisionMode_WWW_03 como elegible para PathMode_Engineering
        self.mdPathMode_Engineering.addSubMode(self.mdDecisionMode_WWW_03)
        # Marcamos DecisionMode_Engineering como elegible para PathMode_Engineering
        self.mdPathMode_Engineering.addSubMode(self.mdDecisionMode_Engineering)
        # Marcamos LineFollowerMode_WBW como elegible para DecisionMode_BBW_01
        self.mdDecisionMode_BBW_01.addSubMode(self.mdLineFollowerMode_WBW)
        # Marcamos LineFollowerMode_WBW como elegible para DecisionMode_BWW_01
        self.mdDecisionMode_BWW_01.addSubMode(self.mdLineFollowerMode_WBW)
        # Marcamos LineFollowerMode_WBW como elegible para DecisionMode_BWW_03
        self.mdDecisionMode_BWW_03.addSubMode(self.mdLineFollowerMode_WBW)
        # Marcamos LineFollowerMode_WBW como elegible para DecisionMode_WBB_03
        self.mdDecisionMode_WBB_03.addSubMode(self.mdLineFollowerMode_WBW)
        # Marcamos LineFollowerMode_WBW como elegible para DecisionMode_WBW_01
        self.mdDecisionMode_WBW_01.addSubMode(self.mdLineFollowerMode_WBW)
        # Marcamos LineFollowerMode_WBW como elegible para DecisionMode_WBW_03
        self.mdDecisionMode_WBW_03.addSubMode(self.mdLineFollowerMode_WBW)
        # Marcamos LineFollowerMode_WBW como elegible para DecisionMode_WWB_01
        self.mdDecisionMode_WWB_01.addSubMode(self.mdLineFollowerMode_WBW)
        # Marcamos LineFollowerMode_WBW como elegible para DecisionMode_WWB_03
        self.mdDecisionMode_WWB_03.addSubMode(self.mdLineFollowerMode_WBW)
        # Marcamos LineFollowerMode_WBW como elegible para DecisionMode_Engineering
        self.mdDecisionMode_Engineering.addSubMode(self.mdLineFollowerMode_WBW)
        # Marcamos MobilityMode_Stop como elegible para DecisionMode_BBB_00
        self.mdDecisionMode_BBB_00.addSubMode(self.mdMobilityMode_Stop)
        # Marcamos MobilityMode_TurnRight como elegible para DecisionMode_BBB_01
        self.mdDecisionMode_BBB_01.addSubMode(self.mdMobilityMode_TurnRight)
        # Marcamos MobilityMode_TurnLeft como elegible para DecisionMode_BBB_03
        self.mdDecisionMode_BBB_03.addSubMode(self.mdMobilityMode_TurnLeft)
        # Marcamos MobilityMode_Stop como elegible para DecisionMode_BBW_00
        self.mdDecisionMode_BBW_00.addSubMode(self.mdMobilityMode_Stop)
        # Marcamos MobilityMode_TurnLeft como elegible para DecisionMode_BBW_03
        self.mdDecisionMode_BBW_03.addSubMode(self.mdMobilityMode_TurnLeft)
        # Marcamos MobilityMode_Stop como elegible para DecisionMode_BWB_00
        self.mdDecisionMode_BWB_00.addSubMode(self.mdMobilityMode_Stop)
        # Marcamos MobilityMode_Stop como elegible para DecisionMode_BWB_01
        self.mdDecisionMode_BWB_01.addSubMode(self.mdMobilityMode_Stop)
        # Marcamos MobilityMode_Stop como elegible para DecisionMode_BWB_03
        self.mdDecisionMode_BWB_03.addSubMode(self.mdMobilityMode_Stop)
        # Marcamos MobilityMode_Stop como elegible para DecisionMode_BWW_00
        self.mdDecisionMode_BWW_00.addSubMode(self.mdMobilityMode_Stop)
        # Marcamos MobilityMode_Stop como elegible para DecisionMode_WBB_00
        self.mdDecisionMode_WBB_00.addSubMode(self.mdMobilityMode_Stop)
        # Marcamos MobilityMode_TurnRight como elegible para DecisionMode_WBB_01
        self.mdDecisionMode_WBB_01.addSubMode(self.mdMobilityMode_TurnRight)
        # Marcamos MobilityMode_Stop como elegible para DecisionMode_WBW_00
        self.mdDecisionMode_WBW_00.addSubMode(self.mdMobilityMode_Stop)
        # Marcamos MobilityMode_Stop como elegible para DecisionMode_WWB_00
        self.mdDecisionMode_WWB_00.addSubMode(self.mdMobilityMode_Stop)
        # Marcamos MobilityMode_Stop como elegible para DecisionMode_WWW_00
        self.mdDecisionMode_WWW_00.addSubMode(self.mdMobilityMode_Stop)
        # Marcamos MobilityMode_Forward como elegible para DecisionMode_WWW_01
        self.mdDecisionMode_WWW_01.addSubMode(self.mdMobilityMode_Forward)
        # Marcamos MobilityMode_Stop como elegible para DecisionMode_WWW_03
        self.mdDecisionMode_WWW_03.addSubMode(self.mdMobilityMode_Stop)
        # Marcamos MobilityMode_Forward como elegible para DecisionMode_Engineering
        self.mdDecisionMode_Engineering.addSubMode(self.mdMobilityMode_Forward)
        # Marcamos MobilityMode_TurnRight como elegible para DecisionMode_Engineering
        self.mdDecisionMode_Engineering.addSubMode(self.mdMobilityMode_TurnRight)
        # Marcamos MobilityMode_TurnLeft como elegible para DecisionMode_Engineering
        self.mdDecisionMode_Engineering.addSubMode(self.mdMobilityMode_TurnLeft)
        # Marcamos MobilityMode_Stop como elegible para DecisionMode_Engineering
        self.mdDecisionMode_Engineering.addSubMode(self.mdMobilityMode_Stop)
        # Marcamos MobilityMode_SoftLeft como elegible para DecisionMode_Engineering
        self.mdDecisionMode_Engineering.addSubMode(self.mdMobilityMode_SoftLeft)
        # Marcamos MobilityMode_SoftRight como elegible para DecisionMode_Engineering
        self.mdDecisionMode_Engineering.addSubMode(self.mdMobilityMode_SoftRight)
        # Marcamos MobilityMode_Engineering como elegible para DecisionMode_Engineering
        self.mdDecisionMode_Engineering.addSubMode(self.mdMobilityMode_Engineering)
        # Marcamos RightWheelSpeedMode_Forward como elegible para MobilityMode_Forward
        self.mdMobilityMode_Forward.addSubMode(self.mdRightWheelSpeedMode_Forward)
        # Marcamos RightWheelSpeedMode_Back como elegible para MobilityMode_TurnRight
        self.mdMobilityMode_TurnRight.addSubMode(self.mdRightWheelSpeedMode_Back)
        # Marcamos RightWheelSpeedMode_Forward como elegible para MobilityMode_TurnLeft
        self.mdMobilityMode_TurnLeft.addSubMode(self.mdRightWheelSpeedMode_Forward)
        # Marcamos RightWheelSpeedMode_Stop como elegible para MobilityMode_Stop
        self.mdMobilityMode_Stop.addSubMode(self.mdRightWheelSpeedMode_Stop)
        # Marcamos RightWheelSpeedMode_Forward como elegible para MobilityMode_SoftLeft
        self.mdMobilityMode_SoftLeft.addSubMode(self.mdRightWheelSpeedMode_Forward)
        # Marcamos RightWheelSpeedMode_Stop como elegible para MobilityMode_SoftRight
        self.mdMobilityMode_SoftRight.addSubMode(self.mdRightWheelSpeedMode_Stop)
        # Marcamos RightWheelSpeedMode_Stop como elegible para MobilityMode_Engineering
        self.mdMobilityMode_Engineering.addSubMode(self.mdRightWheelSpeedMode_Stop)
        # Marcamos RightWheelSpeedMode_Forward como elegible para MobilityMode_Engineering
        self.mdMobilityMode_Engineering.addSubMode(self.mdRightWheelSpeedMode_Forward)
        # Marcamos RightWheelSpeedMode_Back como elegible para MobilityMode_Engineering
        self.mdMobilityMode_Engineering.addSubMode(self.mdRightWheelSpeedMode_Back)
        # Marcamos RightWheelSpeed_0 como elegible para RightWheelSpeedMode_Stop
        self.mdRightWheelSpeedMode_Stop.addValue(self.vlRightWheelSpeed_0)
        # Marcamos RightWheelSpeed_10 como elegible para RightWheelSpeedMode_Forward
        self.mdRightWheelSpeedMode_Forward.addValue(self.vlRightWheelSpeed_10)
        # Marcamos RightWheelSpeed__10 como elegible para RightWheelSpeedMode_Back
        self.mdRightWheelSpeedMode_Back.addValue(self.vlRightWheelSpeed__10)
        # Marcamos LeftWheelSpeedMode_Forward como elegible para MobilityMode_Forward
        self.mdMobilityMode_Forward.addSubMode(self.mdLeftWheelSpeedMode_Forward)
        # Marcamos LeftWheelSpeedMode_Forward como elegible para MobilityMode_TurnRight
        self.mdMobilityMode_TurnRight.addSubMode(self.mdLeftWheelSpeedMode_Forward)
        # Marcamos LeftWheelSpeedMode_Back como elegible para MobilityMode_TurnLeft
        self.mdMobilityMode_TurnLeft.addSubMode(self.mdLeftWheelSpeedMode_Back)
        # Marcamos LeftWheelSpeedMode_Stop como elegible para MobilityMode_Stop
        self.mdMobilityMode_Stop.addSubMode(self.mdLeftWheelSpeedMode_Stop)
        # Marcamos LeftWheelSpeedMode_Stop como elegible para MobilityMode_SoftLeft
        self.mdMobilityMode_SoftLeft.addSubMode(self.mdLeftWheelSpeedMode_Stop)
        # Marcamos LeftWheelSpeedMode_Forward como elegible para MobilityMode_SoftRight
        self.mdMobilityMode_SoftRight.addSubMode(self.mdLeftWheelSpeedMode_Forward)
        # Marcamos LeftWheelSpeedMode_Stop como elegible para MobilityMode_Engineering
        self.mdMobilityMode_Engineering.addSubMode(self.mdLeftWheelSpeedMode_Stop)
        # Marcamos LeftWheelSpeedMode_Forward como elegible para MobilityMode_Engineering
        self.mdMobilityMode_Engineering.addSubMode(self.mdLeftWheelSpeedMode_Forward)
        # Marcamos LeftWheelSpeedMode_Back como elegible para MobilityMode_Engineering
        self.mdMobilityMode_Engineering.addSubMode(self.mdLeftWheelSpeedMode_Back)
        # Marcamos LeftWheelSpeed_0 como elegible para LeftWheelSpeedMode_Stop
        self.mdLeftWheelSpeedMode_Stop.addValue(self.vlLeftWheelSpeed_0)
        # Marcamos LeftWheelSpeed_10 como elegible para LeftWheelSpeedMode_Forward
        self.mdLeftWheelSpeedMode_Forward.addValue(self.vlLeftWheelSpeed_10)
        # Marcamos LeftWheelSpeed__10 como elegible para LeftWheelSpeedMode_Back
        self.mdLeftWheelSpeedMode_Back.addValue(self.vlLeftWheelSpeed__10)
        # Marcamos NextStepMode_Yes como elegible para DecisionMode_BBB_01
        self.mdDecisionMode_BBB_01.addSubMode(self.mdNextStepMode_Yes)
        # Marcamos NextStepMode_Yes como elegible para DecisionMode_BBB_03
        self.mdDecisionMode_BBB_03.addSubMode(self.mdNextStepMode_Yes)
        # Marcamos NextStepMode_Yes como elegible para DecisionMode_BBW_03
        self.mdDecisionMode_BBW_03.addSubMode(self.mdNextStepMode_Yes)
        # Marcamos NextStepMode_Yes como elegible para DecisionMode_WBB_01
        self.mdDecisionMode_WBB_01.addSubMode(self.mdNextStepMode_Yes)
        # Marcamos NextStepMode_Yes como elegible para DecisionMode_Engineering
        self.mdDecisionMode_Engineering.addSubMode(self.mdNextStepMode_Yes)

    #----------------------------------------------------------------------
    #  Specific methods
    #----------------------------------------------------------------------


    ## MissionRobotMode 
    def get_MissionRobotMode(self)-> PORISMode:
        return self.sysMissionRobot.getSelectedMode()

    def set_MissionRobotMode(self, mode: PORISMode)-> PORISMode :
        return self.sysMissionRobot.selectMode(mode)


    ## PathMode 
    def get_PathMode(self)-> PORISMode:
        return self.sysPath.getSelectedMode()

    def set_PathMode(self, mode: PORISMode)-> PORISMode :
        return self.sysPath.selectMode(mode)


    ## DecisionMode 
    def get_DecisionMode(self)-> PORISMode:
        return self.sysDecision.getSelectedMode()

    def set_DecisionMode(self, mode: PORISMode)-> PORISMode :
        return self.sysDecision.selectMode(mode)


    ## LineFollowerMode 
    def get_LineFollowerMode(self)-> PORISMode:
        return self.sysLineFollower.getSelectedMode()

    def set_LineFollowerMode(self, mode: PORISMode)-> PORISMode :
        return self.sysLineFollower.selectMode(mode)


    ## MobilityMode 
    def get_MobilityMode(self)-> PORISMode:
        return self.sysMobility.getSelectedMode()

    def set_MobilityMode(self, mode: PORISMode)-> PORISMode :
        return self.sysMobility.selectMode(mode)


    ## prParam RightWheelSpeed 

    # RightWheelSpeed
    def get_RightWheelSpeed(self)-> PORISValue :
        return self.prRightWheelSpeed.getSelectedValue()

    def set_RightWheelSpeed(self, value: PORISValue)-> PORISValue :
        return self.prRightWheelSpeed.setValue(value)


    ## RightWheelSpeedMode 
    def get_RightWheelSpeedMode(self)-> PORISMode:
        return self.prRightWheelSpeed.getSelectedMode()

    def set_RightWheelSpeedMode(self, mode: PORISMode)-> PORISMode :
        return self.prRightWheelSpeed.selectMode(mode)


    ## prParam LeftWheelSpeed 

    # LeftWheelSpeed
    def get_LeftWheelSpeed(self)-> PORISValue :
        return self.prLeftWheelSpeed.getSelectedValue()

    def set_LeftWheelSpeed(self, value: PORISValue)-> PORISValue :
        return self.prLeftWheelSpeed.setValue(value)


    ## LeftWheelSpeedMode 
    def get_LeftWheelSpeedMode(self)-> PORISMode:
        return self.prLeftWheelSpeed.getSelectedMode()

    def set_LeftWheelSpeedMode(self, mode: PORISMode)-> PORISMode :
        return self.prLeftWheelSpeed.selectMode(mode)


    ## NextStepMode 
    def get_NextStepMode(self)-> PORISMode:
        return self.sysNextStep.getSelectedMode()

    def set_NextStepMode(self, mode: PORISMode)-> PORISMode :
        return self.sysNextStep.selectMode(mode)

