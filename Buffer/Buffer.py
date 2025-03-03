class Buffer:
    SIZE_OF_BUFFER = 5

    def __init__(self):
        self.buffer = []

    def add(self, a):
        while len(a) > 0:
            try:
                float(a[0])
            except ValueError:
                a.pop(0)
                continue

            self.buffer.append(float(a.pop(0)))
            if len(self.buffer) == Buffer.SIZE_OF_BUFFER:
                print(self.buffer)
                print(f"Sum of {Buffer.SIZE_OF_BUFFER} elements of buffer =  {self.calculate_element_of_buffer()}")

        print(self.buffer)

    def calculate_element_of_buffer(self):
        result = sum(self.buffer)
        self.buffer = []
        return result
