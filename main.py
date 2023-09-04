from datetime import date, datetime, timedelta
from collections import defaultdict


def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання

    users_list = defaultdict(list)

    current_date = date.today()
    current_year = current_date.year
    days_of_week = timedelta(days=7)

    if len(users) < 1:
        return users_list

    for user in users:
        user_birthday = user.get("birthday")

        if user_birthday.month == 1:
            user_birthday = user_birthday.replace(year=current_year + 1)
        else:
            user_birthday = user_birthday.replace(year=current_year)

        if user_birthday - current_date > days_of_week or user_birthday < current_date:
            continue

        birthday_weekday = user_birthday.weekday()

        if birthday_weekday == 0 or birthday_weekday == 5 or birthday_weekday == 6:
            users_list["Monday"].append(user.get("name"))
        elif birthday_weekday == 1:
            users_list["Tuesday"].append(user.get("name"))
        elif birthday_weekday == 2:
            users_list["Wednesday"].append(user.get("name"))
        elif birthday_weekday == 3:
            users_list["Thursday"].append(user.get("name"))
        elif birthday_weekday == 4:
            users_list["Friday"].append(user.get("name"))

    return users_list


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")