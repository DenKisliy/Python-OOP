from Shop.Shop import Shop

class Discount:
    def __init__(self, discount_products, shop):
        self.shop = shop
        self.discount_products = discount_products

    def get_discounts_products(self):
        print(f"Shop '{self.shop.shop_name}' has next discounts products:")
        print(f"".join(f"{product}\n" for product in self.discount_products))

    def add_discount_product(self, product):
        self.discount_products.append(product)

    def and_new_product_and_show_information(self):
        self.add_discount_product('jacket')
        self.get_discounts_products()