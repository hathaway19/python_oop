# Animal Class (parent to Dog, Dragon, and Turtle classes)
class Animal(object):
    # Initialize variables
    def __init__(self, name, health):
        self.name = name
        self.health = health
    # Decreases health by 1
    def walk(self):
        self.health -= 1
        return self
    # Decreases health by 5
    def run(self):
        self.health -= 5
        return self
    # lists health of animal
    def display_health(self):
        print "Animal's health: ", self.health
        return self

# Dog Class (inherits from Animal class)
class Dog(Animal):
    def __init__(self, name, health=150):
        super(Dog, self).__init__(name, health)
        # Animal.__init__(self, name, health)
    # Dog has an unique class of getting pets 
    def pet(self):
        self.health += 5
        return self

# Dragon Class (inherits from Animal)
class Dragon(Animal):
    def __init__(self, name, health=170):
        Animal.__init__(self, name, health)
    # Unique method of Being able to fly
    def fly(self):
        self.health -= 10
        return self
    # Adds upon existing method in Animal by adding another print statement
    def display_health(self):
        super(Dragon, self).display_health()
        print "I am a Dragon"
        return self

# Turtle Class (inheriets from Animal)
class Turtle(Animal):
    def __init__(self, name, health=1000):
        super(Turtle, self).__init__(name, health)

print "dog"
doge = Dog("Lego").walk().walk().walk().run().run().pet().display_health()
print "dragon"
dragon = Dragon("nazgul").display_health()
print "turtle"
turtle = Turtle("Frodo").walk().display_health()