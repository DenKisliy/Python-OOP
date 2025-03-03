from System.User import User
from System.Privileges import Privileges

class Admin(User):
    def __init__(self, first_name, last_name, login, password, privileges):
        super().__init__(first_name, last_name, login, password)
        self.privileges = Privileges(privileges)

    def print_info(self):
        super().greeting_user()
        self.privileges.show_privileges()

