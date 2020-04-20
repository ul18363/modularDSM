# -*- coding: utf-8 -*-

class dc_motor():
    """Sensorimotor Law Encoder"""

    def __init__(self,voltage=0,offset_voltage=0,motor_commands={}):
        """
            Interface for a dc motor.
            DC motors interface only have 1 possible behaviour:
                1- Set voltage at some level.
        """
        super(dc_motor, self).__init__()
        self.motor_commands=motor_commands
        self.offset_voltage=offset_voltage
        self.voltage=voltage
        
    def set_voltage(self,voltage):
        self.voltage=voltage
        
    def named_helloWorld(self):
        if self.name:
            print('Hi '+self.__class__.__name__+": "+str(self.name))
        else:
            print('Hi unknown '+self.__class__.__name__)
        return None
    
    def helloWorld(self):
        print('Hi unknown '+self.__class__.__name__)
        return None
