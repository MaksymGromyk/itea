class User():
    def __init__(self, first_name, last_name=None, login_attemps=0):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attemps = login_attemps

    def describe_user(self, name):
        print("{}, private info:\ncustomer's name is {} {}.\n".format(name, self.first_name, self.last_name))

    def greeting_user(self):
        print('Hello there, {}!\n'.format(self.first_name, self.last_name))

    def increment_login_attemps(self):
        self.login_attemps += 1

    def reset_login_attemps(self):
        self.login_attemps = 0
