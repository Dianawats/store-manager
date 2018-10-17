from datetime import datetime

class Product(object):
    """
    Product model class
    """
    def __init__(self, name, quantity, price):
        """
        constructor method for class
        :param product_id = 0:
        :param product_name:
        :param quantity:
        :param price:
        """
        self.id = 0 
        self.name = name
        self.quantity = quantity
        self.price = price
        Product = []

    def jsonify(self):
        return {
            "id": self.id,
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price
        }


class Sale(object):
    def __init__(self,sales_id, name, quantity_sold, amount):
        self.id = sales_id
        self.name = name
        self.quantity_sold = quantity_sold
        self.amount = amount
        self.date = datetime

    def jsonify(self):
        return {
            "id": self.sales_id,
            "name": self.name,
            "quantity_sold": self.quantity_sold,
            "amount": self.amount,
            "date": self.datetime
        }
