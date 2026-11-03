import json
import os
import secrets
import string

FILE_NAME = "passwords.json"


def load_data():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Unable to read password file.")
        return []


def save_data(accounts):
    with open(FILE_NAME, "w") as file:
        json.dump(accounts, file, indent=4)


def generate_password():
    characters = string.ascii_letters + string.digits + "!@#$%"
    return "".join(secrets.choice(characters) for _ in range(12))


def add_account(accounts):
    website = input("Enter website: ").strip()
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if not website or not username or not password:
        print("All fields are required!")
        return

    accounts.append({
        "website": website,
        "username": username,
        "password": password
    })

    save_data(accounts)
    print("Account saved successfully!")


def show_accounts(accounts):
    if not accounts:
        print("No accounts saved.")
        return

    print("\n--- Saved Accounts ---")

    for account in accounts:
        print("Website:", account["website"])
        print("Username:", account["username"])
        print("Password: ********")
        print("---------------------")


def search_account(accounts):
    website = input("Enter website to search: ").strip().lower()

    for account in accounts:
        if account["website"].lower() == website:
            print("Website:", account["website"])
            print("Username:", account["username"])
            print("Password:", account["password"])
            return

    print("Account not found!")


def delete_account(accounts):
    website = input("Enter website to delete: ").strip().lower()

    for account in accounts:
        if account["website"].lower() == website:
            accounts.remove(account)
            save_data(accounts)
            print("Account deleted!")
            return

    print("Account not found!")


def create_random_password():
    password = generate_password()
    print("Generated Password:", password)


accounts = load_data()

while True:
    print("\n===== PASSWORD MANAGER =====")
    print("1. Add Account")
    print("2. Show Accounts")
    print("3. Search Account")
    print("4. Delete Account")
    print("5. Generate Password")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_account(accounts)

    elif choice == "2":
        show_accounts(accounts)

    elif choice == "3":
        search_account(accounts)

    elif choice == "4":
        delete_account(accounts)

    elif choice == "5":
        create_random_password()

    elif choice == "6":
        print("Password Manager Closed.")
        break

    else:
        print("Invalid choice!")
