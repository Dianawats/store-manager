class Product(object):
    """
    A class that defines product attributes
    """

    def __init__(self):
        self.all_products = []

    def add_product(self, product, quantity, price):
        """
        This method adds product item
        """
        product = dict(
                product_id = len(self.all_products) + 1,
                product = product,
                quantity = quantity,
                price = price
            )
        self.all_products.append(product)
        return self.all_products

    def get_all_products(self):
        """
        Method to fetch all available products
        """
        if len(self.all_products) > 0:
            return self.all_products
        return False

    def get_single_product(self, product_id):
        """
        Method to fetch a single product
        """
        if len(self.all_products) > 0:
            try:
                product = next(prod for prod in self.all_products if prod["product_id"] == int(product_id))
                return product
            except Exception as err:
                return False    
        return False
      