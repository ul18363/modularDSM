# -*- coding: utf-8 -*-

class stepper_motor():
    """Sensorimotor Law Encoder"""

    def __init__(self,step=0,motor_commands={},name=None):
        """
            Interface for a stepper motor.
            Stepper motor have 2 possible motions:
                1- Go to a specific position
                2- Incrementally increase the step position
        """
        super(stepper_motor, self).__init__()
        self.step=step
        self.motor_commands=motor_commands
        self.name=name
		#self.arg = arg
        
    def named_helloWorld(self):
        if self.name:
            print('Hi '+self.__class__.__name__+": "+str(self.name))
        else:
            print('Hi unknown '+self.__class__.__name__)
        return None
    
    def helloWorld(self):
        print('Hi unknown '+self.__class__.__name__)
        return None
    
if __name__ == "__main__":
    my_stepper=stepper_motor()
    my_stepper.helloWorld()