import re
import string


def validate_username(username):
    smallcase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    numbers = string.digits
    available_symbols = list(smallcase_letters) + list(uppercase_letters) + list(numbers) + [' ']
    for character in username:
        if character not in available_symbols:
            raise ValueError(f'Username character {character} is not in allowed symbols!')


def validate_password(password):
    if len(password) < 8:
        raise ValueError('Password length must be at least 8 symbols!')
    special_symbols = re.compile("[@,!,#,$,%,^,&,*,(,),-,_]")
    capital_letters = re.compile("[A-Z]")
    if not capital_letters.search(password):
        raise ValueError('Password must contain at least 1 capital symbol!')
    if not special_symbols.search(password):
        raise ValueError('Password must contain at least 1 special symbol!')
