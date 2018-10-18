from app.validation import Validation
from flask import jsonify

all_products=[]
validation = Validation()

class Product:
    """model class for a product"""
    def __init__(self, user_input):
        self.user_input = user_input

    def add_product(self):
        """Method for adding product item"""
        data = self.user_input
        search_keys = ("product_name", "quantity", "price")
        if all(key in data.keys() for key in search_keys):
            
            valid = validation.product_validation(data.get("product_name"), data.get("quantity"), data.get("price"))
            if valid:
                return jsonify({"message":valid}), 400
            product = dict(
                product_id = len(all_products) + 1,
                product_name = data.get("product_name"),
                quantity = data.get("quantity"),
                unit_price = data.get("price")
            )
            if any(d["product_name"] == data.get("product_name") for d in all_products):
                return jsonify({"message":"product already exists, update its quantity"}), 409       

            all_products.append(product)
            return jsonify({"message":"product successfully added", "products":all_products}), 201
        return jsonify({"message": "a 'key(s)' is missing in your request body"}), 400  

    @staticmethod
    def fetch_all_products():
        """get request method for all products"""
        if len(all_products) > 0:
            return jsonify({"All Products":all_products}), 200
        return jsonify({"message":"no products added yet"}), 404   

    