"""
	You may modify or reproduce.
	12:02:17 pm Monday
	05-11-2018
	mughalb9291@gmail.com
	Bugs and Criticisms are warmly welcome :) 
	(Improvements will be updated soon )
"""



#! /usr/bin/python3 /usr/bin/python

class Time(object):
    """Time class """

    def __init__( self ):
        self.hour = 0
        self.minute = 0
        self.second = 0


    def __init__( self, hour=0, minute=0, second=0 ):
        """ initilization """
        self.hour = hour
        self.minute = minute
        self.second = second
        self.__str__()
    
    def set_hour( self, hour ):
        self.hour = self.validate("hour",hour)

    def set_minute( self, minute ):
        self.minute = self.validate("minute",minute)

    def set_second( self, second ):
        self.second = self.validate("second",second)

    def get_hour( self ):
        return self.hour

    def get_minute( self ):
        return self.minute

    def get_second( self ):
        return self.second

    def fprint_time( self, is_standard = True ):
        if is_standard == True :
            am_or_pm = "AM" if self.hour < 12 else "PM"
            print("%02d:%02d:%02d %s"%( self.hour%12, self.minute, self.second, am_or_pm ))
        else:
            self.__str__() 

    def validate( self, name, value ):
        if name == "hour":
            if value < 0 or value > 23:
                self.raise_error( name, value )
        elif name == "minute":
            if value < 0 or value > 59:
                self.raise_error( name, value )
        elif name == "second":
            if value < 0 or value > 59:
                self.raise_error( name, value )
        else:
            print("Sorry, Attribute Name Was Not Good. {}".format( name ))
        return value 
    def raise_error(self,name,value):
        print("Sorry, Value Was not Good. {} -> {}".format(name.upper(),value))

    def __str__(self):
       return "%2d:%2d:%2d"%(self.hour,self.minute,self.second)
