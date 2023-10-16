from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    # Створюємо словник для збереження іменнинників по днях тижня
    birthday_dict = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": []
    }
    
    # Отримуємо поточну дату
    today = datetime.today().date()
    
    # Перебираємо користувачів і аналізуємо їх дати народження
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        
        # Перевіряємо, чи вже минув день народження цього року
        if birthday < today:
            # Якщо так, розглядаємо дату на наступний рік
            birthday = birthday.replace(year=today.year + 1)
        
        # Обчислюємо різницю між днем народження і поточним днем
        delta_days = (birthday - today).days
        
        # Визначаємо день тижня для дня народження
        birthday_weekday = (today + timedelta(days=delta_days)).strftime("%A")
        
        # Перевіряємо, чи день народження припадає на вихідний
        if birthday_weekday in ["Saturday", "Sunday"]:
            # Якщо так, переміщаємо вітання на понеділок
            birthday_weekday = "Monday"
        
        # Додаємо ім'я до відповідного дня тижня в словнику
        birthday_dict[birthday_weekday].append(name)
    
    # Виводимо результат
    for day, names in birthday_dict.items():
        if names:
            print(f"{day}: {', '.join(names)}")

# Приклад використання
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jill Valentine", "birthday": datetime(1971, 2, 14)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)}
]

get_birthdays_per_week(users)
