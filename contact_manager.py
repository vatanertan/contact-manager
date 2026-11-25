
#Helper Functions
def display_message(msg):
    """
    Print messages clearly.
    """
    print(f"\n{msg}")

def get_input(txt):
    """
    Getting safe input from the user.(solving the unknown space characters)
    """
    print(txt, end='')
    return input().strip()

def find_contact(contacts_list, search_term):
    """
    Finds all contacts whose name contains the search term (case-insensitive).
    Returns a list of matching contact dictionaries.
    """
    found_contacts = []
    lower_search_term = search_term.lower() #Convert search term to lowercase once for case-insensitive comparison

    for contact in contacts_list: #Check if the 'name' value contains the search term
        if lower_search_term in contact['Name'].lower():
            found_contacts.append(contact)
    return found_contacts

def select_contact(found_contacts, action_name, search_term):
    """
    Handles displaying multiple matching contacts and letting the user select one.
    Returns the selected contact dictionary or None if cancelled or no match.
    """
    num_matches = len(found_contacts) #Give error message for zero match including search term taken from user
    if num_matches == 0:
        print("Error: No contacts found matching","\'"+search_term+"\' search term.")
        return None

    if num_matches == 1: #Check for single match
        return found_contacts[0]


    print(f"\nMultiple contacts found. Please select one to {action_name}:") #Handle multiple matches using a loop and if/else validation

    for index, contact in enumerate(found_contacts): #Print the selection list
        contact_name = contact['Name']
        contact_phone = contact['Phone']
        print(f"[{index + 1}] {contact_name} ({contact_phone})")

    while True: #Ask for user selection until a valid choice is made
        choice = get_input(f"Enter number of contact to {action_name}, (or 'cancel'): ")

        if choice.lower() == 'cancel': #Check for cancel
            display_message(f"Operation cancelled. Returning to main menu.")
            return None

        if choice.isdigit(): #Check if the input is a valid number using 'isdigit()'
            choice_index = int(choice) - 1 #Convert choice to integer for list indexing

            if 0 <= choice_index < num_matches: #Check if the index is valid using if/else
                return found_contacts[choice_index]

            else:
                print("Invalid choice. Please enter a number from the list or 0 to cancel.")

        else:
            print("Invalid input. Please enter a number.") #Handle non-numeric input


#Main Contact Manager Functions


def add_contact(contacts_list,contact_keys):
    """
    Prompts the user for all contact details, validates the phone number,
    and adds the new contact (dictionary) to the contacts list.
    """
    print("\n*** ADD NEW CONTACT (Type 'cancel' to return to menu) ***")
    new_contact = {} #Use a dictionary to temporarily store the new contact data

    for key in contact_keys: #Loop through the required keys defined in the tuple to collect input

        while True: #Loop until valid input is received or user enters 'cancel'
            if key == 'Name':
                prompt_name = "Enter Name (or 'cancel'): "
            elif key == 'Phone':
                prompt_name = "Enter Phone (11 digits, or 'cancel'): "
            elif key == 'Email':
                prompt_name = "Enter Email (or 'cancel'): "
            elif key == 'Country':
                prompt_name = "Enter Country (or 'cancel'): "

            user_input = get_input(prompt_name)

            if user_input.lower() == 'cancel': #Check for cancel condition
                display_message("Operation cancelled. Returning to main menu.")
                return

            if key == "Name" and user_input.strip() == "": #Validation for name (must not be empty)
                print("Error: Name cannot be empty. Operation cancelled. Returning to main menu.")
                return

            if key == "Phone": #Validation for phone (must be 11 digits and numeric)
                if user_input.strip() == "":
                    print("Error: Phone number cannot be empty. Operation cancelled. Returning to main menu.")
                    return

                if not user_input.isdigit():
                    print("Error: Phone number must contain only numbers (no dashes or spaces).")
                    continue

                if len(user_input) != 11: #Check length using len() function
                    print("Error: Phone number must be exactly 11 digits (no dashes or spaces).")
                    continue

            if key == "Email" and user_input.strip() == "":
                print("Error: Email cannot be empty. Operation cancelled. Returning to main menu.")
                return

            if key == "Country" and user_input.strip() == "":
                print("Error: Country cannot be empty. Operation cancelled. Returning to main menu.")
                return

            new_contact[key] = user_input #If all checks pass for the current field, store it and break the inner loop
            break

    contacts_list.append(new_contact) #All fields collected and validated, add the new dictionary to the mutable list
    print(f"\nSUCCESS: Contact '{new_contact['Name']}' added.")


def view_contacts(contacts_list,contact_keys):
    """
    Displays all contacts in a structured, table-like format using f-string and ljust() function.
    """
    print("\n*** VIEW ALL CONTACTS ***")

    if not contacts_list:
        display_message("The contact list is empty.")
        return

    i_width = 5
    n_width = 20
    p_width = 15  #Define column width's of the table
    e_width = 25
    c_width = 15

    total = i_width + n_width + p_width + e_width + c_width + (3 * 4)
    separator = "-" * total #Find the length of the line separator

    print(separator)

#Contact List Header
    header = (
        "Index".ljust(i_width) + " | " +
        contact_keys[0].ljust(n_width) + " | " +
        contact_keys[1].ljust(p_width) + " | " +
        contact_keys[2].ljust(e_width) + " | " +
        contact_keys[3].ljust(c_width)
    )
    print(header)
    print(separator)

#Contact List Table
    for index, contact in enumerate(contacts_list):
        row = (
                str(index).ljust(i_width) + " | " +
                contact['Name'].ljust(n_width) + " | " +
                contact['Phone'].ljust(p_width) + " | " +
                contact['Email'].ljust(e_width) + " | " +
                contact['Country'].ljust(c_width)
        )
        print(row)

    print(separator)


def edit_contact(contacts_list,contact_keys):
    """
    Allows the user to search for a contact and edit one of its fields.
    Handles multiple search results and input validation.
    """
    print("\n*** EDIT CONTACT (Type 'cancel' to return to menu) ***")

    search_term = get_input("Enter the name (or part of the name) to edit (or 'cancel'): ")
    if search_term.lower() == 'cancel':
        display_message("Operation cancelled. Returning to main menu.")
        return
    if search_term == " " or search_term == "":
        display_message("Search term cannot be empty.")
        return

    found_contacts = find_contact(contacts_list, search_term)

    contact_to_edit = select_contact(found_contacts, "edit",search_term) #Use helper function to select the specific contact to edit

    if contact_to_edit is None:
        return #Operation cancelled or no contacts found

    print(f"\nEditing Contact: {contact_to_edit['Name']}")

    options = contact_keys #Display edit menu using the contact_keys tuple
    print("Which field do you want to change?")

    for index, key in enumerate(options): #Print the editing options using a for loop
        current_value = contact_to_edit[key]
        print(f"{index + 1}: {key} (Current: {current_value})")

    while True:
        choice = get_input(f"Enter choice (1-4, or 'cancel'): ")

        if choice.lower() == 'cancel': #Check for cancel condition
            display_message("Operation cancelled. Returning to main menu.")
            return

        if choice.isdigit(): #Check if the input is a valid number using isdigit() function
            choice_index = int(choice) - 1

            if 0 <= choice_index < len(options): #Check if the choice is a valid index for the keys
                key_to_change = options[choice_index]
                break
            else:
                print(f"Invalid choice. Please enter a number between 1 and 4.")
        else:
            print("Invalid input. Please enter a number.") #Handle non-numeric input

#Get New Value and Validate
    new_value = get_input(f"Enter new value for {key_to_change} (or 'cancel'): ")

    if new_value.lower() == 'cancel': #Check for cancel condition
        display_message("Operation cancelled. Returning to main menu.")
        return

    if key_to_change == 'Phone': #Phone validation check (must be 11 digits and numeric)
        if len(new_value) != 11 or not new_value.isdigit():
            print("Error: Phone number update failed. It must be exactly 11 digits and contain only numbers. No changes applied.")
            return

    original_name = contact_to_edit['Name'] #Perform the update on the dictionary
    contact_to_edit[key_to_change] = new_value

    print(f"\nSUCCESS: {key_to_change} of {original_name} updated to {new_value}.")


def delete_contact(contacts_list,contact_keys):
    """
    Allows the user to search for a contact and confirm its deletion.
    Handles multiple search results.
    """
    print("\n*** DELETE CONTACT (Type 'cancel' to return to menu) ***")

    search_term = get_input("Enter the name (or part of the name) to delete (or 'cancel'): ")
    if search_term.lower() == 'cancel':
        display_message("Operation cancelled. Returning to main menu.")
        return
    if search_term == " ":
        display_message("Search term cannot be empty.")
        return
    found_contacts = find_contact(contacts_list, search_term)

    contact_to_delete = select_contact(found_contacts, "delete",search_term) #Use helper function to select the specific contact to delete

    if contact_to_delete is None:
        return #Operation cancelled or no contacts found

    confirmation = get_input(f"Are you sure you want to delete '{contact_to_delete['Name']}'? (yes/no): ")

    if confirmation.lower() == 'yes': #Use the list's 'remove' method which finds the object and removes it.
        contacts_list.remove(contact_to_delete) #This avoids needing to find the index first.
        print(f"\nSUCCESS: Contact '{contact_to_delete['Name']}' has been deleted.")
    else:
        display_message(f"Delete operation cancelled for {contact_to_delete['Name']}.")


def run_manager(contacts_list):
    """
    The main application loop for the Contact Manager.
    Displays the menu and handles user choice using if/elif/else statements.
    """
    contact_keys = ('Name', 'Phone', 'Email', 'Country')  # Tuple for dynamic structure
    while True: #Use a while True loop for continuous menu
        print("\n"+"-" * 40)
        print("      SIMPLE CONTACT MANAGER MENU")
        print("-" * 40)
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        print("-" * 40)

        choice = get_input("Enter your choice (1-5): ")

        if choice == '1': #Use if/elif/else for menu navigation and operation logic
            add_contact(contacts_list,contact_keys)
        elif choice == '2':
            view_contacts(contacts_list,contact_keys)
        elif choice == '3':
            edit_contact(contacts_list,contact_keys)
        elif choice == '4':
            delete_contact(contacts_list,contact_keys)
        elif choice == '5':
            print("Exiting Contact Manager. Goodbye!") # Exit the loop and the program
            break
        elif choice.isdigit():
            print("Invalid choice. Please enter a number between 1 and 5.")
        else:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        input_file_path = sys.argv[1]
        sys.stdin = open(input_file_path, 'r')
    contacts_list = []
    run_manager(contacts_list)
    if len(sys.argv) > 1:
        sys.stdin.close()