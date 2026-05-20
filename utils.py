MAX_SOLDIER_ID = 9999999


def find_soldier_by_id(soldier_id: int) -> dict | None:
    """Finds a soldier by their ID and returns their information as a dictionary."""
    pass

def find_soldier_by_name(name: str) -> dict | None:
    """Finds a soldier by their name and returns their information as a dictionary."""
    pass

def is_valid_status(status: str) -> bool:
    """Checks if the provided status is valid."""
    pass

def is_valid_id(soldier_id: int) -> bool:
    """Checks if the provided soldier ID is valid."""
    try:
        soldier_id = int(soldier_id)
        if soldier_id > MAX_SOLDIER_ID:
            print("Invalid ID. Please enter a valid soldier ID.")
            return False
        return True
    except ValueError:
        print("Invalid ID. Please enter a numeric value.")
        return False
        
  

def is_valid_name(name: str) -> bool:
    """Checks if the provided name is valid."""
    if isinstance(name, str) and name.strip():
        return True
    print("Invalid name. Please enter a valid string.")
    return False

def soldier_has_duty(soldier: dict, duty_name: str) -> bool:
    """Checks if a soldier has a specific duty assigned."""
    pass


def is_valid_day(day: str) -> bool:
    """Checks if the provided day is valid."""
    pass