import hashlib
from .validations import validate_username, validate_password


class UserModel:
    def __init__(self, *, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @staticmethod
    def validate(username, password):
        validate_username(username)
        validate_password(password)

    @staticmethod
    def hash_password(password):
        password = hashlib.sha256(password.encode("utf-8")).hexdigest()
        return password

#print(UserModel(id=1, username='rrrr', password='aAde@rerrr').hash_password('aAde@rerrr'))
