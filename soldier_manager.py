def add_soldier(soldier_id: int, name: str, data: list) -> None:
    """
    מוסיפה חייל חדש למערכת.

    סוג: לוגיקה עסקית (Business Logic)

    מקבלת:
        soldier_id (int): מספר אישי של החייל
        name (str): שם החייל

    מחזירה:
        None - הפונקציה מוסיפה את החייל או זורקת exception

    זורקת:
        ValueError: אם id כבר קיים במערכת
        ValueError: אם name ריק או לא תקין

    למה הפונקציה קיימת:
    לוגיקה עסקית טהורה של הוספת חייל.
    מבצעת בדיקות תקינות ומוסיפה את החייל לנתונים.
    לא מטפלת בקלט/פלט - רק בלוגיקה.
    זורקת exceptions במקרה של שגיאה במקום להחזיר False.
    """
    if not name or not name.strip():
        raise ValueError("Name cannot be empty")

    for soldier in data:
        if soldier["id"] == soldier_id:
            raise ValueError(f"Soldier with id {soldier_id} already exists")

    data.append({"id": soldier_id, "name": name, "duties": []})


def remove_soldier(soldier_id: int, data: list) -> None:
    """
    מסירה חייל מהמערכת לפי id.

    סוג: לוגיקה עסקית (Business Logic)

    מקבלת:
        soldier_id (int): מספר אישי של החייל

    מחזירה:
        None - הפונקציה מסירה את החייל או זורקת exception

    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת

    למה הפונקציה קיימת:
    לוגיקה עסקית של הסרת חייל.
    מבצעת בדיקת קיום ומסירה מהנתונים.
    זורקת exception במקרה שהחייל לא קיים.
    """
    for soldier in data:
        if soldier["id"] == soldier_id:
            data.remove(soldier)
            return

    raise KeyError(f"Soldier with id {soldier_id} not found")


def get_all_soldiers(data: list) -> list:
    """
    מחזירה את רשימת כל החיילים במערכת.

    סוג: גישה לנתונים (Data Access)

    מקבלת: כלום

    מחזירה:
        list: רשימה של מילונים, כל מילון מייצג חייל
              רשימה ריקה אם אין חיילים

    זורקת: כלום - תמיד מחזירה רשימה (ריקה או מלאה)

    למה הפונקציה קיימת:
    גישה לנתונים בצורה מבוקרת.
    מאפשר לקבל את הנתונים מבלי לגשת ישירות למשתנה הגלובלי.
    """
    return data