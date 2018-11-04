"""
	You may modify or reproduce.
	12:02:17 pm Monday
	05-11-2018
	mughalb9291@gmail.com
	Bugs and Criticisms are warmly welcome :) 
	(Improvements will be updated soon )
"""


#! /usr/bin/python3 /usr/bin/python

class Physical(object):

   #-Some Stati

   #-Initialization Method

    def __init__(self):
        self.name = "NON"
        self.age = -1
        self.height = 0.0
        self.weight = 0.0
        self.gender = "NON"
        self.eyes_color = "NON"
        self.teeth_color = "NON"
        self.hair_color = "NON"
        self.skin_color = "NON"

   #-Set Human Characteristics

    def set_name(self,name):
        self.name = name.upper()
 
    def set_age(self,age):
        self.age = age
    
    def set_height(self,height):
        self.height = height

    def set_weight(self,weight):
        self.weight = weight

    def set_gender(self,gender):
        self.gender = gender.upper()

    def set_eyes_color(self,eyes_color):
        self.eyes_color = eyes_color.upper()

    def set_teeth_color(self,teeth_color):
        self.teeth_color = teeth_color.upper()

    def set_hair_color(self,hair_color):
        self.hair_color = hair_color.upper()

    def set_skin_color(self,skin_color):
        self.skin_color = skin_color.upper()

   #-Get Human Characteristics
    
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight

    def get_gender(self):
        return self.gender

    def get_eyese_color(self):
        return self.eyese_color

    def get_teeth_color(self):
        return self.teeth_color

    def get_hair_color(self):
        return self.hair_color

    def get_skin_color(self):
        return self.skin_color

   #-Error Handler
        

   #-To String
  
    def __str__(self):
        return "{0} {1} {2} {3} {4} {5} {6} {7} {8} ".format(self.name,self.age,self.height,self.weight,\
self.gender,self.eyes_color,self.teeth_color,self.hair_color,self.skin_color)       



