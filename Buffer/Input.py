from Buffer.Buffer import Buffer

class BufferInput:
    def __init__(self):
        self.buffer = Buffer()

    def generate_input_list(self):
            element_list = input(f"Enter elements \n").split()
            num_list = []
            while len(element_list) > 0:
                try:
                    num_elem = float(element_list.pop(0))
                except ValueError:
                    return []
                num_list.append(num_elem)

            return num_list

    def run(self):
        while True:
            input_list = self.generate_input_list()
            if input_list:
                self.buffer.add(input_list)
            else:
                print("Not number. Exit")
                break
