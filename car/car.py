class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage

        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
    def display_all(self):
        print "Price:", self.price
        print "Speed:", self.speed
        print "Fuel:", self.fuel
        print "Mileage:", self.mileage
        print "Tax:", self.tax

subaru = Car(1200, "60mph", "Full", 64)
tesla = Car(10000, "80mph", "Full", 12)
ferrari = Car(40000, "200mph", "Not Full", 0)
toyota = Car (12, "4", "Full", 1200)
prius = Car(-5000, "12mph", "Full", 40)
mustang = Car(9000, "120mph", "Not Full", 0)

print "subaru"
subaru.display_all()
print "tesla"
tesla.display_all()
print "ferrari"
ferrari.display_all()
print "toyota"
toyota.display_all()
print "prius"
prius.display_all()
print "mustang"
mustang.display_all()