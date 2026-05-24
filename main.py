from data import data
from soldier_manager import add_soldier, remove_soldier, get_all_soldiers
from duty_manager import add_duty_to_soldier, update_duty_status, get_soldier_duties


def show_menu() -> None:
    """
    מציגה את התפריט הראשי למשתמש.

    מקבלת: כלום
    מחזירה: כלום (מדפיסה לקונסול)

    למה הפונקציה קיימת:
    הפרדה בין הצגת התפריט לבין הלוגיקה העסקית.
    אם נרצה לשנות את התצוגה, נשנה רק כאן.
    """
    print("\n=== Duty Management System ===")
    print("1. Add soldier")
    print("2. Remove soldier")
    print("3. View all soldiers")
    print("4. Add duty to soldier")
    print("5. Update duty status")
    print("6. View soldier duties")
    print("7. Exit")


def get_user_choice() -> str:
    """
    מקבלת בחירה מהמשתמש.

    מקבלת: כלום
    מחזירה: מחרוזת המייצגת את בחירת המשתמש

    למה הפונקציה קיימת:
    הפרדת קבלת קלט מהמשתמש מהלוגיקה של עיבוד הבחירה.
    מאפשר להחליף את שיטת הקלט בעתיד (למשל, GUI).
    """
    return input("Choose an option: ")


def handle_add_soldier() -> None:
    """
    מטפלת בתהליך הוספת חייל חדש.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    מפרידה בין הקלט/פלט לבין הלוגיקה העסקית.
    main.py אחראי על אינטראקציה עם המשתמש,
    soldier_manager.py אחראי על הלוגיקה.
    """
    try:
        soldier_id = int(input("Enter soldier ID: "))
        name = input("Enter soldier name: ")
        add_soldier(soldier_id, name, data)
        print(f"Soldier '{name}' added successfully.")
    except ValueError as e:
        print(f"Error: {e}")


def handle_remove_soldier() -> None:
    """
    מטפלת בתהליך הסרת חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    try:
        soldier_id = int(input("Enter soldier ID to remove: "))
        remove_soldier(soldier_id, data)
        print(f"Soldier {soldier_id} removed successfully.")
    except ValueError:
        print("Error: Please enter a valid numeric ID.")
    except KeyError as e:
        print(f"Error: {e}")


def handle_view_soldiers() -> None:
    """
    מטפלת בתהליך הצגת כל החיילים.
    קוראת לפונקציה המתאימה ומציגה את התוצאה.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין קבלת הנתונים לבין הצגתם.
    """
    soldiers = get_all_soldiers(data)
    if not soldiers:
        print("No soldiers in the system.")
    else:
        for soldier in soldiers:
            print(f"ID: {soldier['id']}, Name: {soldier['name']}, Duties: {len(soldier['duties'])}")


def handle_add_duty() -> None:
    """
    מטפלת בתהליך הוספת תורנות לחייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    try:
        soldier_id = int(input("Enter soldier ID: "))
        duty_name = input("Enter duty name: ")
        day = input("Enter day (sunday-thursday): ")
        add_duty_to_soldier(soldier_id, duty_name, day, data)
        print(f"Duty '{duty_name}' added to soldier {soldier_id}.")
    except ValueError as e:
        print(f"Error: {e}")
    except KeyError as e:
        print(f"Error: {e}")


def handle_update_duty_status() -> None:
    """
    מטפלת בתהליך עדכון סטטוס תורנות.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    try:
        soldier_id = int(input("Enter soldier ID: "))
        duty_name = input("Enter duty name: ")
        new_status = input("Enter new status (pending/completed/missed): ")
        update_duty_status(soldier_id, duty_name, new_status, data)
        print(f"Duty '{duty_name}' status updated to '{new_status}'.")
    except ValueError as e:
        print(f"Error: {e}")
    except KeyError as e:
        print(f"Error: {e}")


def handle_view_soldier_duties() -> None:
    """
    מטפלת בתהליך הצגת תורנויות של חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    try:
        soldier_id = int(input("Enter soldier ID: "))
        duties = get_soldier_duties(soldier_id, data)
        if not duties:
            print(f"Soldier {soldier_id} has no duties.")
        else:
            for duty in duties:
                print(f"  Duty: {duty['name']}, Day: {duty['day']}, Status: {duty['status']}")
    except ValueError:
        print("Error: Please enter a valid numeric ID.")
    except KeyError as e:
        print(f"Error: {e}")


def main() -> None:
    """
    הפונקציה הראשית של התוכנית.
    מריצה לולאה ראשית שמציגה תפריט, מקבלת בחירה ומפעילה פעולה.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    נקודת הכניסה לתוכנית. מנהלת את הזרימה הראשית.
    """
    while True:
        show_menu()
        choice = get_user_choice()

        if choice == "1":
            handle_add_soldier()
        elif choice == "2":
            handle_remove_soldier()
        elif choice == "3":
            handle_view_soldiers()
        elif choice == "4":
            handle_add_duty()
        elif choice == "5":
            handle_update_duty_status()
        elif choice == "6":
            handle_view_soldier_duties()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()