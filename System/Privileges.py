class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(f"User has next privileges:")
        print(f"".join(f"{privilege}\n" for privilege in self.privileges))