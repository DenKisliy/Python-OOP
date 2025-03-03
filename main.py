from Figures import Figures
from Shop import Shop
from Shop import Discount
from Bank import Bank
from System.Admin import Admin
from Coin.Coin import Coin
from Car.Car import Car
from MoneyBox.MoneyBox import MoneyBox
from Pets.Pets import Pets
from Buffer.Input import BufferInput
from Exception.StrLengthException import *
# from Animals.InputAnimals import *
from Math.Math import Math
from RomanNumeralConverter.Converter import *
from BracketChecker.BracketChecker import *

# figures = Figures()
# figures.run()

# shop = Shop("Shop - 1", "clothes")
# shop.update_information()
#
# discount = Discount(['shirt', 'jeans'], shop)
# discount.and_new_product_and_show_information()

# bank = Bank(1000)
# bank.update_information()

# admin = Admin('Denis', 'Kisliy', 'saturn01', 'secret_word',
#               ["Allowed to add message", "Allowed to delete users", "Allowed to ban users"])
# admin.print_info()

# coin = Coin()
# coin.toss(10)

# car = Car('Honda', 'XP5', 2020)
# car.update_speed()

# def money_box_data_input(show_text):
#     while True:
#         try:
#             return int(input(show_text))
#         except ValueError:
#             print("Enter number")
#
# n = money_box_data_input(f"Enter size of money box\n")
# m = money_box_data_input(f"Enter count of money in the box\n")
# k = money_box_data_input(f"Enter count of money want to put\n")
#
# money_box = MoneyBox(n)
# print(money_box.add(k))

# pets = Pets()
# pets.pets_info()
#
# bufferInput = BufferInput()
# bufferInput.run()

# try:
#     result = check_len("CheckText01")
# except StrLengthException as e:
#     print(e)
#
# try:
#     result = check_len("CheckText")
# except StrLengthException as e:
#     print(e)

# math = Math()
# print(math.calculate_value(2, -3))
# print(math.calculate_value(2, 6))
# print(math.calculate_value(81, 0))

# converter = Converter()
# print(converter.converter('MMMCMLXXVI'))
# print(converter.converter('MMCMLXXVI'))
# print(converter.converter('LLL'))
# print(converter.converter('IX'))

checker = BracketChecker()
print(checker.check_correct_position_of_brackets('(){}[]'))
print(checker.check_correct_position_of_brackets('()(()}'))
print(checker.check_correct_position_of_brackets('(][)'))
print(checker.check_correct_position_of_brackets('()'))