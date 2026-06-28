# Notes Manager using File Handling

while True:
    print("\n===== Notes Manager =====")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        note = input("Enter your note: ")

        with open("notes.txt", "a") as file:
            file.write(note + "\n")

        print("Note Saved Successfully!")

    elif choice == "2":
        try:
            with open("notes.txt", "r") as file:
                notes = file.read()

                if notes:
                    print("\nYour Notes:")
                    print(notes)
                else:
                    print("No Notes Available.")

        except FileNotFoundError:
            print("No Notes Found.")

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")