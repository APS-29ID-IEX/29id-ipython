print(__file__)

#m1 = EpicsMotor('xxx:m1', name='m1')
#m2 = EpicsMotor('xxx:m2', name='m2')
#m3 = EpicsMotor('xxx:m3', name='m3')
#m4 = EpicsMotor('xxx:m4', name='m4')
#m5 = EpicsMotor('xxx:m5', name='m5')
#m6 = EpicsMotor('xxx:m6', name='m6')
#m7 = EpicsMotor('xxx:m7', name='m7')
#m8 = EpicsMotor('xxx:m8', name='m8')

m1 = MyEpicsMotorWithDial('29idb:m1', name='m1')
m2 = MyEpicsMotorWithDial('29idb:m2', name='m2')

append_wa_motor_list(m1, m2)
