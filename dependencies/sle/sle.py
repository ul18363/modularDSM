

class SLE():
	"""Sensorimotor Law Encoder"""

	def __init__(self,i,S=None,M=None, arg):
		"""
			The Encoder of the sensor i. 
		"""
		super(SLE, self).__init__()
		self.i=i
		self.S=S #Sensory State
		self.M=M #Motor Input
		self.dSi=None
		self.dSiPred=None
		self.arg = arg

	def set_S(self,S):
		self.S=S
		return None

	def set_dSi(self,dSi):
		self.dSi=dSi
		return None	

	def set_M(self,M):
		self.S=S
		return None	

	def predict_dSi(self):
		dSiPred=None
		return dSiPred

	def predict_dS_of_Motor_n(self,kind='original'):
		"""
			In the original paper the SLE of the sensor i
		"""
		S=self.S
		M=self.M
		if kind =='original':
			dSiPred=self.original_predictor(S,M)

		return None

	def original_predictor(self,S,M):

		return None