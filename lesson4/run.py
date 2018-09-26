from user import User
from admin_and_privileges import *

if __name__ == '__main__':
    user1 = User('Mark', 'Dark')
    user2 = User('Spark', 'Clark')
    user1.describe_user('user1')
    user1.greeting_user()
    user2.describe_user('user2')
    user2.greeting_user()
    login_attemp = User('Dark', 'Chark')
    login_attemp.increment_login_attemps()
    login_attemp.increment_login_attemps()
    login_attemp.increment_login_attemps()
    print(login_attemp.login_attemps)
    login_attemp.reset_login_attemps()
    print(login_attemp.login_attemps)
    admin = Admin('The', 'God', 0)
    admin = Privileges()
    admin.show_privileges()
