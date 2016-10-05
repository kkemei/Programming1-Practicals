"""
CP1404/CP5632 Practical
Car class
"""
import random

class Car:
    """ represent a car object """

    def __init__(self, name="", fuel=0):
        """ initialise a Car instance """
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        return "{}, fuel={}, odo={}".format(self.name, self.fuel, self.odometer)

    def add_fuel(self, amount):
        """ add amount to the car's fuel"""
        self.fuel += amount

    def drive(self, distance):
        """ drive the car a given distance if it has enough fuel or drive until fuel runs out
        return the distance actually driven """
        if distance > self.fuel:
            distance_driven = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
            distance_driven = distance
        self.odometer += distance_driven
        return distance_driven


class Taxi(Car):
    """ specialised version of a Car that includes fare costs """

    def __init__(self, name, fuel):
        """ initialise a Taxi instance, based on parent class Car """
        super().__init__(name, fuel)
        self.price_per_km = 1.20
        self.current_fare_distance = 0

    def __str__(self):
        """ return a string representation like a car but with current fare distance"""
        return "{}, {}km on current fare, ${:.2f}/km".format(super().__str__(), self.current_fare_distance, self.price_per_km)

    def get_fare(self):
        """ get the price for the taxi trip """
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        """ begin a new fare """
        self.current_fare_distance = 0

    def drive(self, distance):
        """ drive like parent Car but calculate fare distance as well"""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven


class UnreliableCar(Car):
    def __init__(self, name, fuel):
        """ initialise a Taxi instance, based on parent class Car """
        super().__init__(name, fuel)
        self.reliability = float(40)
        self.odometer = 0

    def drive(self, distance):
        """ drive like parent Car but calculate fare distance as well"""
        chance = random.randint(0,100)
        if chance >= self.reliability:
            if distance > self.fuel:
                distance_driven = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
                distance_driven = distance
                return True
            self.odometer += distance_driven
            return distance_driven
        else:
            return False


class SilverServiceTaxi(Car):
    """ specialised version of a Car that includes fare costs """

    def __init__(self, name, fuel, fancy):
        """ initialise a Taxi instance, based on parent class Car """
        super().__init__(name, fuel)
        self.price_per_km = 1.20
        self.current_fare_distance = 0
        self.fanciness = fancy*self.price_per_km
        self.flagfall = float(4.50)
        self.fare = 0

    def __str__(self):
        """ return a string representation like a car but with current fare distance"""
        return "{}, {}km on current fare, ${:.2f}/km plus flagfall of ${:.2f} Price is ${:.2f}".format(super().__str__(), self.current_fare_distance, self.fanciness, self.flagfall, self.get_fare())

    def get_fare(self):
        """ get the price for the taxi trip """
        # return self.price_per_km * self.current_fare_distance
        return (self.fanciness * self.current_fare_distance) + self.flagfall


    def start_fare(self):
        """ begin a new fare """
        self.current_fare_distance = 0

    def drive(self, distance):
        """ drive like parent Car but calculate fare distance as well"""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        # self.fare = (self.fanciness * distance) + self.flagfall

        return distance_driven