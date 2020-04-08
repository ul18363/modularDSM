import sys
sys.path.insert(0,"C:/Users/Docker/Documents/UoB/Repository/")

import modularDSM.dependencies.sle.sle          as sle

import modularDSM.dependencies.motor_interface  as mi
import modularDSM.dependencies.sensor_interface.one_dimensional_sensor_interface as s1Di
import modularDSM.dependencies.motor_interface.stepper_motor_interface as stepperMi
import modularDSM.dependencies.motor_interface.dc_motor_interface as dcMi

"""
	A way to test the SLE algorithm could be to make it approximate the value of a function given a change in its domain.
	The value of the function would be the sensory input, and the change in the domain would be the motor command.
	 

	 The test would be like S=cos(x)
	 						M = dx

	 						output of SLE: cos(x+dx)-cos(x)
"""


####################################
#------     Define Motors    ------#
####################################

motor = stepperMi.stepper_motor()


####################################
#------     Define Mechanism    ------#
####################################

motor = stepperMi.stepper_motor()
####################################
#------    Define Sensors    ------#
####################################
# Sensors are independent of the motor and linked to the simulation to 
# take the measurement

sensor_x=s1Di.one_dimensional_sensor()
sensor_y=s1Di.one_dimensional_sensor()
sensor_theta=s1Di.one_dimensional_sensor()

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
#    main()# -*- coding: utf-8 -*-

