

class estimator():
    """Sensorimotor Law Encoder"""

    def __init__(self,i,S=None,M=None, arg):
        """
            The Encoder of the sensor i. 
        """
        super(estimator, self).__init__()
        self.comp_block_list= None
        self.S=S #Sensory State
        self.M=M #Motor Input
        self.dSi=None
        self.dSiPred=None
        self.arg = arg

    def set_S(self,S):
        self.S=S
        return None


class comp_block():
    """Sensorimotor Law Encoder"""

    def __init__(self,i,S=None,M=None, arg):
        """
            The Encoder of the sensor i. 
        """
        super(comp_block, self).__init__()
        self.i=i
        self.S=S #Sensory State
        self.M=M #Motor Input
        self.dSi=None
        self.dSiPred=None
        self.arg = arg

    def set_S(self,S):
        self.S=S
        return None
        
class saw_Node():