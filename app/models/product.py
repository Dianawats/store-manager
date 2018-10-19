class Product(object):
    """Product Class model"""
    def __init__(self):
        self.all_products = []

    def add_product(self, product, quantity, price):
        """This method adds product item"""
        product = dict(
                product_id = len(self.all_products) + 1,
                product = product,
                quantity = quantity,
                price = price
            )
        self.all_products.append(product)
        return self.all_products

    def fetch_all_products(self):
        """This method fetches all available products"""
        if len(self.all_products) > 0:
            return self.all_products
        return False

    def fetch_single_product(self, product_id):
        """This method fetches a single product"""
        if len(self.all_products) > 0:
            for product in range(len(self.all_products)):
                if ((self.all_products[product]["product_id"]) == int(product_id)):
                    return self.all_products[product]
                return False    
        return False
      