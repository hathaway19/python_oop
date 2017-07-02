class Bike(object):
    # __init__ method to initialize variables for object
    def __init__(self, name, price, max_speed):
        # Get the values for price and max speed that are passed in
        self.price = price
        self.max_speed = max_speed
        self.name = name
        # Always initialize miles to 0 at beginning
        self.miles = 0
    # Displays info about bike
    def displayInfo(self):
        print "bike:", self.name
        print "The price of this bike is", self.price, " dollars"
        print "The maximum speed of this bike is", self.max_speed
        print "The total miles on this bike is", self.miles
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing"
        self.miles -= 5
        if self.miles < 0:
            self.miles = 0
        return self

# Bike 1
bike_1 = Bike("bike 1", 3.50, "1000mph")
bike_1.ride().ride().ride().reverse().displayInfo()

# Bike 2
bike_2 = Bike("bike 2", 1, "1mph")
bike_2.ride().ride().reverse().reverse().displayInfo()

# Bike 3
bike_3 = Bike("bike 3", 144.00, "12mph")
bike_3.reverse().reverse().reverse().displayInfo()