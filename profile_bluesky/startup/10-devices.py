print(__file__)

"""Set up default complex devices"""

from ophyd import Component, Device, DeviceStatus
from ophyd import EpicsMotor, EpicsScaler
from ophyd import EpicsSignal, EpicsSignalRO, EpicsSignalWithRBV
from ophyd import PVPositioner, PVPositionerPC
from APS_BlueSky_tools.devices import userCalcsDevice


class OpticalAxisMonitorDevice(Device):
    value = Component(EpicsSignalRO, "P.RBV")
    low_limit_status = Component(EpicsSignalRO, "P_MLIM_STS")
    high_limit_status = Component(EpicsSignalRO, "P_PLIM_STS")
    axis_status = Component(EpicsSignalRO, "P_AXIS_STS")


class EpicsMotorWithDial(EpicsMotor):
    dial = Component(EpicsSignal, ".DRBV", write_pv=".DVAL")
