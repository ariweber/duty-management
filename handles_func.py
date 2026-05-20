from os import name

from data import data
from menu import show_menu, get_user_choice
from soldier_manager import add_soldier, remove_soldier, get_all_soldiers, update_duty_status, get_soldier_duties
from input import input_id, input_name  
from utils import is_valid_day, is_valid_id, is_valid_name, is_valid_status, find_soldier_by_id, find_soldier_by_name, soldier_has_duty is_valid_id        



def handle_add_soldier() -> None:
    """Handles the logic for adding a soldier."""
    flag = True
    while not flag:
            soldier_id = input_id()
            if is_valid_id(soldier_id):
                flag = True
                name = input_name()
                if is_valid_name(name):
                    flag = True
    add_soldier(soldier_id, name)
    print(f"Soldier {name} with ID {soldier_id} added successfully.")   
           
    

def handle_view_soldiers() -> None:
    """Handles the logic for viewing all soldiers."""
    pass

def handle_update_soldier() -> None:
    """Handles the logic for updating a soldier's duty status."""
    pass

def handle_delete_soldier() -> None:
    """Handles the logic for deleting a soldier."""
    pass
