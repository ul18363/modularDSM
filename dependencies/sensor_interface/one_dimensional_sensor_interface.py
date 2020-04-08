# -*- coding: utf-8 -*-

class one_dimensional_sensor():
    """Interface between python script and sensor"""

    def __init__(self,initial_s=None,s_offset=0,name=None,log_readings=False,logger=None,measuring_fun=None):
        """
            oneD_sensor:
                1D sensor takes reading of a physical quantity and returns a scalar value "s".
                For now this value "s" will be a real number.
        """
        super(one_dimensional_sensor, self).__init__()
        self.s_offset=s_offset
        self.s=initial_s
        self.log_readings=log_readings
        self.logger=logger
        self.measuring_fun=measuring_fun
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

    def give_me_those_locals(self,*args,**kwargs):
        print('Returning locals')
        return locals()
    
    def print_me_those_variables(self,*args,**kwargs):
        print('Returning locals')
        return locals()
    
if __name__ == "__main__":
    my_class=one_dimensional_sensor()
    my_class.helloWorld()    