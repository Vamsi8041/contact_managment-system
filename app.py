import streamlit as st

TABLE_SIZE = 100

# Hash function
def hash_function(name):
    hash_val = sum(ord(char) for char in name)
    return hash_val % TABLE_SIZE

def add_contact(phone_book, name, number):
    index = hash_function(name)
    if index not in phone_book:
        phone_book[index] = [{'name': name, 'number': number}]
    else:
        for contact in phone_book[index]:
            if contact['name'] == name:
                st.warning("Contact already exists!")
                return
        phone_book[index].append({'name': name, 'number': number})
    st.success("Contact added successfully!")

def search_contact(phone_book, name):
    index = hash_function(name)
    if index in phone_book:
        for contact in phone_book[index]:
            if contact['name'] == name:
                st.write(f"Contact found - Name: {contact['name']}, Number: {contact['number']}")
                return
    st.warning("Contact not found!")

def delete_contact(phone_book, name):
    index = hash_function(name)
    if index in phone_book:
        contacts = phone_book[index]
        for i, contact in enumerate(contacts):
            if contact['name'] == name:
                del contacts[i]
                st.success("Contact deleted successfully!")
                return
    st.warning("Contact not found!")

def display_contacts(phone_book):
    st.write("Phone Book Contacts:")
    for contacts in phone_book.values():
        for contact in contacts:
            st.write(f"Name: {contact['name']}, Number: {contact['number']}")

def main():
    st.title("Contact Management System")
    if 'phone_book' not in st.session_state:
        st.session_state.phone_book = {}

    # Names to be added
    predefined_names = ["Vamsi", "Prabath", "Madavi", "Surya", "Bhagya Sri"]

    choice = st.sidebar.selectbox("Choose an operation", ("Add Contact", "Search Contact", "Delete Contact", "Display Contacts"))
    
    if choice == "Add Contact":
        name = st.selectbox("Select a name to add", predefined_names)
        number = st.text_input("Enter number")
        if st.button("Add"):
            add_contact(st.session_state.phone_book, name, number)
    elif choice == "Search Contact":
        name = st.text_input("Enter name to search")
        if st.button("Search"):
            search_contact(st.session_state.phone_book, name)
    elif choice == "Delete Contact":
        name = st.text_input("Enter name to delete")
        if st.button("Delete"):
            delete_contact(st.session_state.phone_book, name)
    elif choice == "Display Contacts":
        display_contacts(st.session_state.phone_book)

if __name__ == "__main__":
    main()
