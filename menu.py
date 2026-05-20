def show_menu() -> None:
    """Displays the menu options to the user."""
    print("=== Soldier Management System ===")
    print("1. Add Soldier")
    print("2. View Soldiers")
    print("3. Update Soldier")
    print("4. Delete Soldier")
    print("5. Exit")

def get_user_choice() -> str:
    """Prompts the user to enter their choice and returns it."""
    return input("Enter your choice: ")


