import handlers
from decorators import parse_errors

@parse_errors
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(handlers.add_contact(args))
        elif command == "change":
            print(handlers.change_contact(args))
        elif command == "phone":
            print(handlers.get_contacts_phonenumber(args))
        elif command == "all":
            handlers.get_all_contacts()
        elif command == "add-birthday":
            print(handlers.add_birthday(args))
        elif command == "show-birthday":
            print(handlers.get_birthday(args))
        elif command == "birthdays":
            handlers.get_all_birthdays(args)
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()