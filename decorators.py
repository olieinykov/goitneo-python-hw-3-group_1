class InvalidPhone(Exception):
    pass

class InvalidBirthday(Exception):
    pass

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone or birthday please."
        except KeyError:
            return "User with such number not exist."
        except IndexError:
            return "User with such number or name not exist"
        except InvalidPhone:
            return "Invalid phone number format. Valid number contains 10 digits"
        except InvalidBirthday:
            return "Invalid birthday format. Please use DD.MM.YYYY"

    return inner

def parse_errors(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Please make sure command is correct"

    return inner