def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

# Вітання користувача
def hello():
    return "How can I help you?"

# Для додавання нового контакту
def add_contact(contacts, name, phone):
    # Зберігаємо ім'я та номер телефону у словнику контактів
    contacts[name] = phone
    return "Contact added."

# Для зміни номера телефону у вже існуючого контакту
def change_contact(contacts, name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    return "Contact not found."

# Для виведення номера телефону за ім'ям
def show_phone(contacts, name):
    if name in contacts:
        return contacts[name]
    return "Contact not found."

def show_all(contacts):
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

# Головна функція, яка керує взаємодією з користувачем
def main():
    # Створюємо словник для збереження контактів
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        # Користувач вводить команду
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        # Перевіряємо, чи користувач не хоче завершити роботу бота
        if command in ["close", "exit"]:
            print("Good bye!")
            break

        # Обробляємо команди
        elif command == "hello":
            print(hello())

        elif command == "add":
            if len(args) == 2:
                name, phone = args
                print(add_contact(contacts, name, phone))
            else:
                print("Invalid command.")

        elif command == "change":
            if len(args) == 2:
                name, new_phone = args
                print(change_contact(contacts, name, new_phone))
            else:
                print("Invalid command.")

        elif command == "phone":
            if len(args) == 1:
                name = args[0]
                result = show_phone(contacts, name)
                print(result)
            else:
                print("Invalid command.")

        elif command == "all":
            result = show_all(contacts)
            print(result)

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
