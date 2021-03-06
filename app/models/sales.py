from app.models.product import Product
from datetime import datetime


class SaleRecord(object):
    """
    class that defines a sales object
    """
    
    def __init__(self):
        """ 
        This contructor initialises the sale record list that 
        contains all the attributes of that sale
        """

        self.all_Sales = []

    def create_sale_record(self, product, quantity, amount):
        """
        This method to creates a sales record
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

    def get_all_sales(self):
        """
        This method returns all the sales added in the list
        """
        if len(self.all_Sales) > 0:
            return self.all_Sales
        return False

    def get_single_sale(self, sale_id):
        """
        This method fetches a single sale
        """
        if len(self.all_Sales) > 0:
            try:
                SaleRecord = next(sale for sale in self.all_Sales if sale["sale_id"] == int(sale_id))
                return SaleRecord
            except Exception as err:
                return False    
        return False 
     

product_obj = Product()