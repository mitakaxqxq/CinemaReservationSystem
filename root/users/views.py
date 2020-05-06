from .controllers import UserContoller


class UserViews:
    def __init__(self):
        self.controller = UserContoller()

    def login(self):
        username = input('Username: ')
        password = input('Password: ')

        return self.controller.login_user(username=username, password=password)

    def signup(self):
        username = input('Username: ')
        password = input('Password: ')

        return self.controller.create_user(username=username, password=password)
