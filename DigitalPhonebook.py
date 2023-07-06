def print_menu():
    print('1. New Contact')
    print('2. Existing Contact')
    print('3. Show Phonebook')
    print()

numbers = {}
menu_choice = 0
print_menu()
while menu_choice != 3:
    menu_choice = int(input("Type in a number (1-3): "))
    if menu_choice == 1:
        print("Add Name and Number")
        name = input("Name: ")
        phone = input("Number: ")
        numbers[name] = phone
        print()
    elif menu_choice == 2:
        print("Existing contact")
        name = input("Name: ")
        if name in numbers:
            print("The number is", numbers[name])
        else:
            print(name, "was not found")
    elif menu_choice == 3:
        print("Phonebook:")
        sorted_phonebook =dict(sorted(numbers.items()))
        for name, phone_no in sorted_phonebook.items() :
         print("Name: ", name, "\tNumber:", phone_no)
        print_menu()
