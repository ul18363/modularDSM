

class stepper_motor_simulator():
    """Stepper motor simulator:
        It incorporates physical elements to the stepper motor.
            As drag, minimum torque, offset, noise, dynamics of the motor.
            It keeps track of the state of the motor.
    """

    def __init__(self,timescale=None):
        """
            Interface for a stepper motor.
            Stepper motor have 2 possible motions:
                1- Go to a specific position
                2- Incrementally increase the step position
        """
        super(stepper_motor_simulator, self).__init__()
        self.timescale=timescale

    def set_timescale(self,timescale):
        self.timescale=timescale
        
    def helloWorld(self):
        print('Hi')
        return None

