import datetime
def display_current_datetime():
    current_date = datetime.datetime.now()

    current_date_time = current_date.strftime(
        "Today is %Y-%m-%d %H:%M:%S"
    )
    print(f"Current date and time: {current_date_time}")
display_current_datetime()

number_of_days = int(input("Enter the number of days to add to the current date: "))
from datetime import timedelta, date
def calculate_future_date(number_of_days):
    current_date = date.today()
    duration = timedelta(days=number_of_days)
    future_date = current_date + duration
    formatted_date = future_date.strftime("%Y-%m-%d")
    return formatted_date
future_date = calculate_future_date(number_of_days)
print(f"Future date: {future_date}")