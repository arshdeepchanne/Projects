# Expense Tracker
#### Video Demo:  <URL https://www.youtube.com/watch?v=4KQVtfA_8lE>
#### Description:
The idea for this project comes from my personal (somewhat unpleasant) experiences of not being able to manage my money correctly.
 
As a college student, it can be challenging to keep track of daily expenses. Small transactions made over a few days can add up, resulting in a money crisis by the end of the month or confusion about where all the money went.
 
To solve this problem I came up with the idea of an Expense Tracker, which, as the name suggests, helps you track your expenses. The [project.py](project.py) file has the code for the program.
 
The program works in the following way-
 
- A CSV file stores all of the data for the current month. The nomenclature of the file is: expense-sheet-(year)-(month).csv
 
- If the user wants to create a new CSV file for the month, they can do so by specifying the command line argument `new`.
    - Usage: `python project.py [new]`
    - If the user wants to continue using an existing file, there is no need to specify the `new` command-line argument.
 
- The CSV stores the following attributes-
    - Date.
    - Limit for the day.
    - Expenditure of the day.
    - Money saved in the day.
    - Total amount of money spent in the month.
    - Budget for the month.
 
- If the user is creating a new file, they will be prompted to set a budget for the month. Afterward, they will be presented with a menu of actions they can perform, such as adding a new expenditure, viewing the daily limit, viewing the daily savings, and updating the CSV file with any new data they provide.
 
For the purposes of CS50P, I have limited this program to a command-line application. However, as a future project, I plan to implement it as an Android application and later as an iOS application with additional features.
 