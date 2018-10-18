from app import app
from flask import request
from .models.product import Product

@app.route("/api/v1/products",methods=["POST"])
"""
Add the product route
"""
def add_product():
    add_product = Product(request.get_json())
    new_product = add_product.add_product()
    return new_product

@app.route("/api/v1/products", methods=["GET"])
"""This route for fetching all products"""
def fetch_all_products():
    all_products = Product.fetch_all_products()
    return all_products 



