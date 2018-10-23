from app.models.product import Product
from tests.base_test import BaseTestCase
from flask import json

product_obj = Product()
class TestProducts(BaseTestCase):

    def test_add_a_product(self):
        """
        Test POST request to add a product successfully
        """
        response = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product="Rice", quantity="20", price="4000"),))

        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "product added successfully")
        self.assertEqual(response.status_code, 201)

    def test_fetching_products(self):
        """
        Test GET request to fetch all products
        """
        response = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product="Rice", quantity="20", price="4000"),))

        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/products",
        content_type='application/json',
            data=reply)
        reply2 = json.loads(response2.data.decode())
        self.assertEqual(response2.status_code, 200)

    def test_fetching_single_product(self):
        """
        Test successful GET request to fetch a product by id
        """
        response = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product="Rice", quantity="20", price="4000"),))

        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/products/1",
        content_type='application/json',
            data=reply)
        reply2 = json.loads(response2.data.decode())
        self.assertEqual(response2.status_code, 200)

    def test_add_existing_product(self):
        """
        Test POST a product that exists
        """
        response = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product="Ricess", quantity="20", price="4000"),))
        response2 = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product="Ricess", quantity="20", price="4000"),))    

        reply = json.loads(response2.data)
        self.assertEqual(reply["message"], "The product inserted already exists, add a new product")
        self.assertEqual(response2.status_code, 409)

    def test_add_product_without_a_name(self):
        """
        Test POST request to add a product with no name
        """
        response = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product=" ", quantity="20", price="4000"),))

        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "product name is missing")
        self.assertEqual(response.status_code, 400)

    def test_add_product_without_quantity(self):
        """
        Test POST request to add a product with no quantity
        """
        response = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product="rice", quantity=" ", price="4000"),))

        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "quantity must be only digits and must have no white spaces")
        self.assertEqual(response.status_code, 400)

    def test_add_product_without_price(self):
        """
        Test POST request to add a product with no value
        """
        response = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product="Ricess", quantity="20", price=" "),))

        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "price must be only digits and must have no white spaces")
        self.assertEqual(response.status_code, 400)

    def test_fetching_none_exist_single_product(self):
        """
        Test GET request to fetch a product that doesnot exist
        """
        response = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product="Rice", quantity="20", price="4000"),))

        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/products/10",
        content_type='application/json',
            data=reply)
        reply2 = json.loads(response2.data.decode())
        self.assertEqual(response2.status_code, 404)    

    def test_fetching_single_product_with_no_proper_id(self):
        response = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product="Rice", quantity="20", price="4000"),))

        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/products/q",
        content_type='application/json',
            data=reply)
        reply2 = json.loads(response2.data.decode())
        self.assertEqual(response2.status_code, 400)        
        
    def test_add_product_with_short_name(self):
        """
        Test POST request to add a product with short name
        """
        response = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product="rc", quantity="20", price="4000"),))

        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "product name should be more than 3 characters long")
        self.assertEqual(response.status_code, 400)

    def test_add_product_with_missing_key(self):
        """
        Test POST request to add a product with the missing key
        """
        response = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(quantity="20", price="4000"),))

        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "You missed some key in your request body")
        self.assertEqual(response.status_code, 400)        

    def test_add_product_with_no_price_2(self):
        """
        Test POST request to add a product with no price
        """
        response = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product="Ricess", quantity="20", price=""),))

        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "price is missing")
        self.assertEqual(response.status_code, 400)

                  
    
              