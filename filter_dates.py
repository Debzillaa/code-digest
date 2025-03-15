# Write a Python program that implements a Python program that filters out dates (in that format "YYYY-MM-DD") that are in future using the filter function.
from datetime import datetime
# Define a list of dates in "YYYY-MM-DD" format
date_strings = ["2021-04-01", "2022-05-15", "2023-07-20", "2020-12-31", "2024-01-01", "2019-08-25", "2025-09-10", "2018-03-05", "2023-11-11", "2022-02-28"]
print("List of dates:")
print(date_strings)
# Convert the date strings to datetime objects
dates = [datetime.strptime(date, "%Y-%m-%d") for date in date_strings]
# Get the current date
current_date = datetime.now()
print("\nCurrent date:", current_date)
# Define a function to check if a date is in the future
def is_date_in_future(date):
    return date > current_date
# Use the filter function to extract dates in the past
dates_in_past = list(filter(is_date_in_future, dates))
# Convert the filtered dates back to strings
filtered_date_strings = [date.strftime("%Y-%m-%d") for date in dates_in_past]
print("\nCheck if a date is in the future!")
# Print the dates in the past
print(filtered_date_strings)