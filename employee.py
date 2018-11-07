#! /usr/bin/python3 /usr/bin/python

"""
	You may modify or reproduce.
	11:30:17 pm Wednesday
	07-11-2018
	mughalb9291@gmail.com
	Bugs and Criticisms are warmly welcome :) 
	(Improvements will be updated soon )
"""

class Employee(object):
    """ Employee Management """
    def __init__( self, first_name = "NON", last_name = "NON" ):
        if self.__class__ == Employee:
            raise NotImplementedError,"Sorry, Cannot Instantiate."
        self.first_name = first_name
        self.last_name = last_name

    def set_first_name( self, first_name):
        self.first_name = first_name

    def set_last_name( self, last_name):
        self.last_name = last_name

    def get_first_name( self ):
        return self.first_name

    def get_last_name( self ):
        return self.last_name

    def _validate( self, value ):
        """ Utility Method """
        if value < 0:
            raise ValueError,"Sorry, Value was not Good."
        else:
            return value

    def earnings( self ): 
        """ Abstract Method """
        raise NotImplementedError,"Sorry, Cannot Call Abstract method."

    def __str__( self ):
        return "{0} {1}".format( self.first_name, self.last_name )


class HourlyWorker(Employee):
    """ hourly Employee """
    def __init__( self, first, last , hours = 0.0, wage = 0.0 ):
        Employee.__init__( self, first, last )
        self.hours = self._validate( hours )
        self.wage = self._validate( wage )

    def set_hours( self, hours ):
        self.hours = self._validate( hours )

    def set_wage( self, wage ):
        self.wage = self._validate( wage )

    def get_hours( self ):
        return self.hours

    def get_wage( self ):
        return self.wage

    def earnings( self ):
        return self.hours * self.wage

    def __str__( self ):
        return "{0} ${1} ".format( Employee.__str__( self ), self.earnings() )

class PieceWorker(Employee):
    """ PieceWorker Employee """
    def __init__( self, first, last , wage_per_piece = 0.0, quantity = 0.0 ):
        Employee.__init__( self, first, last )
        self.wage_per_piece = self._validate( wage_per_piece )
        self.quantity = self._validate( quantity )

    def set_wage_per_piece( self, wage_per_piece ):
        self.wage_per_piece = self._validate( wage_per_piece )

    def set_quantity( self, quantity ):
        self.quantity = self._validate( quantity )

    def get_wage_per_piece( self ):
        return self.wage_per_piece

    def get_quantity( self ):
        return self.quantity

    def earnings( self ):
        return self.wage_per_piece * self.quantity

    def __str__( self ):
        return "{0} ${1} ".format( Employee.__str__( self ), self.earnings() )

class CommissionWorker(Employee):
    """ CommissionWorker Employee """
    def __init__( self, first, last , base_salary = 0.0, commission = 0.0, quantity = 0.0 ):
        Employee.__init__( self, first, last )
        self.base_salary = self._validate( base_salary )
        self.commission = self._validate( commission )
        self.quantity = self._validate( quantity )

    def set_base_salary( self, base_salary ):
        self.base_salary = self._validate( base_salary )

    def set_quantity( self, quantity ):
        self.quantity = self._validate( quantity )

    def set_commission( self, commission ):
        self.commission = self._validate( commission )

    def get_base_salary( self ):
        return self.base_salary

    def get_quantity( self ):
        return self.quantity

    def get_commission( self ):
        return self.commission

    def earnings( self ):
        return self.base_salary + self.commission * self.quantity

    def __str__( self ):
        return "{0} ${1} ".format( Employee.__str__( self ), self.earnings() )

class Boss(Employee):
    """ Boss Employee """
    def __init__( self, first, last , weekly_salary = 0.0 ):
        Employee.__init__( self, first, last )
        self.weekly_salary = self._validate( weekly_salary )

    def set_weekly_salary( self, weekly_salary ):
        self.weekly_salary = self._validate( weekly_salary )


    def get_weekly_salary( self ):
        return self.wage

    def earnings( self ):
        return self.weekly_salary

    def __str__( self ):
        return "{0} ${1} ".format( Employee.__str__( self ), self.earnings() )























