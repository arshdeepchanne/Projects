import csv
from datetime import datetime
import calendar
import sys

# List of dictionaries to store data read from csv.
month_data = []

# Consturct present month's file name.
file_name = "expense-sheet-{}-{}.csv".format(
    str(datetime.today().year), calendar.month_abbr[datetime.today().month]
)

# Get today's date.
today_date = datetime.today().day


def main():
    # Check if user wants to create a new file to store data.
    if len(sys.argv) > 2:
        sys.exit("Usage: project.py [new: optional]")
    elif len(sys.argv) == 2 and sys.argv[1] == "new":
        create_file()

    # Reads the file into a list of dictionaries.
    try:
        read_file()
    except FileNotFoundError as e:
        sys.exit(f"{e}: Please create a new file.\n" +
        "Usage: project.py [optional: new]"
        )

    # Get and store the months budget in a global variable.
    global budget
    budget = round(float(month_data[0]["budget"]), 2)

    # Get the months total expenditure and update today's row data.
    if today_date - 2 >= 0:
        total_month_spent = float(month_data[today_date - 2]["total_month_spent"])
    else:
        total_month_spent = 0

    # Calculate limit for today and update today's row data.
    limit = set_limit(today_date, budget, total_month_spent)
    month_data[today_date - 1]["limit"] = limit

    choice = 0
    while choice != 5:
        print(
            "1. Add current expenditure",
            "2. Show today's limit",
            "3. Show today's savings",
            "4. Set changes for the day",
            "5. Exit",
            sep="\n",
        )
        choice = int(input("What action do you want to perform? "))

        today_expend = float(month_data[today_date - 1]["spent"])

        if choice == 1:
            # Get current expenditure value from the user and calculate today's total expenditure.
            current = float(input("How much did you spent today? "))
            today_total = set_today_total(today_expend, current)

            # Update today's row data of the days total expenditure and the months total expenditure.
            month_data[today_date - 1]["spent"] = today_total
            month_data[today_date - 1]["total_month_spent"] = (
                total_month_spent + today_total
            )

        elif choice == 2:
            # Print today's limit.
            print("today's limit is:", limit)

        elif choice == 3:
            # Calculate today's savings and update today's row data.
            saving = set_savings(limit, today_expend)
            month_data[today_date - 1]["saved"] = saving

            if saving < 0:
                print("You overspent today. Saving:", saving)
            else:
                print("Saving:", saving)

        elif choice == 4:
            # Update the CSV file with all the changes.
            update_file()

        elif choice == 5:
            break

        else:
            print("Invalid choice")


def set_limit(today_date, budget, total_month_spent):
    """
    Calculates and returns today's limit.
    """
    return round(((budget - total_month_spent) / days_remaining(today_date)), 2)


def set_today_total(today_expend, current):
    """
    Calculates and returns today's total expenditure.
    """
    return round((today_expend + current), 2)


def set_savings(limit, today_expend):
    """
    Calculates and returns today's total savings.
    """
    return round(limit - today_expend, 2)


def days_remaining(today_date):
    """
    Calculates and returns the number of days left in the current month.
    """
    days = calendar.monthrange(datetime.today().year, datetime.today().month)

    return (days[1] - today_date) + 1


def create_file():
    """
    Creates a new CSV file for the current month with appropriate nomenclature.
    """
    with open(file_name, "w") as file:
        # Get the month's budget from the user.
        budget = float(
            input(
                "Enter your month's budget (Warning! You can't change this information later!): "
            )
        )
        fieldnames = ["date", "limit", "spent", "saved", "total_month_spent", "budget"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        weekd = calendar.weekday(datetime.today().year, datetime.today().month, 1)
        cal = calendar.Calendar(firstweekday=weekd)

        # Write '0' as default values for all attributes except budget.
        # Set budget attribute for all rows equal to the value given by user.
        for i in cal.itermonthdays(datetime.today().year, datetime.today().month):
            if i != 0:
                writer.writerow(
                    {
                        "date": i,
                        "limit": 0,
                        "spent": 0,
                        "saved": 0,
                        "total_month_spent": 0,
                        "budget": budget,
                    }
                )


def read_file():
    """
    Reads a CSV file into a list of dictionaries.
    """
    with open(file_name, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            month_data.append(row)


def update_file():
    """
    Updates the CSV file when the user wants to set all the changes they made for the day.
    """
    with open(file_name, "w") as file:
        fieldnames = ["date", "limit", "spent", "saved", "total_month_spent", "budget"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        weekd = calendar.weekday(datetime.today().year, datetime.today().month, 1)
        cal = calendar.Calendar(firstweekday=weekd)

        for i in cal.itermonthdays(datetime.today().year, datetime.today().month):
            if i != 0:
                total_month_spent = month_data[i - 1]["total_month_spent"]
                if (i - 1) >= (today := (datetime.today().day - 1)):
                    total_month_spent = month_data[today]["total_month_spent"]

                writer.writerow(
                    {
                        "date": month_data[i - 1]["date"],
                        "limit": month_data[i - 1]["limit"],
                        "spent": month_data[i - 1]["spent"],
                        "saved": month_data[i - 1]["saved"],
                        "total_month_spent": total_month_spent,
                        "budget": budget,
                    }
                )


if __name__ == "__main__":
    main()
