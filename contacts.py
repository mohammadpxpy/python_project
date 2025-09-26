
start = input("for start click ENTER")
if len(start) == 0:
    while True:
        user = input(" for add contact print << add >> \n for read list contacts print << show >> \n to search print << search >> \n for remove << remove >> \n << exit >> \n : ")
        if user == "add" :
            name = input("enter name: ")
            number = input("enter number: ")
            with open("contacts.txt", "a") as file:
                file.write(f"{name} : {number}\n")
            print("contact added")
        elif user == "show" :
            try:
                with open(r"C:\Users\pc\Desktop\project\contacts.txt", "r") as file:
                    show = file.read()
                    if show:
                        print(show)
                    else:
                        print("NO contacts")
            except FileNotFoundError:
                print("not found")
        elif user == "search" :
            search_name = input("enter name to search: ")
            try:
                with open(r"C:\Users\pc\Desktop\project\contacts.txt", "r") as file:
                    found = False
                    for i in file:
                        if search_name.lower() in i.lower():
                            print(i.strip())
                            found = True
                    if not found:
                        print(f"NO contact found with name {search_name}")
            except FileNotFoundError:
                print("not found")
        elif user == "remove" :
            remove_name = input("plase enter name to remove: ")
            try:
                with open(r"C:\Users\pc\Desktop\project\contacts.txt", "r") as file:
                    lines = file.readlines()
                with open(r"C:\Users\pc\Desktop\project\contacts.txt", "w") as file:
                    found = False
                    for line in lines:
                        if remove_name.lower() not in line.lower():
                            file.write(line)
                        else:
                            found = True
                    if found:
                        print(f"contact with name {remove_name} removed")
                    else:
                        print("not found")
            except FileNotFoundError:
                print("not found")
        elif user == "exit":
            break
        else:
            print("Plase use << add , show , search , remove , exit >>")