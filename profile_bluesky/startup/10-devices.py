print(__file__)

"""Set up default complex devices"""

from ophyd import Component, Device, DeviceStatus
from ophyd import EpicsMotor, EpicsScaler
from ophyd import EpicsSignal, EpicsSignalRO, EpicsSignalWithRBV
from ophyd import PVPositioner, PVPositionerPC
from APS_BlueSky_tools.devices import userCalcsDevice


class OpticalAxisMonitorDevice(Device):
    """ documentation """
    value = Component(EpicsSignalRO, "P.RBV")
    low_limit_status = Component(EpicsSignalRO, "P_MLIM_STS")
    high_limit_status = Component(EpicsSignalRO, "P_PLIM_STS")
    axis_status = Component(EpicsSignalRO, "P_AXIS_STS")


class EpicsMotorWithDial(EpicsMotor):
    """
    add motor record's dial coordinates to EpicsMotor
    
    USAGE::
    
        m1 = EpicsMotorWithDial('xxx:m1', name='m1')
    
    """
    dial = Component(EpicsSignal, ".DRBV", write_pv=".DVAL")
