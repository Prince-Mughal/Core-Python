"""
	You may modify or reproduce.
	11:56:17 pm Sunday
	04-11-2018
	mughalb9291@gmail.com
	Bugs and Criticisms are warmly welcome :) 
	(Improvements will be updated soon )
"""
#! /usr/bin/python3 /usr/bin/python

class Date(object):
    """ Date Implementation """
    DAY_IN_MONTH = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


    def __init__( self, day, month, year ):
        self.day = day
        self.month = month
        self.year = year
        self.set_date( day, month, year )

    def set_date( self, day, month, year):
        self.set_day( day )
        self.set_month( month)
        self.set_year( year )

    def set_day( self, day):
        self.day = self.validate("day", day)

    def set_month( self, month):
        self.month = self.validate("month", month)

    def set_year( self, year):
        self.year = self.validate("year", year)

    def get_day( self ):
        return self.day

    def get_month( self ):
        return self.month

    def get_year( self ):
        return self.year

    def validate( self, name, value ):
        if name == "day":
            if self.validate_day(value):
                self.raise_error( name, value )
        elif name == "month":
            if value > 12 or value < 0:
                self.raise_error( name, value )
        elif name == "year":
            if value < 0:
                self.raise_error( name, value )
        else:
            print("Sorry, Attribute Name Was Not Good. {}".format( name ))
        return value 

    def validate_day( self, value ):
        if value <= Date.DAY_IN_MONTH[self.month]:
            return False
        else:
            return True 

    def raise_error( self, name, value ):
        print("Sorry, Value Was not Good. {} -> {}".format(name.upper(),value))

    def __str__(self):
       return "%02d:%02d:%04d"%( self.day, self.month, self.year)
        
