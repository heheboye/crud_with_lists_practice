# Storage lists.
storage_id = [1, 2, 3]
storage_name = ['Carlos', 'Ricardo', 'Carlos']
storage_surname = ['Sarlanga', 'Sarnoso', 'Arandano']
storage_birthdate = ['30/11/1990', '19/08/1987', '22/07/1933']
storage_age = ['22', '39', '69']

# Create entries.
def new_entry(where, entry):
    where.append(entry)

# Search an entry by name.
def search_by_name(name):
    for index, nombre in enumerate(storage_name):
        if nombre == name:
            print("\nId: " + str(storage_id[index]))
            print("Name: " + storage_name[index])
            print("Surname: " + storage_surname[index])
            print("Birthdate: " + storage_birthdate[index])
            print("Age: " + storage_age[index])
            
# Menu selection.
while True:
    print("\n1) Create a new entry.")
    print("2) Search for an entry.")
    print("3) Update an entry.")
    print("4) Delete an entry.\n")
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
        search_name = input("\nNombre a buscar: ")
        search_by_name(search_name)