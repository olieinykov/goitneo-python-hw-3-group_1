from models import AddressBook, Record
from decorators import input_error

book = AddressBook()

@input_error
def add_contact(args):
    name, phone = args
    contact = Record(name)
    contact.add_phone(phone)
    book.add_record(contact)

    return f"Contact with name: '{name}' added."

@input_error
def change_contact(args):
    name, new_phone = args
    contact = book.find(name)

    if contact:
        contact.edit_phone(contact.phones[0], new_phone)
        return f"Phone number for contact '{name}' was updated to {new_phone}."
    else:
        return f"Contact {name} not found."

@input_error
def get_contacts_phonenumber(args):
    name = args[0]
    contact = book.find(name)
    if contact:
        return f"Phone number for '{name}' is {contact.phones[0]}"
    else:
        return f"Contact '{name}' not found."

@input_error
def get_all_contacts():
    for key, value in book.items():
        print(f"{key}, Phone:{value.phones[0]}, Birthday: {value.birthday}")

@input_error
def add_birthday(args):
    name, birthday = args
    contact = book.find(name)

    if contact:
        contact.add_birthday(birthday)
        return f"Birthday: {birthday} added to '{name}'"
    else:
        return f"Contact '{name}' not found."

@input_error
def get_birthday(args):
    name = args[0]
    contact = book.find(name)
    if contact is None:
        return f"Contact '{name}' not found."
    if contact.birthday:
        return contact.birthday
    else:
        return f"Birthday has not been added yet for {name}"


def get_all_birthdays(args):
    return book.get_birthdays_per_week()
