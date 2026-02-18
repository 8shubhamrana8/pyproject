import sys
import os
from pyfiglet import Figlet
import pandas as pd
import matplotlib.pyplot as plt


def pathcheck():
    while True:

        filepath = input("Enter the csv file path: ")
        if os.path.isfile(filepath):
            print(2 * "\n", "File Loaded")
            df = pd.read_csv(filepath)
            return df, filepath
        else:
            print("No such file at diectory")


def menu(filepath, df):

    while True:
        option = input(
            """
                <<<<<<  MENU  >>>>>>
                (1) Add Expense
                (2) View Summary
                (3) History
                (4) Exit

                Choose an option: """
        )
        print(f"Option {option} choosen")
        if option == "1":
            addexpense(filepath, df)

        elif option == "2":
            summary(df)

        elif option == "3":
            history(df)

        elif option == "4":
            print("Exiting")
            sys.exit()
        else:
            print("Enter Valid input in digits. Thank You!", end="\n")


def budgetoverrun():
    """set parameters given by user plus have ome default parameters
    compare monthly sppending
    tell if it is more and by how much"""
    ...


def getexpense(df):

    year = input("Enter Year: ")
    month = input("Enter Month: ")
    day = input("Enter Day: ")
    date = year + "-" + month + "-" + day

    print("\n" * 2)

    amount = float(input("Enter amount : "))

    print("\n" * 2)

    all_categories = df["Category"].unique()
    cat_dict = {i: category for i, category in enumerate(all_categories, start=1)}

    print("Select Category : ", "\n")

    for num, category in cat_dict.items():
        print(f"({num})--> {category}")
    print("\n" * 2)

    while True:
        usr_cat_num = int(input("Select Category : "))
        if usr_cat_num in cat_dict:
            category = cat_dict[usr_cat_num]
            break
        else:
            print("Invalid choice. Try again.")

    new_expense_format = {"Date": date, "Amount": amount, "Category": category}

    return new_expense_format


def addexpense(filename, df):

    user_data = getexpense(df)
    new_data_df = pd.DataFrame([user_data])
    df = pd.concat([df, new_data_df], ignore_index=True)
    df.to_csv(filename, mode="w", index=False)
    print("\n File updated successfully \n")


def summary(df):
    month_map = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12",
    }
    total = df["Amount"].sum()
    categoryspending = df.groupby("Category", as_index=False)["Amount"].sum()
    categoryspending = categoryspending.sort_values(by="Amount", ascending=False)
    categoryspending["Percentage"] = (categoryspending["Amount"] / total) * 100
    print(categoryspending.to_markdown())
    categoryspending = categoryspending.set_index("Category")
    labels = categoryspending.index

    # Pie chart sizes (percentages)
    sizes = categoryspending["Percentage"]

    # Plotting the pie chart
    plt.figure(figsize=(7, 7))
    plt.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90,
        colors=plt.cm.Paired.colors,
    )
    plt.title("Category Distribution")
    plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

    df[["Year", "Month", "Day"]] = df["Date"].str.split(("-"), expand=True)
    month = input("Enter the month you want to see history of :").strip().title()
    print(month_map[month])

    df.drop(columns="Date", inplace=True)
    filtered_df = df[(df["Month"] == month_map[month])]
    filtered_df = filtered_df[["Day", "Category", "Amount"]]
    filtered_df.reset_index(drop=True, inplace=True)
    print(filtered_df.to_string(), "\n" * 3)


def history(df):

    while True:
        choice = (
            input(
                """
                        
                        Choose option
                        
                        (A) Monthly Spending History of Selected Year
                        
                        (B) Yearly Spending history

                        (C) Exit History
                        
                        Enter Choice ----> """
            )
            .strip()
            .lower()
        )

        if choice == "a":
            yr = int(input("Enter Year : "))
            print("\n" * 2)
            print(f"Filtering Year {yr}", "\n" * 3)
            try:
                df["Date"] = pd.to_datetime(df["Date"])
                filterdf = df[(df["Date"].dt.year == yr)]
                filterdf["Month"] = filterdf["Date"].dt.to_period("M").dt.month
                monthly_expense = (
                    filterdf.groupby("Month")["Amount"].sum().reset_index()
                )
                me = monthly_expense.plot.bar(x="Month", y="Amount", rot=0)
                plt.show()
                break
            except ValueError, IndexError:
                print(f"{yr} Year not found", "\n" * 3)
                continue

        if choice == "b":
            df["Date"] = pd.to_datetime(df["Date"])
            df["Year"] = df["Date"].dt.to_period("Y").dt.year
            yearly_expense = df.groupby("Year")["Amount"].sum().reset_index()
            ye = yearly_expense.plot.bar(x="Year", y="Amount", rot=0)
            plt.show()
            break

        if choice == "c":
            break

        else:
            print("Kindly enter A , B , C. Thank You!!")


def main():
    # ask for csv file

    f = Figlet(font="rounded")
    print(f.renderText("BUDGET TRACKER"))
    data, filepath = pathcheck()
    menu(filepath, data)


main()
