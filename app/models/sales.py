from app.models.product import Product
from datetime import datetime


product_obj = Product()

class SaleRecord(object):
    """
    class that defines a sales object
    """
    
    def __init__(self):
        self.all_Sales = []

    def create_sale_record(self, product, quantity, amount):
        """
        Method to create a sales record
        """
        sale_record = dict(
            sale_id = len(self.all_Sales)+1,
            product = product,
            quantity = quantity,
            amount = amount,
            attendant = "attendant",
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        self.all_Sales.append(sale_record)
        return True

    def fetch_all_sales(self):
        """
        Method to fetch all available sales
        """
        if len(self.all_Sales) > 0:
            return self.all_Sales
        return False

    def fetch_single_sale(self, sale_id):
        """
        Method to fetch a single sale
        """
        if len(self.all_Sales) > 0:
            try:
                SaleRecord = next(sale for sale in self.all_Sales if sale["sale_id"] == int(sale_id))
                return SaleRecord
            except Exception as err:
                return False    
        return False  

