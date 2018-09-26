from user import User


class Admin(User):
    privileges = ['Allowed to add message', 'Allowed to delete users', 'allowed to ban users']

    def __init__(self, first_name, last_name, login_attemps, privileges=privileges):
        super().__init__(first_name, last_name, login_attemps)
        self.privileges = privileges


class Privileges():
    def __init__(self, privileges=None):
        self.privileges = ['Allowed to add message', 'Allowed to delete users', 'allowed to ban users']

    def show_privileges(self):
        for e in self.privileges:
            print(e)
