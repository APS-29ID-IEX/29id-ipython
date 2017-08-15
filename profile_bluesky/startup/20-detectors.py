print(__file__)

"""
This is a multi-line, multi-paragraph docstring

See what we mean?
"""

from ophyd import (EpicsScaler, EpicsSignal, EpicsSignalRO,
                   Device, DeviceStatus)
from ophyd import Component as Cpt

import time

## Beam Monitor Counts
#bs_bm2 = EpicsSignalRO('BL14B:Det:BM2', name='bs_bm2')
#noisy = EpicsSignalRO('xxx:userCalc1', name='noisy')
#scaler = EpicsScaler('xxx:scaler1', name='scaler')

aps_current = EpicsSignal("S:SRcurrentAI", name="aps_current")

# Current Amplifier (Keithley) - Beamline:
ca1 = EpicsSignalRO('29idb:ca1:read', name='ca1_b')
ca2 = EpicsSignalRO('29idb:ca2:read', name='ca2_b')
ca3 = EpicsSignalRO('29idb:ca3:read', name='ca3_b')
ca4 = EpicsSignalRO('29idb:ca4:read', name='ca4_b')
ca5 = EpicsSignalRO('29idb:ca5:read', name='ca5_b')
#ca6 = EpicsSignalRO('29idb:ca6:read', name='ca6_b')
#ca7 = EpicsSignalRO('29idb:ca7:read', name='ca7_b')
#ca8 = EpicsSignalRO('29idb:ca8:read', name='ca8_b')
#ca9 = EpicsSignalRO('29idb:ca9:read', name='ca9_b')
ca10 = EpicsSignalRO('29idb:ca10:read', name='ca10_b')
#ca11 = EpicsSignalRO('29idb:ca11:read', name='ca11_b')
ca12 = EpicsSignalRO('29idb:ca12:read', name='ca12_b')
ca13 = EpicsSignalRO('29idb:ca13:read', name='ca13_b')


# Current Amplifier (Keithley) - ARPES:

D_1 = EpicsSignalRO('29idb:ca15:read', name='D1')
TEY_C = EpicsSignalRO('29idc:ca1:read', name='TEY_C')
D_2 = EpicsSignalRO('29idc:ca2:read', name='D2')
EAV = EpicsSignalRO('29idcEAV:Stats1:Total_RBV', name='EAV')

# Current Amplifier (Keithley) - RSXS:

Mesh = EpicsSignalRO('29idb:ca14:read', name='Mesh')
#ca1_d = EpicsSignalRO('29idd:ca1:read', name='ca1_d')
TEY_D = EpicsSignalRO('29idd:ca2:read', name='TEY_D')
D_3 = EpicsSignalRO('29idd:ca3:read', name='D3')
D_4 = EpicsSignalRO('29idd:ca4:read', name='D4')

