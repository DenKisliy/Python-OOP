import copy

class Converter:
    ROMAN_NUMERAL_DICT = {
        'I': 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000,
    }
    MAX_COMBINE_OF_ONE_NUMBER = 3

    def __init__(self):
        pass

    def calculate_elem(self, roman_numer_str):
        numer = roman_numer_str[0]
        count_number = 0
        list_count = []

        for idx, elem in enumerate(roman_numer_str):
            if numer != elem:
                list_count.append([numer, count_number])
                numer = elem
                count_number = 1
            else:
                count_number += 1

            if idx == len(roman_numer_str) - 1:
                list_count.append([numer, count_number])
                return list_count

            if count_number == Converter.MAX_COMBINE_OF_ONE_NUMBER:
                list_count.append([numer, count_number])
                if len(roman_numer_str) == 3:
                    numer = ''
                else:
                    numer = roman_numer_str[idx + 1]
                count_number = 0

        return list_count

    def get_number_of_rom(self, rom_num):
        return Converter.ROMAN_NUMERAL_DICT.get(rom_num)

    def is_first_elem_smaller(self, first_elem, second_elem):
        return self.get_number_of_rom(first_elem) < self.get_number_of_rom(second_elem)

    def change_to_number(self, list_of_calculate_elem):
        list_of_calculate_elem_copy = copy.deepcopy(list_of_calculate_elem)
        list_of_number = []
        for idx, [rom_num, count] in enumerate(list_of_calculate_elem_copy):
            if rom_num != '':
                if count == Converter.MAX_COMBINE_OF_ONE_NUMBER:
                    list_of_number.append(self.get_number_of_rom(rom_num) * count)

                if idx < len(list_of_calculate_elem_copy) - 1:
                    if self.is_first_elem_smaller(rom_num, list_of_calculate_elem_copy[idx + 1][0]):
                        calculate_num = (self.get_number_of_rom(list_of_calculate_elem_copy[idx + 1][0]) * list_of_calculate_elem_copy[idx + 1][1] -
                                         self.get_number_of_rom(rom_num) * count)
                        list_of_calculate_elem_copy[idx][0] = ''
                        list_of_calculate_elem_copy[idx + 1][0] = ''
                        list_of_number.append(calculate_num)
                        continue
                    elif count != Converter.MAX_COMBINE_OF_ONE_NUMBER:
                        list_of_number.append(self.get_number_of_rom(rom_num) * count)
                else:
                    list_of_number.append(self.get_number_of_rom(rom_num) * count)

        return list_of_number

    def converter(self, roman_numer_str):
        list_count = self.calculate_elem(roman_numer_str)
        list_of_number = self.change_to_number(list_count)
        return sum(list_of_number)

