import sys
sys.path.insert(0,"C:/Users/Docker/Documents/UoB/Repository/")

import modularDSM.dependencies.sle.sle as sle

import dependencies.sle.sle          as sle

import dependencies.motor_interface  as mi
import dependencies.sensor_interface as si

"""
	A way to test the SLE algorithm could be to make it approximate the value of a function given a change in its domain.
	The value of the function would be the sensory input, and the change in the domain would be the motor command.
	 

	 The test would be like S=cos(x)
	 						M = dx

	 						output of SLE: cos(x+dx)-cos(x)
"""




#def main():
#	return None
#
#
#def function_generator():
#
#	return None
#
#
#
#if __name__ == "__main__":
#    main()