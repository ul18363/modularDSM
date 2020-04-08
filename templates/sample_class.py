# -*- coding: utf-8 -*-
import numpy as np
    
def mult(a,b):
    return a*b
def sqr(a):
    return a*a
import sys
sys.path.insert(0,"C:/Users/Docker/Documents/UoB/Repository/")

import modularDSM.dependencies.sle.sle as sle
import modularDSM.dependencies.motor_interface.stepper_motor_interface as smi

class class_template():
    """Interface between python script and sensor"""

    def __init__(self,A=None,B=None):
        """
            oneD_sensor:
                1D sensor takes reading of a physical quantity and returns a scalar value "s".
                For now this value "s" will be a real number.
        """
        super(class_template, self).__init__()
        self.A=A
        self.B=B
		#self.arg = arg
    
    def set_measurement_function(self,fun):
        self.measuring_fun=fun
          
    def take_measurement(self,*args,**kwargs):
        self.measuring_fun(args,kwargs)
        print('Hi unknown '+self.__class__.__name__)
        return None
    
    def helloWorld(self):
        print('Hi unknown '+self.__class__.__name__)
        return None

    def give_me_those_locals(self,first,second,*args,**kwargs):
        print('Returning locals')
        return locals()
    
    def __get_my_objects__(self,show_hidden=False):
        my_vars=[a for a in dir(self) if (not a.startswith('__') or show_hidden)]
        print('my_vars')
        return my_vars
    
    def __print_me_those_variables__(self,*args,**kwargs):
        print('Returning locals')
        return locals()
    
    def __set_attribute__(self,attrname,value):
        """ setattr(object, attrname, value)"""
        setattr(self, attrname, value)
        return None
        
    def __get_attribute__(self,attrname):
        """getattr(object, attrname)"""
        attr=getattr(self, attrname)
        return attr

        
    def evaluate_B(self,*args,**kwargs):
        """getattr(object, attrname)"""
        if callable(self.B):
            output=self.B(*args,**kwargs)
            return output #locals()
        else:
            print('B is not callable')
        return None
    
if __name__ == "__main__":
    my_class=class_template()
    my_class.helloWorld()    
    x=my_class.__get_my_objects__()
#    my_locals=my_class.give_me_those_locals(2,3,4,5,a='b',c='d')
#    my_class.__set_attribute__('B',np.cos)#np.cos
#    c=my_class.evaluate_B(np.pi)
#    my_class.__set_attribute__('B',mult)
#    d=my_class.evaluate_B(2,3)
    my_class.__set_attribute__('B',np.array)
    c=my_class.evaluate_B([0], dtype='d')
    