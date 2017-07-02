class Underscore(object):
    def map(self, list, transformation):
        for val in list:
            transformation(val)
        return list
    def reduce(self, list):
        sum = 0
        for val in list:
            sum += val
        return sum
    def find(self, list, val_to_find):
        for val in list:
            if val == val_to_find:
                return val
        return None
    def filter(self, list, val_to_find):
        new_list = []
        for val in list:
            if val == val_to_find:
                new_list.append(val)
        return new_list
    def reject(self, list, val_to_avoid):
        new_list = []
        for val in list:
            if not (val == val_to_avoid):
                new_list.append(val)
        return new_list