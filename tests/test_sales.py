from app.models.sales import SaleRecord
from tests.base_test import BaseTestCase
from flask import json

sales_obj = SaleRecord()
class TestSales(BaseTestCase):

    def test_creating_sale(self):
        """
        Test successful POST request to create a sale
        """
        response = self.app.post("/api/v1/sales",
            content_type='application/json',
            data=json.dumps(dict(product="Rice", quantity="20", amount="4000"),))

        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Sale record successfully created")
        self.assertEqual(response.status_code, 201)

    def test_fetching_sales(self):
        """
        Test successful GET request to
        fetch all sales
        """
        response = self.app.post("/api/v1/sales",
            content_type='application/json',
            data=json.dumps(dict(product="Rice", quantity="20", price="4000"),))

        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/sales",
        content_type='application/json',
            data=reply)
        reply = json.loads(response2.data.decode())
        self.assertEqual(response2.status_code, 200)
         
    def test_fetching_single_sale(self):
        """
        Test successful GET request to
        fetch a single sale
        """
        response = self.app.post("/api/v1/sales",
            content_type='application/json',
            data=json.dumps(dict(product="Rice", quantity="20", price="4000"),))

        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/sales/1",
        content_type='application/json',
            data=reply)
        reply = json.loads(response2.data.decode())
        self.assertEqual(response2.status_code, 200)

    def test_creating_sale_a_missing_product(self):
        """
        Test POST request to create no product
        """
        response = self.app.post("/api/v1/sales",
            content_type='application/json',
            data=json.dumps(dict(product=" ", quantity="20", amount="4000"),))

        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "product name is missing")
        self.assertEqual(response.status_code, 400)

    def test_creating_sale_missing_quantity(self):
        """
        Test successful POST request to create 
        a sale without quantity value
        """
        response = self.app.post("/api/v1/sales",
            content_type='application/json',
            data=json.dumps(dict(product="posho", quantity=" ", amount="4000"),))

        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "quantity should only be digits with no white spaces")
        self.assertEqual(response.status_code, 400)

    def test_creating_sale_with_quantity_spaces(self):
        """
        Test successful POST request to create a sale with quantity spaces
        """
        response = self.app.post("/api/v1/sales",
            content_type='application/json',
            data=json.dumps(dict(product="posho", quantity=" 20", amount="4000"),))

        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "quantity should only be digits with no white spaces")
        self.assertEqual(response.status_code, 400)

    def test_creating_sale_with_product_spaces(self):
        """
        Test successful POST request to create a sale with product spaces
        """
        response = self.app.post("/api/v1/sales",
            content_type='application/json',
            data=json.dumps(dict(product=" posho", quantity="20", amount="4000"),))

        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "product name should contain no white spaces")
        self.assertEqual(response.status_code, 400)

    def test_creating_sale_with_short_product_name(self):
        """
        Test successful POST request to create a sale with short product name
        """
        response = self.app.post("/api/v1/sales",
            content_type='application/json',
            data=json.dumps(dict(product="ph", quantity="20", amount="4000"),))

        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "product name should be more than 3 characters long")
        self.assertEqual(response.status_code, 400)

    def test_creating_sale_with_wrong_quantity(self):
        """
        Test successful POST request to create 
        a sale with wrong quantity
        """
        response = self.app.post("/api/v1/sales",
            content_type='application/json',
            data=json.dumps(dict(product="sugar", quantity="0", amount="4000"),))

        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "quantity should be at least 1 item")
        self.assertEqual(response.status_code, 400)

    def test_creating_sale_with_wrong_price(self):
        """
        Test successful POST request to create 
        a sale with wrong price
        """
        response = self.app.post("/api/v1/sales",
            content_type='application/json',
            data=json.dumps(dict(product="sugar", quantity="20", amount="0"),))

        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "price should be greater than zero")
        self.assertEqual(response.status_code, 400)  

    def test_creating_sale_with_missing_key(self):
        """
        Test successful POST request to create 
        a sale with some key missing
        """
        response = self.app.post("/api/v1/sales",
            content_type='application/json',
            data=json.dumps(dict(quantity="20", amount="0"),))

        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "You missed some key in your request body")
        self.assertEqual(response.status_code, 400)          

    def test_fetching_single_sale_with_no_proper_id(self):
        """
        Test GET request to fetch a single sale
        with no proper id
        """
        response = self.app.post("/api/v1/sales",
            content_type='application/json',
            data=json.dumps(dict(product="Rice", quantity="20", price="4000"),))

        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/sales/q",
        content_type='application/json',
            data=reply)
        reply2 = json.loads(response2.data.decode())
        self.assertEqual(reply2["message"], "Input should be an integer")
        self.assertEqual(response2.status_code, 400)

    def test_fetching_non_existing_single_sale(self):
        """
        Test GET request to fetch a sale
        that does not exist
        """
        response = self.app.post("/api/v1/sales",
            content_type='application/json',
            data=json.dumps(dict(product="Rice", quantity="20", price="4000"),))

        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/sales/12",
        content_type='application/json',
            data=reply)
        reply = json.loads(response2.data.decode())
        self.assertEqual(response2.status_code, 404)                