import re

class Validation:
    """validates product and return appropriate message"""

    def product_validation(self, product_name, quantity, price):
        if not product_name:
            return "product_name is missing"
        if product_name == " ":
            return "product_name is missing"
        if not re.match(r"^([a-zA-Z]+\s)*[a-zA-Z]+$", product_name):
            return "product_name must have no white spaces"
        if not re.match(r"^[0-9]*$", quantity):
            return "quantity must be only digits and must have no white spaces"
        if not re.match(r"^[0-9]*$", price):
            return "price must be only digits and must have no white spaces"    
        if len(product_name) < 4:
            return "product_name should be more than 6 characters long"
        if not quantity:
            return "quantity is missing"
        if quantity == " ":
            return "quantity is missing"
        if quantity < 1:
            return "quantity should be at least 1 item"    
        if not price:
            return "price is missing"
        if price < 1:
            return "price should be greater than zero"    
        if price == " ":
            return "price is missing"    
        
    def validate_input_type(self, input):
        try:
            _input = int(input)
        except ValueError:
            return "Input should be an interger"

    def validate_quantity(self, quantity):
        if not re.match(r"^[0-9]*$", quantity):
            return "quantity must be only digits and must have no white spaces"
        if not quantity:
            return "quantity is missing"    
        if quantity == " ":
            return "quantity is missing"
        if int(quantity) < 1:
            return "quantity should be at least 1 item"   