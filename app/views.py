from app import app
from flask import request
from .models.product import Product
from .models.sales import SaleRecord
from app.validation import Validation

product_object = Product()
sale_object = SaleRecord()
validation_object = Validation()

@app.route("/api/v1/products",methods=["POST"])
"""Add the product route"""
def add_product():
    add_product = Product(request.get_json())
    new_product = add_product.add_product()
    return new_product

@app.route("/api/v1/products", methods=["GET"])
"""This route for fetching all products"""
def fetch_all_products():
    all_products = Product.fetch_all_products()
    return all_products 

@app.route("/api/v1/products/<product_id>", methods=["GET"])
"""route for a single product"""
def fetch_single_product(product_id):
    valid = validation.validate_input_type(product_id)
    if valid:
        return jsonify({"message":valid}), 400
    product = Product(product_id)
    single_product = product.fetch_single_product()
    return single_product

@app.route("/api/v1/sales", methods=["POST"])
"""routes for adding sales record"""
def create_sales_record():
    data = request.get_json()
    search_keys = ( "product","quantity", "amount")
    if all(key in data.keys() for key in search_keys):
        product = data.get("product")
        quantity = data.get("quantity")
        amount = data.get("amount")

        invalid_values = validation_obj.product_validation(product, quantity, amount)
        if invalid_values:
            return jsonify({"message":invalid_values}), 400
        if (sale_obj.create_sale_record(product, quantity, amount)):
            return jsonify({"message":"Sale record successfully created", "Sales":sale_obj.all_Sales}), 201
        else:
            return jsonify({"message":"sale record not created or no products added yet"}), 400
    else:
        return jsonify({"message": "a 'key(s)' is missing in your request body"}), 400

@app.route("/api/v1/sales", methods=["GET"])
"""route for fetching all sales"""
def fetch_all_sales():
    all_sales = sale_obj.fetch_all_sales()
    if all_sales:
        return jsonify({"All Sales":sale_obj.all_Sales}), 200
    return jsonify({"message":"no sales created yet"}), 404  




