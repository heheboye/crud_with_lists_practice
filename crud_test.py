# Storage lists.
storage_id = [1, 2, 3]
storage_name = ['Carlos', 'Ricardo', 'Carlos']
storage_surname = ['Perez', 'Sanchez', 'Gutierrez']
storage_birthdate = ['30/11/1990', '19/08/1987', '22/07/1933']
storage_age = ['22', '39', '69']

# Create entries.
def new_entry(where, entry):
    where.append(entry)

# Search an entry by name.
def search_name_or_id(name_or_id):
    for index, (nombre, idxd) in enumerate(zip(storage_name, storage_id)):
        if nombre == name_or_id or idxd == name_or_id:
            print("\nId: " + str(storage_id[index]))
            print("Name: " + storage_name[index])
            print("Surname: " + storage_surname[index])
            print("Birthdate: " + storage_birthdate[index])
            print("Age: " + storage_age[index])

# Search an entry by id to update.
def search_and_update(idxd):
    for index, idnum in enumerate(storage_id):
        if idnum == idxd:
            print("\nCurrent values:")
            print("\nId: " + str(storage_id[index]))
            print("Name: " + storage_name[index])
            print("Surname: " + storage_surname[index])
            print("Birthdate: " + storage_birthdate[index])
            print("Age: " + storage_age[index])
            print("\nType new values (Don't type anything and press enter to leave an entry unchanged):")
            entry_name = input("\nName: ")
            entry_surname = input("Surname: ")
            entry_birthdate = input("Birthdate: ")
            entry_age = input("Age: ")
            if entry_name != "":
                storage_name[index] = entry_name
            if entry_surname != "":
                storage_surname[index] = entry_surname
            if entry_birthdate != "":
                storage_birthdate[index] = entry_birthdate
            if entry_age != "":
                storage_age[index] = entry_age
                
# Search by id and delete.
def search_and_delete(idxd):
    for index, idnum in enumerate(storage_id):
        if idnum == idxd:
            del storage_id[index]
            del storage_name[index]
            del storage_surname[index]
            del storage_birthdate[index]
            del storage_age[index]
            print("Entry deleted successfully.")
                               
# Menu selection.
while True:
    print("\n1) Create a new entry.")
    print("2) Search for an entry.")
    print("3) Update an entry.")
    print("4) Delete an entry.")
    print("5) Exit.\n")
    
    option = int(input("Select an option: "))
    if option == 1:
        # Type the data for the entries.
        entry_name = input("\nName: ")
        entry_surname = input("Surname: ")
        entry_birthdate = input("Birthdate: ")
        entry_age = input("Age: ")
        # Check if all the entries are valid.
        if entry_name == "" or entry_surname == "" or entry_birthdate == "" or entry_age == "":
            print("Entries can't be empty.\n")
        else:
            new_entry(storage_name, entry_name)
            new_entry(storage_surname, entry_surname)
            new_entry(storage_birthdate, entry_birthdate)
            new_entry(storage_age, entry_age)
            entry_id = int(len(storage_name))
            new_entry(storage_id, entry_id)
            print("\nEntries successfully registered.")
    elif option == 2:
        # Type the name you want to search.
        search_name = input("\nSearch by name or id: ")
        if search_name.isnumeric():
            search_name_or_id(int(search_name))
        else:    
            search_name_or_id(search_name)
    elif option == 3:
        # Type the id of the entry that you want to update or modify.
        search_id = input("\nSearch by id: ")
        if search_id.isnumeric():
            search_and_update(int(search_id))
        else:
            print("Only numbers accepted.")
    elif option == 4:
        # Type the id of the entry that you want to delete.
        search_id = input("\nSearch by id: ")
        if search_id.isnumeric():
            search_and_delete(int(search_id))
        else:
            print("Only numbers accepted.")
    elif option == 5:
        break