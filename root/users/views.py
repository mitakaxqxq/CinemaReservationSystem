from .controllers import UserContoller


class UserViews:
    def __init__(self):
        self.controller = UserContoller()

    def login(self):
        pass

    def signup(self):
        username = input('Username: ')
        password = input('Password: ')

        self.controller.create_user(username=username, password=password)
