def input_error(func):  # Створення декоратора обробки помилок
    def inner(*args, **kwargs): # Внутрішня функція для обгортки переданої
        try:
            return func(*args, **kwargs) # Спроба виконання з переданими аргументами
        except (KeyError, ValueError, IndexError):
            return "Enter the argument for the command" # Вивід помилки у випадку KeyError, ValueError чи IndexError
    return inner

@input_error
def parse_input(user_input):  
    cmd, *args = user_input.split() # Розділяємо введений рядок на команду та аргументи
    cmd = cmd.strip().lower() # Перетворюємо команду в нижній регістр
    return cmd, args

@input_error
def add_contact(args, contacts): # Додаємо контакт до словника
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts): # Оновлюємо номер телефону для існуючого контакту
    name, phone = args
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts): # Виводимо номер телефону для зазначеного контакту
    phone_number = contacts.get(args[0])
    if phone_number:
        return phone_number
    else:
        raise KeyError

def main():
    contacts = {} # Словник для збереження контактів
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
