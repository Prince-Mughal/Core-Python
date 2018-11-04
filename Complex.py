"""
You may modify or reproduce.
Time: 11:56:17 pm Sunday
Date: 04-11-2018
Email: mughalb9291@gmail.com
Bugs and Criticisms are warmly welcome :) 
(Improvements will be updated soon )
 """


#! /usr/bin/python3 /usr/bin/python

class Complex(object):
    """ Complex Number Handler """
    def __init__( self, real_value = 0.0, imaginary_value = 0.0 ):
        self.real_value = real_value
        self.imaginary_value = imaginary_value

    def set_real_value( self, real_value ):
        self.real_value = real_value

    def set_imaginary_value( self, imaginary_value):
        self.imaginary_value = imaginary_value

    def get_real_value( self ):
        return self.real_value

    def get_imaginary_value( self ):
        return self.imaginary_value

    def __add__( self, other ):
        real = self.real_value + other.real_value
        imaginary = self.imaginary_value + other.imaginary_value    
        return Complex( real, imaginary )

    def __sub__( self, other ):
        real = self.real_value - other.real_value
        imaginary = self.imaginary_value - other.imaginary_value    
        return Complex( real, imaginary )

    def __str__( self ):
        return "({},{})".format( self.real_value, self.imaginary_value )
        
