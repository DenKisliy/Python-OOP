import datetime

class User:
    def __init__(self, first_name, last_name, login, password):
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
        self.password = password
        self.registration_date = datetime.datetime.now()
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}")

    def greeting_user(self):
        print(f"Hello {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

