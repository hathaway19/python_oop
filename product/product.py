class Product(object):
    # Initialize class
    def __init__(self, price, item_name, weight, brand, cost, tax):
        # Change price based on tax
        self.price = self.add_tax(0.15, price)
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        # default status of for sale
        self.status = "for sale"
    # Method to set status of product to sold
    def sell(self):
        self.status = "sold"
        return self
    # Adds designated amount of tax to object
    def add_tax(self, tax, price):
        # Assumes user enters percentage, we have to add 100% or it goes down
        return price * (tax + 1.00)
    # Return product
    def return_product(self, reason_to_return):
        # Sets product to defective
        if reason_to_return == "defective":
            self.status = "defective"
            self.price = 0.00
        # Replaces object to be sold
        elif reason_to_return == "like new":
            self.status = "for sale"
        # Apply discount on used items
        elif reason_to_return == "used":
            self.status = "used"
            # Applly 20 percent discount
            self.price *= 0.80
        return self
    # Displays information on the given object
    def display_info(self):
        print "Item:", self.item_name
        print "Brand:", self.brand
        print "Price:", self.price
        print "Weight:", self.weight
        print "Cost:", self.cost
        print "Status:", self.status
        return self

# Test Case
nike = Product(25.00, "nike shield", "0.5 ounces", "nike", 5.50, 0.15)
nike.sell().return_product("used").display_info()