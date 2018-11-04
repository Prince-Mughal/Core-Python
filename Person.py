"""
	You may modify or reproduce.
	12:02:17 pm Monday
	05-11-2018
	mughalb9291@gmail.com
	Bugs and Criticisms are warmly welcome :) 
	(Improvements will be updated soon )
"""


#! /usr/bin/python3 /usr/bin/python


from Date import Date # User-Defined Date Class
from Name import Name # User-Defined Name Class

class Person(object):
    """ Person Information """
    def __init__( self, name = None, birth_date = None, death_date = None ):
        self.name = name
        self.birth_date = birth_date
        self.death_date = death_date

    def set_name( self, first_name, last_name ):
        self.name = Name( first_name, last_name )

    def set_birth_date( self, birth_day, birth_month, birth_year ):
        self.birth_date = Date( birth_date, birth_month, birth_year )

    def set_death_date( self, death_day, death_month, death_year ):
        self.death_date = Date( death_day, death_month, death_year )

    def get_name( self ):
        return self.name

    def get_birth_date( self ):
        return self.birth_date

    def get_death_date( self ):
        return self.death_date

    def __str__( self ):
        return "{}, {}, {}".format( self.name.__str__(), self.birth_date.__str__(), self.death_date.__str__() )
