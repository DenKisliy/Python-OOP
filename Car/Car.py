class Car:
    def __init__(self, mark, model, year):
        self.mark = mark
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed >= 5:
            self.speed -= 5

    def get_speed(self):
        return self.speed

    def update_speed(self):
        count = 0
        while count < 5:
            self.accelerate()
            print(self.get_speed())
            count += 1

        while count > 0:
            self.brake()
            print(self.get_speed())
            count -= 1