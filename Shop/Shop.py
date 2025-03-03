class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0

    def describe_shop(self):
        print(f"Shop name: {self.shop_name} and store type "
              f"{self.store_type} and { self.number_of_units } number of units")

    def open_shop(self):
        print("Shop is open!")

    def show_number_of_units(self):
        print(f"Shop has {self.number_of_units} numbers of units")

    def set_number_of_units(self, units_value):
        self.number_of_units = units_value

    def increment_number_of_units(self, add_unit):
        self.number_of_units += add_unit

    def update_information(self):
        self.describe_shop()
        self.set_number_of_units(10)
        self.increment_number_of_units(2)
        self.describe_shop()
        self.open_shop()
