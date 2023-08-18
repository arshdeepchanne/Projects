from datetime import datetime
import calendar
import csv

with open("expense-sheet.csv", "w") as file:
    fieldnames = ["date", "limit", "spent", "saved", "total_month_spent"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    weekd = calendar.weekday(datetime.today().year, datetime.today().month, 1)
    cal = calendar.Calendar(firstweekday=weekd)

    for i in cal.itermonthdays(datetime.today().year, datetime.today().month):
        if i != 0:
            writer.writerow({"date": i, "limit": 0, "spent": 0, "saved": 0, "total_month_spent": 0})

