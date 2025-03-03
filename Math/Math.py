class Math:
    def __init__(self):
        pass

    def calculate_value(self, number, pow):
        if pow == 0:
            return 1

        result = 1

        while pow != 0:
            if pow < 0:
                result = result / number
                pow += 1
            else:
                result = result * number
                pow -= 1

        return result


