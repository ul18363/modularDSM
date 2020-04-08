# -*- coding: utf-8 -*-

import sys
sys.path.insert(0,"C:/Users/Docker/Documents/UoB/Repository/")

class simulated_motor_command_generator():
    """Interface between python script and sensor"""

    def __init__(self,A=None,B=None):
        """
            oneD_sensor:
                1D sensor takes reading of a physical quantity and returns a scalar value "s".
                For now this value "s" will be a real number.
        """
        super(simulated_motor_command_generator, self).__init__()
        self.A=A
        self.B=B
		#self.arg = arg# -*- coding: utf-8 -*-

