class Product(object):
    """
    Product model class
    """
    def __init__(self, name, quantity, price, category):
         """
        constructor method for class
        :param product_id = 0:
        :param product_name:
        :param quantity:
        :param price:
        :param category:
        """
        self.id = 0; 
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category = category

    def jsonify(self):
        return {
            "id": self.id,
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price,
            "category": self.category
        }


class Sale(object):
