import re

class UserModel:
    def __init__(self, *, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @staticmethod
    def validate(username, password):
        # TODO: Implement a validation -> Raise an error

        '''
        if len(password) < 8:
            raise ValueError("Password must be more than 8 symbols!")
        special_symbol = re.compile("[@,!,#,$,%,^,&,*,(,),-,_]")
        capital_letter = re.compile("[A-Z]")
        if not special_symbol.search(password):
            raise ValueError("Password must have one special symbol!")
        if not capital_letter.search(password):
            raise ValueError("Password must have one capital letter!")
        '''


#UserModel.validate('rrrr', 'aAde@rerrr')