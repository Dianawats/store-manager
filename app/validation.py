import re


class Validation:
    """
    validation class to add product.
    """
    
    def product_validation(self, product_name, quantity, price):
        """Method for product validation"""
        if not product_name:
            return "product name is missing"
        if product_name == " ":
            return "product name is missing"
        if not re.match(r"^([a-zA-Z]+[-_\s])*[a-zA-Z]+$", product_name):
            return "product name must have no white spaces"
        if not re.match(r"^[0-9]*$", quantity):
            return "quantity must be only digits and must have no white spaces"
        if not re.match(r"^[0-9]*$", price):
            return "price must be only digits and must have no white spaces"    
        if len(product_name) < 3:
            return "product name should be more than 3 characters long"
        if not quantity:
            return "quantity is missing"
        if quantity == " ":
            return "quantity is missing"
        if int(quantity) < 1:
            return "quantity should be at least 1 item"    
        if not price:
            return "price is missing"
        if int(price) < 1:
            return "price should be greater than zero"    
        if price == " ":
            return "price is missing"    
        
    def validate_input_type(self, input):
        try:
            _input = int(input)
        except ValueError:
            return "Input should be an interger"
             