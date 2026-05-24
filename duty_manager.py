from utils import DAYS, STATUS


def add_duty_to_soldier(soldier_id: int, duty_name: str, day: str, data: list) -> None:
    """
    מוסיפה תורנות חדשה לחייל.
    
    סוג: לוגיקה עסקית (Business Logic)
    
    מקבלת:
        soldier_id (int): מספר אישי של החייל
        duty_name (str): שם התורנות
        day (str): יום בשבוע (sunday/monday/tuesday/wednesday/thursday)
    מחזירה:
        None - הפונקציה מוסיפה את התורנות או זורקת exception
    
    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת
        ValueError: אם תורנות עם שם זה כבר קיימת לחייל
        ValueError: אם day לא חוקי (friday/saturday או ערך לא תקין)
    
    למה הפונקציה קיימת:
    לוגיקה עסקית של הוספת תורנות.
    מבצעת בדיקות ומוסיפה תורנות לחייל.
    זורקת exceptions במקרה של שגיאה במקום להחזיר False.
    """
  
    day_lower = day.lower()
    if day_lower not in DAYS:
        raise ValueError(f"Invalid day: {day}. Must be one of: {', '.join(DAYS)}")

    for soldier in data:
        if soldier["id"] == soldier_id:
            for duty in soldier["duties"]:
                if duty["name"] == duty_name:
                    raise ValueError(f"Duty '{duty_name}' already exists for soldier {soldier_id}")
            soldier["duties"].append({"name": duty_name, "day": day_lower, "status": "pending"})
            return

    raise KeyError(f"Soldier with id {soldier_id} not found")


def update_duty_status(soldier_id: int, duty_name: str, new_status: str, data: list) -> None:
    """
    מעדכנת את הסטטוס של תורנות.

    סוג: לוגיקה עסקית (Business Logic)

    מקבלת:
        soldier_id (int): מספר אישי של החייל
        duty_name (str): שם התורנות
        new_status (str): סטטוס חדש (pending/completed/missed)

    מחזירה:
        None - הפונקציה מעדכנת את הסטטוס או זורקת exception

    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת
        KeyError: אם תורנות עם שם זה לא נמצאה לחייל
        ValueError: אם new_status לא חוקי (לא pending/completed/missed)

    למה הפונקציה קיימת:
    לוגיקה עסקית של עדכון סטטוס.
    מבצעת בדיקות ומעדכנת את הסטטוס.
    זורקת exceptions במקרה של שגיאה במקום להחזיר False.
    """
    valid_statuses = STATUS
    if new_status not in valid_statuses:
        raise ValueError(f"Invalid status: {new_status}. Must be one of: {', '.join(valid_statuses)}")

    for soldier in data:
        if soldier["id"] == soldier_id:
            for duty in soldier["duties"]:
                if duty["name"] == duty_name:
                    duty["status"] = new_status
                    return
            raise KeyError(f"Duty '{duty_name}' not found for soldier {soldier_id}")

    raise KeyError(f"Soldier with id {soldier_id} not found")


def get_soldier_duties(soldier_id: int, data: list) -> list:
    """
    מחזירה את רשימת התורנויות של חייל.

    סוג: גישה לנתונים (Data Access)

    מקבלת:
        soldier_id (int): מספר אישי של החייל

    מחזירה:
        list: רשימת תורנויות (מילונים)
              רשימה ריקה אם אין תורנויות

    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת

    למה הפונקציה קיימת:
    גישה מבוקרת לתורנויות של חייל.
    מפרידה בין הנתונים לבין הגישה אליהם.
    זורקת exception אם החייל לא קיים (במקום להחזיר רשימה ריקה).
    """
    for soldier in data:
        if soldier["id"] == soldier_id:
            return soldier["duties"]

    raise KeyError(f"Soldier with id {soldier_id} not found")