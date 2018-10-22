from app.models.product import Product
from tests.base_test import BaseTestCase
from flask import json

product_obj = Product()
class TestProducts(BaseTestCase):

    def test_add_product(self):
        response = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product="Rice", quantity="20", price="4000"),))

        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "product added successfully")
        self.assertEqual(response.status_code, 201)

    def test_add_existing_product(self):
        response = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product="Ricess", quantity="20", price="4000"),))
        response2 = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product="Rices", quantity="20", price="4000"),))    

        reply = json.loads(response2.data)
        self.assertEqual(reply["message"], "product added successfully")
        self.assertEqual(response2.status_code, 201)

    def test_add_product_with_no_name(self):
        response = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product=" ", quantity="20", price="4000"),))

        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "product name is missing")
        self.assertEqual(response.status_code, 400)

    def test_add_product_with_no_quantity(self):
        response = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product="rice", quantity=" ", price="4000"),))

        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "quantity must be only digits and must have no white spaces")
        self.assertEqual(response.status_code, 400)

    def test_add_product_with_no_price(self):
        response = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product="Ricess", quantity="20", price=" "),))

        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "price must be only digits and must have no white spaces")
        self.assertEqual(response.status_code, 400)

    def test_add_product_with_short_name(self):
        response = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product="rc", quantity="20", price="4000"),))

        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "product name should be more than 3 characters long")
        self.assertEqual(response.status_code, 400)

    def test_add_product_with_missing_key(self):
        response = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(quantity="20", price="4000"),))

        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "You missed some key in your request body")
        self.assertEqual(response.status_code, 400)        

    def test_add_product_with_no_price_2(self):
        response = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product="Ricess", quantity="20", price=""),))

        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "price is missing")
        self.assertEqual(response.status_code, 400)

    def test_fetching_products(self):
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
        response = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product="Rice", quantity="20", price="4000"),))

        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/products/1",
        content_type='application/json',
            data=reply)
        reply2 = json.loads(response2.data.decode())
        self.assertEqual(response2.status_code, 200)

    def test_fetching_not_exist_single_product(self):
        response = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product="Rice", quantity="20", price="4000"),))

        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/products/12",
        content_type='application/json',
            data=reply)
        reply2 = json.loads(response2.data.decode())
        self.assertEqual(response2.status_code, 404)    

    def test_fetching_single_product_with_impromper_id(self):
        response = self.app.post("/api/v1/products",
            content_type='application/json',
            data=json.dumps(dict(product="Rice", quantity="20", price="4000"),))

        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/products/q",
        content_type='application/json',
            data=reply)
        reply2 = json.loads(response2.data.decode())
        self.assertEqual(response2.status_code, 400)        
        


                  
    
              