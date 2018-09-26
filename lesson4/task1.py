class Shop():
    """docstring for Shop"""
    def __init__(self, shop_name, store_type, number_of_units=0):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = number_of_units

    def describe_shop(self):
        print('The name of shop is:\n{}.\nThe type of shop is:\n{}.\n'.format(self.shop_name, self.store_type))

    def open_shop(self):
        print('The status of shop is OPEN\n')

    def set_number_of_units(self, amount_of_types=0):
        self.amount_of_types = amount_of_types


class Discount(Shop):
    def __init__(self, discount_products):
        self.discount_products = discount_products

    def get_discounts_products(self):
        print('This is a discount products: {}'.format(self.discount_products))


if __name__ == '__main__':
    shop1 = Shop('Forto', 'internet shop')
    shop2 = Shop('Amo', 'U now the kind of this shop')
    shop3 = Shop('Forco', 'Weapons for Humanity')
    shop1.open_shop()
    shop1.describe_shop()
    shop2.open_shop()
    shop2.describe_shop()
    shop3.open_shop()
    shop3.describe_shop()
    store = Shop('Monero', 'Trading market')
    print('The nmr of weapons in shop: {}'.format(store.number_of_units))
    print('Upgrade')
    store.number_of_units = 1000000
    store.set_number_of_units(amount_of_types=1)
    print('The nmr of weapons in shop: {}.\nThe amount of types of weapons is: {}'.format(store.number_of_units, store.amount_of_types))
    store_discount = Discount('ak-47')
    store4 = Discount('c', 'c', 'c')
    store_discount.get_discounts_products()
