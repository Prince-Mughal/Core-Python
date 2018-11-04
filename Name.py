"""
	You may modify or reproduce.
	12:02:17 pm Monday
	05-11-2018
	mughalb9291@gmail.com
	Bugs and Criticisms are warmly welcome :) 
	(Improvements will be updated soon )
"""

#! /usr/bin/python3 /usr/bin/python

class Name(object):

    def __init__( self, first_name = "NON", last_name = "NON" ):
        self.first_name = first_name
        self.last_name = last_name

    def set_first_name( self, first_name ):
        self.first_name = first_name

    def set_last_name( self, last_name ):
        self.last_name = last_name

    def get_first_name( self ):
        return self.first_name

    def get_last_name( self ):
        return self.last_name

    def __str__(self):
        return "{} {}".format( self.first_name, self.last_name )
