print(__file__)


# Set up default complex devices


class MonoEnergyMonitorDevice(Device):
    value = Cpt(EpicsSignalRO, "ENERGY_MON")
    setpoint = Cpt(EpicsSignal, "ENERGY_SP")


class OpticalAxisMonitorDevice(Device):
    value = Cpt(EpicsSignalRO, "P.RBV")
    low_limit_status = Cpt(EpicsSignalRO, "P_MLIM_STS")
    high_limit_status = Cpt(EpicsSignalRO, "P_PLIM_STS")
    axis_status = Cpt(EpicsSignalRO, "P_AXIS_STS")


mono_energy = MonoEnergyMonitorDevice("29idmono:", name="mono_energy")
mono_mirror = OpticalAxisMonitorDevice("29idmonoMIR:", name="mono_mirror")
mono_grt = OpticalAxisMonitorDevice("29idmonoGRT:", name="mono_grt")
mono_error_status = EpicsSignalRO(
    "29idmono:IL_ERR_STS", 
    name="mono_error_status")
