from PORIS import *

class tvPORIS:
    def __init__(self):
        idcounter = 1
        self.sysTV = PORISSys("TV")
        self.mdTVMode_UNKNOWN = PORISMode("TVMode_UNKNOWN")
        self.root = self.sysTV
        self.sysEntrada = PORISSys("Entrada")
        self.mdEntradaMode_UNKNOWN = PORISMode("EntradaMode_UNKNOWN")
        self.prAudio = PORISParam("Audio")
        self.mdAudioMode_UNKNOWN = PORISMode("AudioMode_UNKNOWN")
        self.vlAudio_UNKNOWN = PORISValue("Audio_UNKNOWN")
        self.sysAntena = PORISSys("Antena")
        self.mdAntenaMode_UNKNOWN = PORISMode("AntenaMode_UNKNOWN")
        self.prCanal = PORISParam("Canal")
        self.mdCanalMode_UNKNOWN = PORISMode("CanalMode_UNKNOWN")
        self.vlCanal_UNKNOWN = PORISValue("Canal_UNKNOWN")
        self.prBanda = PORISParam("Banda")
        self.mdBandaMode_UNKNOWN = PORISMode("BandaMode_UNKNOWN")
        self.vlBanda_UNKNOWN = PORISValue("Banda_UNKNOWN")
        self.mdTVMode_Antena = PORISMode("TVMode_Antena")
        self.mdTVMode_AV = PORISMode("TVMode_AV")
        self.mdEntradaMode_HDMI1 = PORISMode("EntradaMode_HDMI1")
        self.mdEntradaMode_HDMI2 = PORISMode("EntradaMode_HDMI2")
        self.mdEntradaMode_AUX = PORISMode("EntradaMode_AUX")
        self.mdEntradaMode_VGA = PORISMode("EntradaMode_VGA")
        self.vlAudio_Jack = PORISValue("Audio_Jack")
        self.vlAudio_RCA = PORISValue("Audio_RCA")
        self.mdAudioMode_Mode = PORISMode("AudioMode_Mode")
        self.vlCanal_Rango_Analogico = PORISValueFloat("Canal_Rango_Analogico")
        self.mdCanalMode_Digital = PORISMode("CanalMode_Digital")
        self.mdCanalMode_Analogico = PORISMode("CanalMode_Analogico")
        self.vlCanal_Rango_Digital = PORISValueFloat("Canal_Rango_Digital")
        self.vlBanda_UHF = PORISValue("Banda_UHF")
        self.vlBanda_VHF = PORISValue("Banda_VHF")
        self.mdBandaMode_Analogico = PORISMode("BandaMode_Analogico")
        self.mdAntenaMode_Digital = PORISMode("AntenaMode_Digital")
        self.mdAntenaMode_Analogico = PORISMode("AntenaMode_Analogico")
        self.mdTVMode_Engineering = PORISMode("TVMode_Engineering")
        self.mdEntradaMode_Engineering = PORISMode("EntradaMode_Engineering")
        self.mdAntenaMode_Engineering = PORISMode("AntenaMode_Engineering")

        self.sysTV.id = idcounter
        idcounter += 1
        self.sysTV.ident = "TV"
        self.sysTV.description = ""

        self.mdTVMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdTVMode_UNKNOWN.ident = "TVMode_UNKNOWN"
        self.mdTVMode_UNKNOWN.description = ""
        self.sysTV.addMode(self.mdTVMode_UNKNOWN)

        self.sysEntrada.id = idcounter
        idcounter += 1
        self.sysEntrada.ident = "Entrada"
        self.sysEntrada.description = ""
        self.sysTV.addSubsystem(self.sysEntrada)

        self.mdEntradaMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdEntradaMode_UNKNOWN.ident = "EntradaMode_UNKNOWN"
        self.mdEntradaMode_UNKNOWN.description = ""
        self.sysEntrada.addMode(self.mdEntradaMode_UNKNOWN)

        self.prAudio.id = idcounter
        idcounter += 1
        self.prAudio.ident = "Audio"
        self.prAudio.description = ""
        self.sysEntrada.addParam(self.prAudio)

        self.vlAudio_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlAudio_UNKNOWN.ident = "Audio_UNKNOWN"
        self.vlAudio_UNKNOWN.description = "Unknown value for Audio"
        self.prAudio.addValue(self.vlAudio_UNKNOWN)

        self.mdAudioMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdAudioMode_UNKNOWN.ident = "AudioMode_UNKNOWN"
        self.mdAudioMode_UNKNOWN.description = "Unknown mode for Audio"
        self.prAudio.addMode(self.mdAudioMode_UNKNOWN)
        self.mdAudioMode_UNKNOWN.addValue(self.vlAudio_UNKNOWN)
        self.mdEntradaMode_UNKNOWN.addSubMode(self.mdAudioMode_UNKNOWN)

        self.sysAntena.id = idcounter
        idcounter += 1
        self.sysAntena.ident = "Antena"
        self.sysAntena.description = ""
        self.sysTV.addSubsystem(self.sysAntena)

        self.mdAntenaMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdAntenaMode_UNKNOWN.ident = "AntenaMode_UNKNOWN"
        self.mdAntenaMode_UNKNOWN.description = ""
        self.sysAntena.addMode(self.mdAntenaMode_UNKNOWN)

        self.prCanal.id = idcounter
        idcounter += 1
        self.prCanal.ident = "Canal"
        self.prCanal.description = ""
        self.sysAntena.addParam(self.prCanal)

        self.vlCanal_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlCanal_UNKNOWN.ident = "Canal_UNKNOWN"
        self.vlCanal_UNKNOWN.description = "Unknown value for Canal"
        self.prCanal.addValue(self.vlCanal_UNKNOWN)

        self.mdCanalMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdCanalMode_UNKNOWN.ident = "CanalMode_UNKNOWN"
        self.mdCanalMode_UNKNOWN.description = "Unknown mode for Canal"
        self.prCanal.addMode(self.mdCanalMode_UNKNOWN)
        self.mdCanalMode_UNKNOWN.addValue(self.vlCanal_UNKNOWN)
        self.mdAntenaMode_UNKNOWN.addSubMode(self.mdCanalMode_UNKNOWN)

        self.prBanda.id = idcounter
        idcounter += 1
        self.prBanda.ident = "Banda"
        self.prBanda.description = ""
        self.sysAntena.addParam(self.prBanda)

        self.vlBanda_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlBanda_UNKNOWN.ident = "Banda_UNKNOWN"
        self.vlBanda_UNKNOWN.description = "Unknown value for Banda"
        self.prBanda.addValue(self.vlBanda_UNKNOWN)

        self.mdBandaMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdBandaMode_UNKNOWN.ident = "BandaMode_UNKNOWN"
        self.mdBandaMode_UNKNOWN.description = "Unknown mode for Banda"
        self.prBanda.addMode(self.mdBandaMode_UNKNOWN)
        self.mdBandaMode_UNKNOWN.addValue(self.vlBanda_UNKNOWN)
        self.mdAntenaMode_UNKNOWN.addSubMode(self.mdBandaMode_UNKNOWN)

        self.mdTVMode_Antena.id = idcounter
        idcounter += 1
        self.mdTVMode_Antena.ident = "TVMode_Antena"
        self.mdTVMode_Antena.description = ""
        self.sysTV.addMode(self.mdTVMode_Antena)

        self.mdTVMode_AV.id = idcounter
        idcounter += 1
        self.mdTVMode_AV.ident = "TVMode_AV"
        self.mdTVMode_AV.description = ""
        self.sysTV.addMode(self.mdTVMode_AV)

        self.mdEntradaMode_HDMI1.id = idcounter
        idcounter += 1
        self.mdEntradaMode_HDMI1.ident = "EntradaMode_HDMI1"
        self.mdEntradaMode_HDMI1.description = ""
        self.sysEntrada.addMode(self.mdEntradaMode_HDMI1)

        self.mdEntradaMode_HDMI2.id = idcounter
        idcounter += 1
        self.mdEntradaMode_HDMI2.ident = "EntradaMode_HDMI2"
        self.mdEntradaMode_HDMI2.description = ""
        self.sysEntrada.addMode(self.mdEntradaMode_HDMI2)

        self.mdEntradaMode_AUX.id = idcounter
        idcounter += 1
        self.mdEntradaMode_AUX.ident = "EntradaMode_AUX"
        self.mdEntradaMode_AUX.description = ""
        self.sysEntrada.addMode(self.mdEntradaMode_AUX)

        self.mdEntradaMode_VGA.id = idcounter
        idcounter += 1
        self.mdEntradaMode_VGA.ident = "EntradaMode_VGA"
        self.mdEntradaMode_VGA.description = ""
        self.sysEntrada.addMode(self.mdEntradaMode_VGA)

        self.vlAudio_Jack.id = idcounter
        idcounter += 1
        self.vlAudio_Jack.ident = "Audio_Jack"
        self.vlAudio_Jack.description = ""
        self.prAudio.addValue(self.vlAudio_Jack)

        self.vlAudio_RCA.id = idcounter
        idcounter += 1
        self.vlAudio_RCA.ident = "Audio_RCA"
        self.vlAudio_RCA.description = ""
        self.prAudio.addValue(self.vlAudio_RCA)

        self.mdAudioMode_Mode.id = idcounter
        idcounter += 1
        self.mdAudioMode_Mode.ident = "AudioMode_Mode"
        self.mdAudioMode_Mode.description = ""
        self.prAudio.addMode(self.mdAudioMode_Mode)

        self.vlCanal_Rango_Analogico.id = idcounter
        idcounter += 1
        self.vlCanal_Rango_Analogico.ident = "Canal_Rango_Analogico"
        self.vlCanal_Rango_Analogico.description = ""
        self.vlCanal_Rango_Analogico.min = 1
        self.vlCanal_Rango_Analogico.default_data = 1
        self.vlCanal_Rango_Analogico.max = 16
        self.prCanal.addValue(self.vlCanal_Rango_Analogico)

        self.mdCanalMode_Digital.id = idcounter
        idcounter += 1
        self.mdCanalMode_Digital.ident = "CanalMode_Digital"
        self.mdCanalMode_Digital.description = ""
        self.prCanal.addMode(self.mdCanalMode_Digital)

        self.mdCanalMode_Analogico.id = idcounter
        idcounter += 1
        self.mdCanalMode_Analogico.ident = "CanalMode_Analogico"
        self.mdCanalMode_Analogico.description = ""
        self.prCanal.addMode(self.mdCanalMode_Analogico)

        self.vlCanal_Rango_Digital.id = idcounter
        idcounter += 1
        self.vlCanal_Rango_Digital.ident = "Canal_Rango_Digital"
        self.vlCanal_Rango_Digital.description = ""
        self.vlCanal_Rango_Digital.min = 1
        self.vlCanal_Rango_Digital.default_data = 1
        self.vlCanal_Rango_Digital.max = 999
        self.prCanal.addValue(self.vlCanal_Rango_Digital)

        self.vlBanda_UHF.id = idcounter
        idcounter += 1
        self.vlBanda_UHF.ident = "Banda_UHF"
        self.vlBanda_UHF.description = ""
        self.prBanda.addValue(self.vlBanda_UHF)

        self.vlBanda_VHF.id = idcounter
        idcounter += 1
        self.vlBanda_VHF.ident = "Banda_VHF"
        self.vlBanda_VHF.description = ""
        self.prBanda.addValue(self.vlBanda_VHF)

        self.mdBandaMode_Analogico.id = idcounter
        idcounter += 1
        self.mdBandaMode_Analogico.ident = "BandaMode_Analogico"
        self.mdBandaMode_Analogico.description = ""
        self.prBanda.addMode(self.mdBandaMode_Analogico)

        self.mdAntenaMode_Digital.id = idcounter
        idcounter += 1
        self.mdAntenaMode_Digital.ident = "AntenaMode_Digital"
        self.mdAntenaMode_Digital.description = ""
        self.sysAntena.addMode(self.mdAntenaMode_Digital)

        self.mdAntenaMode_Analogico.id = idcounter
        idcounter += 1
        self.mdAntenaMode_Analogico.ident = "AntenaMode_Analogico"
        self.mdAntenaMode_Analogico.description = ""
        self.sysAntena.addMode(self.mdAntenaMode_Analogico)

        self.mdTVMode_Engineering.id = idcounter
        idcounter += 1
        self.mdTVMode_Engineering.ident = "TVMode_Engineering"
        self.mdTVMode_Engineering.description = "TV engineering mode"
        self.sysTV.addMode(self.mdTVMode_Engineering)

        self.mdEntradaMode_Engineering.id = idcounter
        idcounter += 1
        self.mdEntradaMode_Engineering.ident = "EntradaMode_Engineering"
        self.mdEntradaMode_Engineering.description = "Entrada engineering mode"
        self.sysEntrada.addMode(self.mdEntradaMode_Engineering)

        self.mdAntenaMode_Engineering.id = idcounter
        idcounter += 1
        self.mdAntenaMode_Engineering.ident = "AntenaMode_Engineering"
        self.mdAntenaMode_Engineering.description = "Antena engineering mode"
        self.sysAntena.addMode(self.mdAntenaMode_Engineering)
        # Marcamos EntradaMode_HDMI1 como elegible para TVMode_AV
        self.mdTVMode_AV.addSubMode(self.mdEntradaMode_HDMI1)
        # Marcamos EntradaMode_HDMI2 como elegible para TVMode_AV
        self.mdTVMode_AV.addSubMode(self.mdEntradaMode_HDMI2)
        # Marcamos EntradaMode_AUX como elegible para TVMode_AV
        self.mdTVMode_AV.addSubMode(self.mdEntradaMode_AUX)
        # Marcamos EntradaMode_VGA como elegible para TVMode_AV
        self.mdTVMode_AV.addSubMode(self.mdEntradaMode_VGA)
        # Marcamos EntradaMode_HDMI1 como elegible para TVMode_Engineering
        self.mdTVMode_Engineering.addSubMode(self.mdEntradaMode_HDMI1)
        # Marcamos EntradaMode_HDMI2 como elegible para TVMode_Engineering
        self.mdTVMode_Engineering.addSubMode(self.mdEntradaMode_HDMI2)
        # Marcamos EntradaMode_AUX como elegible para TVMode_Engineering
        self.mdTVMode_Engineering.addSubMode(self.mdEntradaMode_AUX)
        # Marcamos EntradaMode_VGA como elegible para TVMode_Engineering
        self.mdTVMode_Engineering.addSubMode(self.mdEntradaMode_VGA)
        # Marcamos EntradaMode_Engineering como elegible para TVMode_Engineering
        self.mdTVMode_Engineering.addSubMode(self.mdEntradaMode_Engineering)
        # Marcamos AudioMode_Mode como elegible para EntradaMode_AUX
        self.mdEntradaMode_AUX.addSubMode(self.mdAudioMode_Mode)
        # Marcamos AudioMode_Mode como elegible para EntradaMode_VGA
        self.mdEntradaMode_VGA.addSubMode(self.mdAudioMode_Mode)
        # Marcamos AudioMode_Mode como elegible para EntradaMode_Engineering
        self.mdEntradaMode_Engineering.addSubMode(self.mdAudioMode_Mode)
        # Marcamos Audio_Jack como elegible para AudioMode_Mode
        self.mdAudioMode_Mode.addValue(self.vlAudio_Jack)
        # Marcamos Audio_RCA como elegible para AudioMode_Mode
        self.mdAudioMode_Mode.addValue(self.vlAudio_RCA)
        # Marcamos AntenaMode_Analogico como elegible para TVMode_Antena
        self.mdTVMode_Antena.addSubMode(self.mdAntenaMode_Analogico)
        # Marcamos AntenaMode_Digital como elegible para TVMode_Antena
        self.mdTVMode_Antena.addSubMode(self.mdAntenaMode_Digital)
        # Marcamos AntenaMode_Digital como elegible para TVMode_Engineering
        self.mdTVMode_Engineering.addSubMode(self.mdAntenaMode_Digital)
        # Marcamos AntenaMode_Analogico como elegible para TVMode_Engineering
        self.mdTVMode_Engineering.addSubMode(self.mdAntenaMode_Analogico)
        # Marcamos AntenaMode_Engineering como elegible para TVMode_Engineering
        self.mdTVMode_Engineering.addSubMode(self.mdAntenaMode_Engineering)
        # Marcamos CanalMode_Digital como elegible para AntenaMode_Digital
        self.mdAntenaMode_Digital.addSubMode(self.mdCanalMode_Digital)
        # Marcamos CanalMode_Analogico como elegible para AntenaMode_Analogico
        self.mdAntenaMode_Analogico.addSubMode(self.mdCanalMode_Analogico)
        # Marcamos CanalMode_Digital como elegible para AntenaMode_Engineering
        self.mdAntenaMode_Engineering.addSubMode(self.mdCanalMode_Digital)
        # Marcamos CanalMode_Analogico como elegible para AntenaMode_Engineering
        self.mdAntenaMode_Engineering.addSubMode(self.mdCanalMode_Analogico)
        # Marcamos Canal_Rango_Digital como elegible para CanalMode_Digital
        self.mdCanalMode_Digital.addValue(self.vlCanal_Rango_Digital)
        # Marcamos Canal_Rango_Analogico como elegible para CanalMode_Analogico
        self.mdCanalMode_Analogico.addValue(self.vlCanal_Rango_Analogico)
        # Marcamos BandaMode_Analogico como elegible para AntenaMode_Analogico
        self.mdAntenaMode_Analogico.addSubMode(self.mdBandaMode_Analogico)
        # Marcamos BandaMode_Analogico como elegible para AntenaMode_Engineering
        self.mdAntenaMode_Engineering.addSubMode(self.mdBandaMode_Analogico)
        # Marcamos Banda_UHF como elegible para BandaMode_Analogico
        self.mdBandaMode_Analogico.addValue(self.vlBanda_UHF)
        # Marcamos Banda_VHF como elegible para BandaMode_Analogico
        self.mdBandaMode_Analogico.addValue(self.vlBanda_VHF)

    #----------------------------------------------------------------------
    #  Specific methods
    #----------------------------------------------------------------------


    ## TVMode 
    def get_TVMode(self)-> PORISMode:
        return self.sysTV.selectedMode

    def set_TVMode(self, mode: PORISMode)-> PORISMode :
        return self.sysTV.setMode(mode)


    ## EntradaMode 
    def get_EntradaMode(self)-> PORISMode:
        return self.sysEntrada.selectedMode

    def set_EntradaMode(self, mode: PORISMode)-> PORISMode :
        return self.sysEntrada.setMode(mode)


    ## prParam Audio 

    # Audio
    def get_Audio(self)-> PORISValue :
        return self.prAudio.selectedValue

    def set_Audio(self, value: PORISValue)-> PORISValue :
        return self.prAudio.setValue(value)


    ## AudioMode 
    def get_AudioMode(self)-> PORISMode:
        return self.prAudio.selectedMode

    def set_AudioMode(self, mode: PORISMode)-> PORISMode :
        return self.prAudio.setMode(mode)


    ## AntenaMode 
    def get_AntenaMode(self)-> PORISMode:
        return self.sysAntena.selectedMode

    def set_AntenaMode(self, mode: PORISMode)-> PORISMode :
        return self.sysAntena.setMode(mode)


    ## prParam Canal 

    # Canal
    def get_Canal(self)-> PORISValue :
        return self.prCanal.selectedValue

    def set_Canal(self, value: PORISValue)-> PORISValue :
        return self.prCanal.setValue(value)


    ## CanalMode 
    def get_CanalMode(self)-> PORISMode:
        return self.prCanal.selectedMode

    def set_CanalMode(self, mode: PORISMode)-> PORISMode :
        return self.prCanal.setMode(mode)


    ## prParam Antena 

    # CanalDouble  
    def get_CanalDouble(self)-> float :
        return self.prCanal.selectedValue.getData()

    def set_CanalDouble(self, data: float)-> float :
        return self.prCanal.selectedValue.setData(data)


    ## prParam Antena 

    # CanalDouble  
    def get_CanalDouble(self)-> float :
        return self.prCanal.selectedValue.getData()

    def set_CanalDouble(self, data: float)-> float :
        return self.prCanal.selectedValue.setData(data)


    ## prParam Banda 

    # Banda
    def get_Banda(self)-> PORISValue :
        return self.prBanda.selectedValue

    def set_Banda(self, value: PORISValue)-> PORISValue :
        return self.prBanda.setValue(value)


    ## BandaMode 
    def get_BandaMode(self)-> PORISMode:
        return self.prBanda.selectedMode

    def set_BandaMode(self, mode: PORISMode)-> PORISMode :
        return self.prBanda.setMode(mode)


    ## Action trigger TV_Apply ##
    def execTV_Apply(self, value: bool) -> bool:
        # Override this
        return True

