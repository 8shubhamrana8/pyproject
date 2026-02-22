📊 Personal Budget Tracker -- By Shubham
    #### Video Demo:  <URL HERE>
    #### Description:

    🌟project.py:

    This is the core of my project as it contains the main execution loop plus all the core logic functions used in the programme such as:

    🚀 pathcheck(): This function makes sure that there exists a CSV file at the user mentioned path before attempting to load pandas, thus making sure programme dosen't crash.

    🚀 check_valid_input(): Tired of validating user input as clean and valid, this fumction helps me to check if the user input is clean , in right type plus as a bonus one can enforce rules like input must be greater than 0 by passing the condition before data is accepted.

    🚀 menu(): Provides a clean CLI interface for the user with followin options to choose from:

        Option 1: Add a new expense.

        Option 2: View a pie chart summary of total spending.

        Option 3: View historical bar charts (Monthly or Yearly).

        Option 4: Set budget limits and check for overspending.

        Option 5: Securely exit the application.

    🚀 getexpense() & addexpense(): These functions handle all the user interface for entring new data and the back-end logic for appending that data to tha CSV file.

    🚀 summary() & history(): These functions take advantage of the Pandas and Matplotlib libraries to aggregate data and represent or visualize data respectively.

    🌟test_project.py

    To make sure of the reliability of the programmme this file contains a number of tests designed to work in tandem with Pytest. It mainly focuses on the pure functions that take specific inputs and return outputs that are predictaible and without any errors.

    By testing check_valid_date, getpercentage, and no_duplicate, we make sure that the logical foundation of the said functions is sound even if it is called at different scenarios.

    🌟requirements.txt

    This file lists all the external dependencies required to run my project. It includes the following

    1. Pandas --->  Used for data manipulation in different functions like summary, history and for data entry.
    2. Matplotlib ---> Used fpr representing graphs and pie charts to make the data look more appealing and is easy to understand people.
    3. Pyfiglet ---> Used for ASCII art styling
    4. NumPy --> Used NumPy specifically within the function budgetoverrun to handle the visual layout of your "Budget vs. Actual" comparison bar chart.

    🌟Design choices/Paths I took

    1. Data Entry:
    In starting I considered allowing user to enter free text but this leads to multiple issues like two distict categories for Grocery and groceries plus if a user entered wrong category , my programme could not assist user in correcting it. Therfore I choose to extract the categories from the existing CSV file and presented them in a numbered format.This ensured data consistency.
    I also debated adding a "New Category" option but decided to keep the current version focused on maintaining a clean, existing schema to prevent "category bloat."

    2. Data Representation:
    Initially I was seeking to present my data in a tabular format. But not only it complicates the presenting data in terminal but also limits the user to make quick assements to his/her data. It is therefore I started to learn Pandas and Matplotlib to represent my data beautifully in form of pie charts and bar graphs.

    🌟 Conclusion:
    My project demonstrates pythons data science libraries like Pandas, Matplotlib, Numpy and combines it with user centric CLI design. It gives the user's CSV file a whole new meaning with clean data representation plus guards against human error.    

