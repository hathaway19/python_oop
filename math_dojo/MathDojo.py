# Part 1 MathDojo class
class MathDojo(object):
    def __init__(self):
        self.running_total = 0
    def add(self, num_1, num_2=0):
        self.running_total += num_1 + num_2
        return self
    def subtract(self, num_1, num_2=0):
        self.running_total -= (num_1 + num_2)
        return self
    def results(self):
        print self.running_total
        return self

class MathDojo_2(object):
    def __init__(self):
        self.running_total = 0
    def add(self, *args):
        # Look at all arguments passed in
        for i in args:
            # adds to running total if argument is just a float or an int
            if isinstance(i, int) or isinstance(i, float):
                self.running_total += i
            # if list or tuple, go through every value and subtract
            elif isinstance(i, list) or isinstance(i, tuple):
                # Goes through all numbers in list and adds it to running total
                for number in i:
                    self.running_total += number
        return self
    def subtract(self, *args):
        # Go through all arguments 
        for i in args:
            # if int or float, subtract from running total
            if isinstance(i, int) or isinstance(i, float):
                self.running_total -= i
            # if list or tuple, go through every value and subtract
            elif isinstance(i, list) or isinstance(i, tuple):
                for number in i:
                    self.running_total -= number
        return self
    # Print the value of the running total
    def results(self):
        print self.running_total
        return self

md = MathDojo_2().add([4,5,3],4,13, [2,4,5]).subtract([2,3,4],2.5,[9,8],(9,8)).results()