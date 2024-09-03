from PORIS import *

class controlboxPORIS(PORISDoc):
    def __init__(self, project_id):
        super().__init__(project_id)
        self.sysControlBox = PORISSys("ControlBox")
        self.mdControlBoxMode_UNKNOWN = PORISMode("ControlBoxMode_UNKNOWN")
        self.setRoot(self.sysControlBox)
        self.prOutputMux = PORISParam("OutputMux")
        self.mdOutputMuxMode_UNKNOWN = PORISMode("OutputMuxMode_UNKNOWN")
        self.vlOutputMux_UNKNOWN = PORISValue("OutputMux_UNKNOWN")
        self.sysControlLoop = PORISSys("ControlLoop")
        self.mdControlLoopMode_UNKNOWN = PORISMode("ControlLoopMode_UNKNOWN")
        self.prKd = PORISParam("Kd")
        self.mdKdMode_UNKNOWN = PORISMode("KdMode_UNKNOWN")
        self.vlKd_UNKNOWN = PORISValue("Kd_UNKNOWN")
        self.prKi = PORISParam("Ki")
        self.mdKiMode_UNKNOWN = PORISMode("KiMode_UNKNOWN")
        self.vlKi_UNKNOWN = PORISValue("Ki_UNKNOWN")
        self.prKp = PORISParam("Kp")
        self.mdKpMode_UNKNOWN = PORISMode("KpMode_UNKNOWN")
        self.vlKp_UNKNOWN = PORISValue("Kp_UNKNOWN")
        self.sysSubtractor = PORISSys("Subtractor")
        self.mdSubtractorMode_UNKNOWN = PORISMode("SubtractorMode_UNKNOWN")
        self.prRate = PORISParam("Rate")
        self.mdRateMode_UNKNOWN = PORISMode("RateMode_UNKNOWN")
        self.vlRate_UNKNOWN = PORISValue("Rate_UNKNOWN")
        self.prSetPoint = PORISParam("SetPoint")
        self.mdSetPointMode_UNKNOWN = PORISMode("SetPointMode_UNKNOWN")
        self.vlSetPoint_UNKNOWN = PORISValue("SetPoint_UNKNOWN")
        self.mdOutputMuxMode_AllNothing = PORISMode("OutputMuxMode_AllNothing")
        self.mdOutputMuxMode_PID = PORISMode("OutputMuxMode_PID")
        self.mdOutputMuxMode_Abrupt = PORISMode("OutputMuxMode_Abrupt")
        self.mdOutputMuxMode_Keep = PORISMode("OutputMuxMode_Keep")
        self.mdOutputMuxMode_Sweet = PORISMode("OutputMuxMode_Sweet")
        self.vlOutputMux_CtrlLoopOutput = PORISValue("OutputMux_CtrlLoopOutput")
        self.vlOutputMux_CurrentOutput = PORISValue("OutputMux_CurrentOutput")
        self.vlOutputMux_0 = PORISValue("OutputMux_0")
        self.vlOutputMux_SubtractOutput = PORISValue("OutputMux_SubtractOutput")
        self.vlOutputMux_AllNothing = PORISValue("OutputMux_AllNothing")
        self.mdControlBoxMode_PI = PORISMode("ControlBoxMode_PI")
        self.mdControlBoxMode_P = PORISMode("ControlBoxMode_P")
        self.mdControlBoxMode_PID = PORISMode("ControlBoxMode_PID")
        self.mdControlBoxMode_Abrupt = PORISMode("ControlBoxMode_Abrupt")
        self.mdControlBoxMode_Keep = PORISMode("ControlBoxMode_Keep")
        self.mdControlBoxMode_Sweet = PORISMode("ControlBoxMode_Sweet")
        self.mdControlLoopMode_P = PORISMode("ControlLoopMode_P")
        self.vlKd_Range = PORISValueFloat("Kd_Range",0,0.01,0.5)
        self.mdKdMode_Normal = PORISMode("KdMode_Normal")
        self.vlKd_0 = PORISValue("Kd_0")
        self.mdKdMode_Disabled = PORISMode("KdMode_Disabled")
        self.vlKi_Range = PORISValueFloat("Ki_Range",0,0.01,0.5)
        self.mdKiMode_Normal = PORISMode("KiMode_Normal")
        self.vlKi_0 = PORISValue("Ki_0")
        self.mdKiMode_Disabled = PORISMode("KiMode_Disabled")
        self.vlKp_Range = PORISValueFloat("Kp_Range",0,0.01,0.5)
        self.mdKpMode_Normal = PORISMode("KpMode_Normal")
        self.mdControlLoopMode_PI = PORISMode("ControlLoopMode_PI")
        self.mdControlLoopMode_PID = PORISMode("ControlLoopMode_PID")
        self.vlRate_Range = PORISValueFloat("Rate_Range",0,0.01,0.5)
        self.mdRateMode_Active = PORISMode("RateMode_Active")
        self.mdSubtractorMode_Active = PORISMode("SubtractorMode_Active")
        self.mdControlBoxMode_AllNothing = PORISMode("ControlBoxMode_AllNothing")
        self.vlSetPoint_Range = PORISValueFloat("SetPoint_Range",0,0.01,0.5)
        self.mdSetPointMode_Normal = PORISMode("SetPointMode_Normal")
        self.mdControlBoxMode_Engineering = PORISMode("ControlBoxMode_Engineering")
        self.mdControlLoopMode_Engineering = PORISMode("ControlLoopMode_Engineering")
        self.mdSubtractorMode_Engineering = PORISMode("SubtractorMode_Engineering")
        self.addNode(self.sysControlBox)
        self.sysControlBox.ident = "ControlBox"
        self.sysControlBox.description = ""
        self.addNode(self.mdControlBoxMode_UNKNOWN)
        self.mdControlBoxMode_UNKNOWN.ident = "ControlBoxMode_UNKNOWN"
        self.mdControlBoxMode_UNKNOWN.description = ""
        self.sysControlBox.addMode(self.mdControlBoxMode_UNKNOWN)
        self.addNode(self.prOutputMux)
        self.prOutputMux.ident = "OutputMux"
        self.prOutputMux.description = ""
        self.sysControlBox.addParam(self.prOutputMux)
        self.addNode(self.vlOutputMux_UNKNOWN)
        self.vlOutputMux_UNKNOWN.ident = "OutputMux_UNKNOWN"
        self.vlOutputMux_UNKNOWN.description = "Unknown value for OutputMux"
        self.prOutputMux.addValue(self.vlOutputMux_UNKNOWN)
        self.addNode(self.mdOutputMuxMode_UNKNOWN)
        self.mdOutputMuxMode_UNKNOWN.ident = "OutputMuxMode_UNKNOWN"
        self.mdOutputMuxMode_UNKNOWN.description = "Unknown mode for OutputMux"
        self.prOutputMux.addMode(self.mdOutputMuxMode_UNKNOWN)
        self.mdOutputMuxMode_UNKNOWN.addValue(self.vlOutputMux_UNKNOWN)
        self.mdControlBoxMode_UNKNOWN.addSubMode(self.mdOutputMuxMode_UNKNOWN)
        self.addNode(self.sysControlLoop)
        self.sysControlLoop.ident = "ControlLoop"
        self.sysControlLoop.description = ""
        self.sysControlBox.addSubsystem(self.sysControlLoop)
        self.addNode(self.mdControlLoopMode_UNKNOWN)
        self.mdControlLoopMode_UNKNOWN.ident = "ControlLoopMode_UNKNOWN"
        self.mdControlLoopMode_UNKNOWN.description = ""
        self.sysControlLoop.addMode(self.mdControlLoopMode_UNKNOWN)
        self.addNode(self.prKd)
        self.prKd.ident = "Kd"
        self.prKd.description = ""
        self.sysControlLoop.addParam(self.prKd)
        self.addNode(self.vlKd_UNKNOWN)
        self.vlKd_UNKNOWN.ident = "Kd_UNKNOWN"
        self.vlKd_UNKNOWN.description = "Unknown value for Kd"
        self.prKd.addValue(self.vlKd_UNKNOWN)
        self.addNode(self.mdKdMode_UNKNOWN)
        self.mdKdMode_UNKNOWN.ident = "KdMode_UNKNOWN"
        self.mdKdMode_UNKNOWN.description = "Unknown mode for Kd"
        self.prKd.addMode(self.mdKdMode_UNKNOWN)
        self.mdKdMode_UNKNOWN.addValue(self.vlKd_UNKNOWN)
        self.mdControlLoopMode_UNKNOWN.addSubMode(self.mdKdMode_UNKNOWN)
        self.addNode(self.prKi)
        self.prKi.ident = "Ki"
        self.prKi.description = ""
        self.sysControlLoop.addParam(self.prKi)
        self.addNode(self.vlKi_UNKNOWN)
        self.vlKi_UNKNOWN.ident = "Ki_UNKNOWN"
        self.vlKi_UNKNOWN.description = "Unknown value for Ki"
        self.prKi.addValue(self.vlKi_UNKNOWN)
        self.addNode(self.mdKiMode_UNKNOWN)
        self.mdKiMode_UNKNOWN.ident = "KiMode_UNKNOWN"
        self.mdKiMode_UNKNOWN.description = "Unknown mode for Ki"
        self.prKi.addMode(self.mdKiMode_UNKNOWN)
        self.mdKiMode_UNKNOWN.addValue(self.vlKi_UNKNOWN)
        self.mdControlLoopMode_UNKNOWN.addSubMode(self.mdKiMode_UNKNOWN)
        self.addNode(self.prKp)
        self.prKp.ident = "Kp"
        self.prKp.description = ""
        self.sysControlLoop.addParam(self.prKp)
        self.addNode(self.vlKp_UNKNOWN)
        self.vlKp_UNKNOWN.ident = "Kp_UNKNOWN"
        self.vlKp_UNKNOWN.description = "Unknown value for Kp"
        self.prKp.addValue(self.vlKp_UNKNOWN)
        self.addNode(self.mdKpMode_UNKNOWN)
        self.mdKpMode_UNKNOWN.ident = "KpMode_UNKNOWN"
        self.mdKpMode_UNKNOWN.description = "Unknown mode for Kp"
        self.prKp.addMode(self.mdKpMode_UNKNOWN)
        self.mdKpMode_UNKNOWN.addValue(self.vlKp_UNKNOWN)
        self.mdControlLoopMode_UNKNOWN.addSubMode(self.mdKpMode_UNKNOWN)
        self.addNode(self.sysSubtractor)
        self.sysSubtractor.ident = "Subtractor"
        self.sysSubtractor.description = ""
        self.sysControlBox.addSubsystem(self.sysSubtractor)
        self.addNode(self.mdSubtractorMode_UNKNOWN)
        self.mdSubtractorMode_UNKNOWN.ident = "SubtractorMode_UNKNOWN"
        self.mdSubtractorMode_UNKNOWN.description = ""
        self.sysSubtractor.addMode(self.mdSubtractorMode_UNKNOWN)
        self.addNode(self.prRate)
        self.prRate.ident = "Rate"
        self.prRate.description = ""
        self.sysSubtractor.addParam(self.prRate)
        self.addNode(self.vlRate_UNKNOWN)
        self.vlRate_UNKNOWN.ident = "Rate_UNKNOWN"
        self.vlRate_UNKNOWN.description = "Unknown value for Rate"
        self.prRate.addValue(self.vlRate_UNKNOWN)
        self.addNode(self.mdRateMode_UNKNOWN)
        self.mdRateMode_UNKNOWN.ident = "RateMode_UNKNOWN"
        self.mdRateMode_UNKNOWN.description = "Unknown mode for Rate"
        self.prRate.addMode(self.mdRateMode_UNKNOWN)
        self.mdRateMode_UNKNOWN.addValue(self.vlRate_UNKNOWN)
        self.mdSubtractorMode_UNKNOWN.addSubMode(self.mdRateMode_UNKNOWN)
        self.addNode(self.prSetPoint)
        self.prSetPoint.ident = "SetPoint"
        self.prSetPoint.description = ""
        self.sysControlBox.addParam(self.prSetPoint)
        self.addNode(self.vlSetPoint_UNKNOWN)
        self.vlSetPoint_UNKNOWN.ident = "SetPoint_UNKNOWN"
        self.vlSetPoint_UNKNOWN.description = "Unknown value for SetPoint"
        self.prSetPoint.addValue(self.vlSetPoint_UNKNOWN)
        self.addNode(self.mdSetPointMode_UNKNOWN)
        self.mdSetPointMode_UNKNOWN.ident = "SetPointMode_UNKNOWN"
        self.mdSetPointMode_UNKNOWN.description = "Unknown mode for SetPoint"
        self.prSetPoint.addMode(self.mdSetPointMode_UNKNOWN)
        self.mdSetPointMode_UNKNOWN.addValue(self.vlSetPoint_UNKNOWN)
        self.mdControlBoxMode_UNKNOWN.addSubMode(self.mdSetPointMode_UNKNOWN)
        self.addNode(self.mdOutputMuxMode_AllNothing)
        self.mdOutputMuxMode_AllNothing.ident = "OutputMuxMode_AllNothing"
        self.mdOutputMuxMode_AllNothing.description = ""
        self.prOutputMux.addMode(self.mdOutputMuxMode_AllNothing)
        self.addNode(self.mdOutputMuxMode_PID)
        self.mdOutputMuxMode_PID.ident = "OutputMuxMode_PID"
        self.mdOutputMuxMode_PID.description = ""
        self.prOutputMux.addMode(self.mdOutputMuxMode_PID)
        self.addNode(self.mdOutputMuxMode_Abrupt)
        self.mdOutputMuxMode_Abrupt.ident = "OutputMuxMode_Abrupt"
        self.mdOutputMuxMode_Abrupt.description = ""
        self.prOutputMux.addMode(self.mdOutputMuxMode_Abrupt)
        self.addNode(self.mdOutputMuxMode_Keep)
        self.mdOutputMuxMode_Keep.ident = "OutputMuxMode_Keep"
        self.mdOutputMuxMode_Keep.description = ""
        self.prOutputMux.addMode(self.mdOutputMuxMode_Keep)
        self.addNode(self.mdOutputMuxMode_Sweet)
        self.mdOutputMuxMode_Sweet.ident = "OutputMuxMode_Sweet"
        self.mdOutputMuxMode_Sweet.description = ""
        self.prOutputMux.addMode(self.mdOutputMuxMode_Sweet)
        self.addNode(self.vlOutputMux_CtrlLoopOutput)
        self.vlOutputMux_CtrlLoopOutput.ident = "OutputMux_CtrlLoopOutput"
        self.vlOutputMux_CtrlLoopOutput.description = ""
        self.prOutputMux.addValue(self.vlOutputMux_CtrlLoopOutput)
        self.addNode(self.vlOutputMux_CurrentOutput)
        self.vlOutputMux_CurrentOutput.ident = "OutputMux_CurrentOutput"
        self.vlOutputMux_CurrentOutput.description = ""
        self.prOutputMux.addValue(self.vlOutputMux_CurrentOutput)
        self.addNode(self.vlOutputMux_0)
        self.vlOutputMux_0.ident = "OutputMux_0"
        self.vlOutputMux_0.description = ""
        self.prOutputMux.addValue(self.vlOutputMux_0)
        self.addNode(self.vlOutputMux_SubtractOutput)
        self.vlOutputMux_SubtractOutput.ident = "OutputMux_SubtractOutput"
        self.vlOutputMux_SubtractOutput.description = ""
        self.prOutputMux.addValue(self.vlOutputMux_SubtractOutput)
        self.addNode(self.vlOutputMux_AllNothing)
        self.vlOutputMux_AllNothing.ident = "OutputMux_AllNothing"
        self.vlOutputMux_AllNothing.description = ""
        self.prOutputMux.addValue(self.vlOutputMux_AllNothing)
        self.addNode(self.mdControlBoxMode_PI)
        self.mdControlBoxMode_PI.ident = "ControlBoxMode_PI"
        self.mdControlBoxMode_PI.description = ""
        self.sysControlBox.addMode(self.mdControlBoxMode_PI)
        self.addNode(self.mdControlBoxMode_P)
        self.mdControlBoxMode_P.ident = "ControlBoxMode_P"
        self.mdControlBoxMode_P.description = ""
        self.sysControlBox.addMode(self.mdControlBoxMode_P)
        self.addNode(self.mdControlBoxMode_PID)
        self.mdControlBoxMode_PID.ident = "ControlBoxMode_PID"
        self.mdControlBoxMode_PID.description = ""
        self.sysControlBox.addMode(self.mdControlBoxMode_PID)
        self.addNode(self.mdControlBoxMode_Abrupt)
        self.mdControlBoxMode_Abrupt.ident = "ControlBoxMode_Abrupt"
        self.mdControlBoxMode_Abrupt.description = ""
        self.sysControlBox.addMode(self.mdControlBoxMode_Abrupt)
        self.addNode(self.mdControlBoxMode_Keep)
        self.mdControlBoxMode_Keep.ident = "ControlBoxMode_Keep"
        self.mdControlBoxMode_Keep.description = ""
        self.sysControlBox.addMode(self.mdControlBoxMode_Keep)
        self.addNode(self.mdControlBoxMode_Sweet)
        self.mdControlBoxMode_Sweet.ident = "ControlBoxMode_Sweet"
        self.mdControlBoxMode_Sweet.description = ""
        self.sysControlBox.addMode(self.mdControlBoxMode_Sweet)
        self.addNode(self.mdControlLoopMode_P)
        self.mdControlLoopMode_P.ident = "ControlLoopMode_P"
        self.mdControlLoopMode_P.description = ""
        self.sysControlLoop.addMode(self.mdControlLoopMode_P)
        self.addNode(self.vlKd_Range)
        self.vlKd_Range.ident = "Kd_Range"
        self.vlKd_Range.description = ""
        self.prKd.addValue(self.vlKd_Range)
        self.addNode(self.mdKdMode_Normal)
        self.mdKdMode_Normal.ident = "KdMode_Normal"
        self.mdKdMode_Normal.description = ""
        self.prKd.addMode(self.mdKdMode_Normal)
        self.addNode(self.vlKd_0)
        self.vlKd_0.ident = "Kd_0"
        self.vlKd_0.description = ""
        self.prKd.addValue(self.vlKd_0)
        self.addNode(self.mdKdMode_Disabled)
        self.mdKdMode_Disabled.ident = "KdMode_Disabled"
        self.mdKdMode_Disabled.description = ""
        self.prKd.addMode(self.mdKdMode_Disabled)
        self.addNode(self.vlKi_Range)
        self.vlKi_Range.ident = "Ki_Range"
        self.vlKi_Range.description = ""
        self.prKi.addValue(self.vlKi_Range)
        self.addNode(self.mdKiMode_Normal)
        self.mdKiMode_Normal.ident = "KiMode_Normal"
        self.mdKiMode_Normal.description = ""
        self.prKi.addMode(self.mdKiMode_Normal)
        self.addNode(self.vlKi_0)
        self.vlKi_0.ident = "Ki_0"
        self.vlKi_0.description = ""
        self.prKi.addValue(self.vlKi_0)
        self.addNode(self.mdKiMode_Disabled)
        self.mdKiMode_Disabled.ident = "KiMode_Disabled"
        self.mdKiMode_Disabled.description = ""
        self.prKi.addMode(self.mdKiMode_Disabled)
        self.addNode(self.vlKp_Range)
        self.vlKp_Range.ident = "Kp_Range"
        self.vlKp_Range.description = ""
        self.prKp.addValue(self.vlKp_Range)
        self.addNode(self.mdKpMode_Normal)
        self.mdKpMode_Normal.ident = "KpMode_Normal"
        self.mdKpMode_Normal.description = ""
        self.prKp.addMode(self.mdKpMode_Normal)
        self.addNode(self.mdControlLoopMode_PI)
        self.mdControlLoopMode_PI.ident = "ControlLoopMode_PI"
        self.mdControlLoopMode_PI.description = ""
        self.sysControlLoop.addMode(self.mdControlLoopMode_PI)
        self.addNode(self.mdControlLoopMode_PID)
        self.mdControlLoopMode_PID.ident = "ControlLoopMode_PID"
        self.mdControlLoopMode_PID.description = ""
        self.sysControlLoop.addMode(self.mdControlLoopMode_PID)
        self.addNode(self.vlRate_Range)
        self.vlRate_Range.ident = "Rate_Range"
        self.vlRate_Range.description = ""
        self.prRate.addValue(self.vlRate_Range)
        self.addNode(self.mdRateMode_Active)
        self.mdRateMode_Active.ident = "RateMode_Active"
        self.mdRateMode_Active.description = ""
        self.prRate.addMode(self.mdRateMode_Active)
        self.addNode(self.mdSubtractorMode_Active)
        self.mdSubtractorMode_Active.ident = "SubtractorMode_Active"
        self.mdSubtractorMode_Active.description = ""
        self.sysSubtractor.addMode(self.mdSubtractorMode_Active)
        self.addNode(self.mdControlBoxMode_AllNothing)
        self.mdControlBoxMode_AllNothing.ident = "ControlBoxMode_AllNothing"
        self.mdControlBoxMode_AllNothing.description = ""
        self.sysControlBox.addMode(self.mdControlBoxMode_AllNothing)
        self.addNode(self.vlSetPoint_Range)
        self.vlSetPoint_Range.ident = "SetPoint_Range"
        self.vlSetPoint_Range.description = ""
        self.prSetPoint.addValue(self.vlSetPoint_Range)
        self.addNode(self.mdSetPointMode_Normal)
        self.mdSetPointMode_Normal.ident = "SetPointMode_Normal"
        self.mdSetPointMode_Normal.description = ""
        self.prSetPoint.addMode(self.mdSetPointMode_Normal)
        self.addNode(self.mdControlBoxMode_Engineering)
        self.mdControlBoxMode_Engineering.ident = "ControlBoxMode_Engineering"
        self.mdControlBoxMode_Engineering.description = "ControlBox engineering mode"
        self.sysControlBox.addMode(self.mdControlBoxMode_Engineering)
        self.addNode(self.mdControlLoopMode_Engineering)
        self.mdControlLoopMode_Engineering.ident = "ControlLoopMode_Engineering"
        self.mdControlLoopMode_Engineering.description = "ControlLoop engineering mode"
        self.sysControlLoop.addMode(self.mdControlLoopMode_Engineering)
        self.addNode(self.mdSubtractorMode_Engineering)
        self.mdSubtractorMode_Engineering.ident = "SubtractorMode_Engineering"
        self.mdSubtractorMode_Engineering.description = "Subtractor engineering mode"
        self.sysSubtractor.addMode(self.mdSubtractorMode_Engineering)
        # Marcamos OutputMuxMode_PID como elegible para ControlBoxMode_PI
        self.mdControlBoxMode_PI.addSubMode(self.mdOutputMuxMode_PID)
        # Marcamos OutputMuxMode_PID como elegible para ControlBoxMode_P
        self.mdControlBoxMode_P.addSubMode(self.mdOutputMuxMode_PID)
        # Marcamos OutputMuxMode_PID como elegible para ControlBoxMode_PID
        self.mdControlBoxMode_PID.addSubMode(self.mdOutputMuxMode_PID)
        # Marcamos OutputMuxMode_Abrupt como elegible para ControlBoxMode_Abrupt
        self.mdControlBoxMode_Abrupt.addSubMode(self.mdOutputMuxMode_Abrupt)
        # Marcamos OutputMuxMode_Keep como elegible para ControlBoxMode_Keep
        self.mdControlBoxMode_Keep.addSubMode(self.mdOutputMuxMode_Keep)
        # Marcamos OutputMuxMode_Sweet como elegible para ControlBoxMode_Sweet
        self.mdControlBoxMode_Sweet.addSubMode(self.mdOutputMuxMode_Sweet)
        # Marcamos OutputMuxMode_AllNothing como elegible para ControlBoxMode_AllNothing
        self.mdControlBoxMode_AllNothing.addSubMode(self.mdOutputMuxMode_AllNothing)
        # Marcamos OutputMuxMode_AllNothing como elegible para ControlBoxMode_Engineering
        self.mdControlBoxMode_Engineering.addSubMode(self.mdOutputMuxMode_AllNothing)
        # Marcamos OutputMuxMode_PID como elegible para ControlBoxMode_Engineering
        self.mdControlBoxMode_Engineering.addSubMode(self.mdOutputMuxMode_PID)
        # Marcamos OutputMuxMode_Abrupt como elegible para ControlBoxMode_Engineering
        self.mdControlBoxMode_Engineering.addSubMode(self.mdOutputMuxMode_Abrupt)
        # Marcamos OutputMuxMode_Keep como elegible para ControlBoxMode_Engineering
        self.mdControlBoxMode_Engineering.addSubMode(self.mdOutputMuxMode_Keep)
        # Marcamos OutputMuxMode_Sweet como elegible para ControlBoxMode_Engineering
        self.mdControlBoxMode_Engineering.addSubMode(self.mdOutputMuxMode_Sweet)
        # Marcamos OutputMux_AllNothing como elegible para OutputMuxMode_AllNothing
        self.mdOutputMuxMode_AllNothing.addValue(self.vlOutputMux_AllNothing)
        # Marcamos OutputMux_CtrlLoopOutput como elegible para OutputMuxMode_PID
        self.mdOutputMuxMode_PID.addValue(self.vlOutputMux_CtrlLoopOutput)
        # Marcamos OutputMux_0 como elegible para OutputMuxMode_Abrupt
        self.mdOutputMuxMode_Abrupt.addValue(self.vlOutputMux_0)
        # Marcamos OutputMux_CurrentOutput como elegible para OutputMuxMode_Keep
        self.mdOutputMuxMode_Keep.addValue(self.vlOutputMux_CurrentOutput)
        # Marcamos OutputMux_SubtractOutput como elegible para OutputMuxMode_Sweet
        self.mdOutputMuxMode_Sweet.addValue(self.vlOutputMux_SubtractOutput)
        # Marcamos ControlLoopMode_PI como elegible para ControlBoxMode_PI
        self.mdControlBoxMode_PI.addSubMode(self.mdControlLoopMode_PI)
        # Marcamos ControlLoopMode_P como elegible para ControlBoxMode_P
        self.mdControlBoxMode_P.addSubMode(self.mdControlLoopMode_P)
        # Marcamos ControlLoopMode_PID como elegible para ControlBoxMode_PID
        self.mdControlBoxMode_PID.addSubMode(self.mdControlLoopMode_PID)
        # Marcamos ControlLoopMode_P como elegible para ControlBoxMode_Engineering
        self.mdControlBoxMode_Engineering.addSubMode(self.mdControlLoopMode_P)
        # Marcamos ControlLoopMode_PI como elegible para ControlBoxMode_Engineering
        self.mdControlBoxMode_Engineering.addSubMode(self.mdControlLoopMode_PI)
        # Marcamos ControlLoopMode_PID como elegible para ControlBoxMode_Engineering
        self.mdControlBoxMode_Engineering.addSubMode(self.mdControlLoopMode_PID)
        # Marcamos ControlLoopMode_Engineering como elegible para ControlBoxMode_Engineering
        self.mdControlBoxMode_Engineering.addSubMode(self.mdControlLoopMode_Engineering)
        # Marcamos KdMode_Disabled como elegible para ControlLoopMode_P
        self.mdControlLoopMode_P.addSubMode(self.mdKdMode_Disabled)
        # Marcamos KdMode_Disabled como elegible para ControlLoopMode_PI
        self.mdControlLoopMode_PI.addSubMode(self.mdKdMode_Disabled)
        # Marcamos KdMode_Normal como elegible para ControlLoopMode_PID
        self.mdControlLoopMode_PID.addSubMode(self.mdKdMode_Normal)
        # Marcamos KdMode_Normal como elegible para ControlLoopMode_Engineering
        self.mdControlLoopMode_Engineering.addSubMode(self.mdKdMode_Normal)
        # Marcamos KdMode_Disabled como elegible para ControlLoopMode_Engineering
        self.mdControlLoopMode_Engineering.addSubMode(self.mdKdMode_Disabled)
        # Marcamos Kd_Range como elegible para KdMode_Normal
        self.mdKdMode_Normal.addValue(self.vlKd_Range)
        # Marcamos Kd_0 como elegible para KdMode_Disabled
        self.mdKdMode_Disabled.addValue(self.vlKd_0)
        # Marcamos KiMode_Disabled como elegible para ControlLoopMode_P
        self.mdControlLoopMode_P.addSubMode(self.mdKiMode_Disabled)
        # Marcamos KiMode_Normal como elegible para ControlLoopMode_PI
        self.mdControlLoopMode_PI.addSubMode(self.mdKiMode_Normal)
        # Marcamos KiMode_Normal como elegible para ControlLoopMode_PID
        self.mdControlLoopMode_PID.addSubMode(self.mdKiMode_Normal)
        # Marcamos KiMode_Normal como elegible para ControlLoopMode_Engineering
        self.mdControlLoopMode_Engineering.addSubMode(self.mdKiMode_Normal)
        # Marcamos KiMode_Disabled como elegible para ControlLoopMode_Engineering
        self.mdControlLoopMode_Engineering.addSubMode(self.mdKiMode_Disabled)
        # Marcamos Ki_Range como elegible para KiMode_Normal
        self.mdKiMode_Normal.addValue(self.vlKi_Range)
        # Marcamos Ki_0 como elegible para KiMode_Disabled
        self.mdKiMode_Disabled.addValue(self.vlKi_0)
        # Marcamos KpMode_Normal como elegible para ControlLoopMode_P
        self.mdControlLoopMode_P.addSubMode(self.mdKpMode_Normal)
        # Marcamos KpMode_Normal como elegible para ControlLoopMode_PI
        self.mdControlLoopMode_PI.addSubMode(self.mdKpMode_Normal)
        # Marcamos KpMode_Normal como elegible para ControlLoopMode_PID
        self.mdControlLoopMode_PID.addSubMode(self.mdKpMode_Normal)
        # Marcamos KpMode_Normal como elegible para ControlLoopMode_Engineering
        self.mdControlLoopMode_Engineering.addSubMode(self.mdKpMode_Normal)
        # Marcamos Kp_Range como elegible para KpMode_Normal
        self.mdKpMode_Normal.addValue(self.vlKp_Range)
        # Marcamos SubtractorMode_Active como elegible para ControlBoxMode_Sweet
        self.mdControlBoxMode_Sweet.addSubMode(self.mdSubtractorMode_Active)
        # Marcamos SubtractorMode_Active como elegible para ControlBoxMode_Engineering
        self.mdControlBoxMode_Engineering.addSubMode(self.mdSubtractorMode_Active)
        # Marcamos SubtractorMode_Engineering como elegible para ControlBoxMode_Engineering
        self.mdControlBoxMode_Engineering.addSubMode(self.mdSubtractorMode_Engineering)
        # Marcamos RateMode_Active como elegible para SubtractorMode_Active
        self.mdSubtractorMode_Active.addSubMode(self.mdRateMode_Active)
        # Marcamos RateMode_Active como elegible para SubtractorMode_Engineering
        self.mdSubtractorMode_Engineering.addSubMode(self.mdRateMode_Active)
        # Marcamos Rate_Range como elegible para RateMode_Active
        self.mdRateMode_Active.addValue(self.vlRate_Range)
        # Marcamos SetPointMode_Normal como elegible para ControlBoxMode_PI
        self.mdControlBoxMode_PI.addSubMode(self.mdSetPointMode_Normal)
        # Marcamos SetPointMode_Normal como elegible para ControlBoxMode_P
        self.mdControlBoxMode_P.addSubMode(self.mdSetPointMode_Normal)
        # Marcamos SetPointMode_Normal como elegible para ControlBoxMode_PID
        self.mdControlBoxMode_PID.addSubMode(self.mdSetPointMode_Normal)
        # Marcamos SetPointMode_Normal como elegible para ControlBoxMode_AllNothing
        self.mdControlBoxMode_AllNothing.addSubMode(self.mdSetPointMode_Normal)
        # Marcamos SetPointMode_Normal como elegible para ControlBoxMode_Engineering
        self.mdControlBoxMode_Engineering.addSubMode(self.mdSetPointMode_Normal)
        # Marcamos SetPoint_Range como elegible para SetPointMode_Normal
        self.mdSetPointMode_Normal.addValue(self.vlSetPoint_Range)

    #----------------------------------------------------------------------
    #  Specific methods
    #----------------------------------------------------------------------


    ## ControlBoxMode 
    def get_ControlBoxMode(self)-> PORISMode:
        return self.sysControlBox.getSelectedMode()

    def set_ControlBoxMode(self, mode: PORISMode)-> PORISMode :
        return self.sysControlBox.selectMode(mode)


    ## prParam OutputMux 

    # OutputMux
    def get_OutputMux(self)-> PORISValue :
        return self.prOutputMux.getSelectedValue()

    def set_OutputMux(self, value: PORISValue)-> PORISValue :
        return self.prOutputMux.setValue(value)


    ## OutputMuxMode 
    def get_OutputMuxMode(self)-> PORISMode:
        return self.prOutputMux.getSelectedMode()

    def set_OutputMuxMode(self, mode: PORISMode)-> PORISMode :
        return self.prOutputMux.selectMode(mode)


    ## ControlLoopMode 
    def get_ControlLoopMode(self)-> PORISMode:
        return self.sysControlLoop.getSelectedMode()

    def set_ControlLoopMode(self, mode: PORISMode)-> PORISMode :
        return self.sysControlLoop.selectMode(mode)


    ## prParam Kd 

    # Kd
    def get_Kd(self)-> PORISValue :
        return self.prKd.getSelectedValue()

    def set_Kd(self, value: PORISValue)-> PORISValue :
        return self.prKd.setValue(value)


    ## KdMode 
    def get_KdMode(self)-> PORISMode:
        return self.prKd.getSelectedMode()

    def set_KdMode(self, mode: PORISMode)-> PORISMode :
        return self.prKd.selectMode(mode)


    ## prParam ControlLoop 

    # KdDouble  
    def get_KdDouble(self)-> float :
        v = self.prKd.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_KdDouble(self, data: float)-> float :
        return self.prKd.getSelectedValue().setData(data)


    ## prParam Ki 

    # Ki
    def get_Ki(self)-> PORISValue :
        return self.prKi.getSelectedValue()

    def set_Ki(self, value: PORISValue)-> PORISValue :
        return self.prKi.setValue(value)


    ## KiMode 
    def get_KiMode(self)-> PORISMode:
        return self.prKi.getSelectedMode()

    def set_KiMode(self, mode: PORISMode)-> PORISMode :
        return self.prKi.selectMode(mode)


    ## prParam ControlLoop 

    # KiDouble  
    def get_KiDouble(self)-> float :
        v = self.prKi.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_KiDouble(self, data: float)-> float :
        return self.prKi.getSelectedValue().setData(data)


    ## prParam Kp 

    # Kp
    def get_Kp(self)-> PORISValue :
        return self.prKp.getSelectedValue()

    def set_Kp(self, value: PORISValue)-> PORISValue :
        return self.prKp.setValue(value)


    ## KpMode 
    def get_KpMode(self)-> PORISMode:
        return self.prKp.getSelectedMode()

    def set_KpMode(self, mode: PORISMode)-> PORISMode :
        return self.prKp.selectMode(mode)


    ## prParam ControlLoop 

    # KpDouble  
    def get_KpDouble(self)-> float :
        v = self.prKp.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_KpDouble(self, data: float)-> float :
        return self.prKp.getSelectedValue().setData(data)


    ## SubtractorMode 
    def get_SubtractorMode(self)-> PORISMode:
        return self.sysSubtractor.getSelectedMode()

    def set_SubtractorMode(self, mode: PORISMode)-> PORISMode :
        return self.sysSubtractor.selectMode(mode)


    ## prParam Rate 

    # Rate
    def get_Rate(self)-> PORISValue :
        return self.prRate.getSelectedValue()

    def set_Rate(self, value: PORISValue)-> PORISValue :
        return self.prRate.setValue(value)


    ## RateMode 
    def get_RateMode(self)-> PORISMode:
        return self.prRate.getSelectedMode()

    def set_RateMode(self, mode: PORISMode)-> PORISMode :
        return self.prRate.selectMode(mode)


    ## prParam Subtractor 

    # RateDouble  
    def get_RateDouble(self)-> float :
        v = self.prRate.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_RateDouble(self, data: float)-> float :
        return self.prRate.getSelectedValue().setData(data)


    ## prParam SetPoint 

    # SetPoint
    def get_SetPoint(self)-> PORISValue :
        return self.prSetPoint.getSelectedValue()

    def set_SetPoint(self, value: PORISValue)-> PORISValue :
        return self.prSetPoint.setValue(value)


    ## SetPointMode 
    def get_SetPointMode(self)-> PORISMode:
        return self.prSetPoint.getSelectedMode()

    def set_SetPointMode(self, mode: PORISMode)-> PORISMode :
        return self.prSetPoint.selectMode(mode)


    ## prParam ControlBox 

    # SetPointDouble  
    def get_SetPointDouble(self)-> float :
        v = self.prSetPoint.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_SetPointDouble(self, data: float)-> float :
        return self.prSetPoint.getSelectedValue().setData(data)

