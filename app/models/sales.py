from app.models.product import Product
from datetime import datetime


product_obj = Product()

class SaleRecord:
    "Model class for a sales_record"
    def __init__(self):
        self.all_Sales = []

    def create_sale_record(self, product, quantity, amount):
        """Method to create a sales record"""
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
        """Method to fetch all available sales"""
        if len(self.all_Sales) > 0:
            return self.all_Sales
        return False

    def fetch_single_sale(self, sale_id):
        """Method to fetch a single sale"""
        if len(self.all_Sales) > 0:
            for sale in range(len(self.all_Sales)):
                if ((self.all_Sales[sale]["sale_id"]) == int(sale_id)):
                    return self.all_Sales[sale]
                return False    
        return False    

