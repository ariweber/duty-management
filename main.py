from data import data
from menu import show_menu, get_user_choice
from soldier_manager import add_soldier, remove_soldier, get_all_soldiers, update_duty_status, get_soldier_duties
from handles_func import handle_add_soldier, handle_remove_soldier, handle_update_soldier, handle_view_soldiers, handle_delete_soldier
def main() -> None:
 """Main function to run the soldier management system."""
 exit_p = False
while not exit_p:
    show_menu()
    choice = get_user_choice()
    if choice == "1":
        handle_add_soldier()
    elif choice == "2":
        handle_view_soldiers()
    elif choice == "3":
        handle_update_soldier()
    elif choice == "4":
        handle_delete_soldier()
    elif choice == "5":
        exit_p = True
    else:
        print("Invalid choice. Please try again.")

        

if __name__ == "__main__":
    main()