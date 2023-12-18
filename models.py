from collections import UserDict, defaultdict
from datetime import datetime, time
from utils import get_weekday
from decorators import InvalidPhone, InvalidBirthday

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        self.value = value


class Phone(Field):
    def __init__(self, value):
        if not self.validate_format(value):
            raise InvalidPhone()
        self.value = value

    def validate_format(self, value):
        return len(value) == 10


class Birthday(Field):
    def __init__(self, value):
        if not self.validate_format(value):
            raise InvalidBirthday()
        self.value = value

    def validate_format(self, value):
        try:
            return bool(datetime.strptime(value, '%d.%m.%Y'))
        except ValueError:
            return False

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, current_phone, new_phone):
        for idx, phone in enumerate(self.phones):
            if phone.value == current_phone:
                self.phones[idx] = Phone(new_phone)

    def delete_phone(self, current_phone):
        self.phones = [phone for phone in self.phones if phone.value != current_phone]

    def find_phone(self, current_phone):
        for phone in self.phones:
            if phone.value == current_phone:
                return phone


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_birthdays_per_week(self):
        result = defaultdict(list)
        today = datetime.today().date()
        current_date = datetime.combine(today, datetime.min.time())

        for name, values in self.data.items():
            if values.birthday:
                birthday = datetime.strptime(values.birthday.value, "%d.%m.%Y")
                birthday_this_year = birthday.replace(year=current_date.year)

                if birthday_this_year < current_date:
                    birthday_this_year = birthday.replace(year=current_date.year + 1)

                delta_days = (birthday_this_year - current_date).days

                if delta_days < 7:
                    weekday = get_weekday(birthday_this_year.weekday())
                    result[weekday].append(name)

        if len(result):
            for weekday, birthdays in result.items():
                print(f"{weekday}: {", ".join(birthdays)}")
        else:
            print('There is no birthday on this week')