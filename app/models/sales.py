from app.models.product import Product
from datetime import datetime


product_obj = Product()

class SaleRecord:
    """Model class for a sales record"""
    def __init__(self):
        self.all_Sales = []

    def create_sale_record(self, product, quantity, amount):
        """This method creates a sales record"""
        sale_record = dict(
            sale_id = len(self.all_Sales)+1,
            product = product,
            quantity = quantity,
            amount = amount,
            attendant = "attendants_name",
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        self.all_Sales.append(sale_record)
        return True

    def fetch_all_sales(self):
        """This method fetches all the available sales"""
        if len(self.all_Sales) > 0:
            return self.all_Sales
        return False