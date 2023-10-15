def main():
    contacts = {}
    print("Welcome to the assistant bot created by Kostiantyn Klymenko!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = user_input.split()

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command.lower() == "hello":
            print("How can I help you?")
        elif command.lower() == "add":
            name, phone = args
            contacts[name] = phone
            print("Contact added.")
        elif command.lower() == "change":
            name, phone = args
            if name in contacts:
                contacts[name] = phone
                print("Contact updated.")
            else:
                print("Contact not found.")
        elif command.lower() == "phone":
            name = args[0]
            if name in contacts:
                print(contacts[name])
            else:
                print("Contact not found.")
        elif command.lower() == "all":
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

