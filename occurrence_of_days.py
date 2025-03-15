# Find number of times every day occurs in a Year
import datetime
import calendar

def day_occur_time(year):
    # Store days in a week
    days = ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"]
    
    # Initialize all counts as 52
    L = [52 for i in range(7)]

    # Find the index of the first day of the year
    pos = -1
    day = datetime.datetime(year, month = 1, day = 1).strftime("%A")
    for i in range(7):
        if day == days[i]:
            pos = i

    # Mark the occurrence to be 53 of the first day and second day if the year is a leap year
    if calendar.isleap(year):
        L[pos] += 1
        L[(pos + 1) % 7] += 1

    else:
        L[pos] += 1

    # Print the days
    for i in range(7):
        print(days[i], L[i])

# Driver code
year = 2025
day_occur_time(year)