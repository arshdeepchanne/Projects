import csv
from datetime import datetime
import calendar
import shutil
from tempfile import NamedTemporaryFile


def create_file():
    with open("sheet.csv", "w") as file:
        fieldnames = ["date", "limit", "spent", "saved", "total_month_spent"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        weekd = calendar.weekday(datetime.today().year, datetime.today().month, 1)
        cal = calendar.Calendar(firstweekday=weekd)

        for i in cal.itermonthdays(datetime.today().year, datetime.today().month):
            if i != 0:
                writer.writerow({"date": i, "limit": 0, "spent": 0, "saved": 0, "total_month_spent": 0})


def update_file(limit, expenditure, saving, total_month_spent):
    tempsheet =  NamedTemporaryFile(mode='w', delete=False)
    fieldnames = ["date", "limit", "spent", "saved", "total_month_spent"]

    with open("sheet.csv", "r") as csvfile, tempsheet:
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        writer = csv.DictWriter(tempsheet, fieldnames=fieldnames)
        for row in reader:
            if row["date"] == str(datetime.today().day):
                row["limit"], row["spent"], row["saved"], row["total_month_spent"] = limit, expenditure, saving, total_month_spent
            row = {"date": row["date"], "limit": row["limit"], "spent": row["spent"], "saved": row["saved"], "total_month_spent": row["total_month_spent"]}
            writer.writerow(row)

    shutil.move(tempsheet.name, "sheet.csv")

create_file()
update_file(3100, 90, 10, 90)