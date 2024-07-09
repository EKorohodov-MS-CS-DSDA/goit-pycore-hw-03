from datetime import datetime
from datetime import date
from datetime import timedelta
import random
import re

# Task 1
def get_days_from_today(date: str) -> int:
    """
    Calculates the number of days since the given date.

    Parameters:
    date (str): The date in the format "YYYY-MM-DD".

    Returns:
    int: The number of days since the given date.
    """
    pattern = r"\d{4}-\d{2}-\d{2}"
    if not re.match(pattern, date):
        raise ValueError(f"Invalid date format: {date}. Must be YYYY-MM-DD.")
    
    input_date = datetime.strptime(date, "%Y-%m-%d")
    return (datetime.now() - input_date).days

# Task 2
def get_numbers_ticket(min_number: int, max_number: int, quantity: int) -> list:
    """
    Generates a list of unique random numbers within the specified range.

    Parameters:
    min_number (int): The minimum value of the range. Must be greater than 1.
    max (int): The maximum value of the range. Must be less than 1000.
    quantity (int): The number of unique random numbers to generate.
      Must be between min_number and max_number.

    Returns:
    list: A list of unique random numbers within the specified range.

    Raises:
    ValueError: If the parameters are invalid.
    """
    if min_number < 1:
        raise ValueError("Min number must be greater than 1.")
    if max_number > 1000:
        raise ValueError("Max number must be less than 1000.")
    if min_number >= quantity  or quantity >= max_number:
        raise ValueError(f"Quantity must be between {min_number} and {max_number}.")

    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min_number, max_number))
    return list(numbers)

# Task 3
def normalize_phone(phone_number: str) -> str:
    """
    Normalizes the phone number to the format "+380000000000".

    Parameters:
    phone_number (str): The phone number to normalize.

    Returns:
    str: The normalized phone number.

    Raises:
    ValueError: If the input phone number has an invalid number of digits.
    """

    # get numbers only
    pattern = r"(\d+)"
    number_string = "".join(re.findall(pattern, phone_number))

    # check the number length
    if len(number_string) < 10 or len(number_string) >= 13:
        raise ValueError(f"Can't process this phone number({number_string}). The number of digits is invalid.")

    # prepare data to zip
    phone_template = "+380000000000"
    number_string = number_string.rjust(13, "_")

    # zip phone template and the number string
    result = ""
    for template_ch, number_ch in zip(phone_template, number_string):
        result += number_ch if number_ch != "_" else template_ch

    return result

# Task 4
def get_upcoming_birthdays(users: list) -> list:
    """
    Returns a list of upcoming birthdays for the given users.

    Args:
    users (list): A list of dictionaries with users' information.

    Returns:
    list: A list of upcoming birthdays for the given users.
    """
    clebration_dict = {}
    for user in users:
        # get date data
        birthday_string = user["birthday"]
        pattern = r"(\d{4}).(\d{2}).(\d{2})"
        if not re.match(pattern, birthday_string):
            continue

        # prepare dates data
        birthady_date = datetime.strptime(birthday_string, "%Y.%m.%d").date()
        current_date = date.today()
        birthady_date_this_year = birthady_date.replace(year=current_date.year)

        # if the birthday has already happened, we'll celebrate next year
        if birthady_date_this_year < current_date:
            continue

        # if the birthday is on weekend, shift it to the next Monday
        birthday_week_day = birthady_date_this_year.weekday()
        if birthday_week_day >= 5:
            birthady_date_this_year = birthady_date_this_year + timedelta(days=7 - birthday_week_day)

        if (birthady_date_this_year - current_date).days < 10:
            clebration_dict[user["name"]] = birthady_date_this_year

    return clebration_dict


def main():
    users = [
    {"name": "John Doe", "birthday": "1985.07.08"},
    {"name": "John1 Doe", "birthday": "1985.07.10"},
    {"name": "Jane Smith", "birthday": "1990.07.13"},
    {"name": "Jane1 Smith", "birthday": "1990.07.18"}
    ]
    print(get_days_from_today("1985.07.08"))



    
if __name__ == "__main__":
    main()

