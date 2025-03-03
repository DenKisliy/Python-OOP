BRACKET_DICT ={
    '{': '}',
    '(': ')',
    '[': ']'
}

class BracketChecker:
    def __init__(self):
        self.str_value = ''
        self.elem_list = []
        self.checker_list = []
        self.list_index_open = {}
        self.list_index_close = {}

    def find_elem_count(self, search_elem):
        count_of_elem = []
        for idx, elem in enumerate(self.elem_list):
            if elem == search_elem:
                count_of_elem.append(idx)

        return  count_of_elem

    def set_lists_index(self):
        self.list_index_open = {}
        self.list_index_close = {}

        for i in BRACKET_DICT:
            if len(self.find_elem_count(i)) > 0:
                self.list_index_open[i] = self.find_elem_count(i)

            if len(self.find_elem_count(BRACKET_DICT[i])) > 0:
                self.list_index_close[BRACKET_DICT[i]] = self.find_elem_count(BRACKET_DICT[i])

    def check_elem(self, elem_key, key_list):
        list_close = self.list_index_close.get(BRACKET_DICT.get(elem_key))

        if len(key_list) == len(list_close):
            for idx, elem in enumerate(key_list):
                check_value = list_close[idx] - elem
                if check_value == 1:
                    continue

                if not (check_value > -1 and (check_value - 1) % 2 == 0):
                    return False

        return True

    def check_base(self):
        if len(self.str_value) % 2 == 1:
            return False

        if len(self.list_index_open) != len(self.list_index_close):
            return False

        return True

    def check_correct_position_of_brackets(self, brackets_str):
        self.str_value = brackets_str
        self.elem_list = list(self.str_value)
        self.set_lists_index()

        if not self.check_base():
            return False

        for i in self.list_index_open:
            if not self.check_elem(i, self.list_index_open[i]):
                return False

        return True