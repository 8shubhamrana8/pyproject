import sys
import os
from pyfiglet import Figlet
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np


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
                (4) Check Budget Overrun
                (5) Exit

                Choose an option: """
        )
        print(f"Option {option} choosen")
        if option == "1":
            df = addexpense(filepath, df)

        elif option == "2":
            summary(df)
            show_monthly_expenses(df)
            

        elif option == "3":
            history(df)

        elif option == "4":
            budgetoverrun(df)

        elif option == "5":
            print("Exiting")
            sys.exit()
        else:
            print("Enter Valid input in digits. Thank You!", end="\n")


def budgetoverrun(df):

    budget_dict = {}
    categories = no_duplicate(df["Category"].to_list())
    for category in categories:
        budget = float(input(f"Set Budget for {category}--> $"))
        budget_dict[category] = budget

    category_spending = df.groupby("Category", as_index=False)["Amount"].sum()
    category_spending["Budget"] = category_spending["Category"].map(budget_dict)
    category_spending["Overrun"] = (
        category_spending["Amount"] - category_spending["Budget"]
    )
    over_limit = category_spending[category_spending["Overrun"] > 0]

    if not over_limit.empty:
        print("\n⚠️ Alert: You exceeded your budget in these categories:")
        print(over_limit[["Category", "Overrun"]])
    else:
        print("\n✅ Great job! You are within budget for all categories.")

    labels = category_spending["Category"]
    actual = category_spending["Amount"]
    budget = category_spending["Budget"]

    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(x - width / 2, actual, width, label="Actual Spent", color="#3498db")
    ax.bar(x + width / 2, budget, width, label="Budgeted", color="#e74c3c", alpha=0.7)

    ax.set_ylabel("Amount ($)")
    ax.set_title("Budget vs. Actual Spending by Category")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    for i, val in enumerate(category_spending["Overrun"]):
        if val > 0:
            ax.text(
                i - width / 2,
                actual[i] + 1,
                "Over!",
                color="red",
                fontweight="bold",
                ha="center",
            )

    plt.tight_layout()
    plt.savefig("budget_analysis.png")
    plt.show()


def check_valid_date(year, month, day):
    try:
        datetime(int(year), int(month), int(day))
        return True
    except ValueError:
        return False


def getexpense(df):

    while True:
        year = input("Enter Year: ")
        month = input("Enter Month: ")
        day = input("Enter Day: ")
        if check_valid_date(year, month, day):
            date = year + "-" + month + "-" + day
            break
        else:
            print("Enter valid date \n")

    print("\n" * 2)

    amount = float(input("Enter amount : "))

    print("\n" * 2)

    all_categories = df["Category"].unique()
    cat_dict = {i: category for i, category in enumerate(all_categories, start=1)}

    print("Select Category : \n")

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


def getpercentage(value, total):
    if total == 0:
        return 0.0
    return round((value / total) * 100, 2)


def addexpense(filename, df):

    user_data = getexpense(df)
    new_data_df = pd.DataFrame([user_data])
    df = pd.concat([df, new_data_df], ignore_index=True)
    df.to_csv(filename, mode="w", index=False)
    print("\n File updated successfully \n")
    return df


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
    categoryspending["Percentage"] = getpercentage(categoryspending["Amount"], total)
    print(categoryspending.to_markdown())

    categoryspending = categoryspending.set_index("Category")
    labels = categoryspending.index

    sizes = categoryspending["Percentage"]

    plt.figure(figsize=(7, 7))
    plt.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90,
        colors=plt.cm.Paired.colors,
    )
    plt.title("Category Distribution")
    plt.axis("equal")
    plt.show()


def no_duplicate(datalist):
    outputlist = []
    for data in datalist:
        if data in outputlist:
            pass
        else:
            outputlist.append(data)
    return sorted(outputlist)


def show_monthly_expenses(df):
    copydf = df.copy()
    copydf["Date"] = pd.to_datetime(copydf["Date"])
    copydf["Year-Month"] = copydf["Date"].dt.strftime("%Y-%m")
    copydf["Day"] = copydf["Date"].dt.strftime("%d")

    unq_date = no_duplicate(copydf["Year-Month"].tolist())

    while True:
        usr_date = input("\n Enter year and month (YYYY-MM) : ")
        if usr_date in unq_date:
            data = copydf[(copydf["Year-Month"] == usr_date)]
            data = data[["Day", "Category", "Amount"]]
            data = data.set_index("Day")
            print(data.to_string())
            break
        else:
            print("\n Date Not Found")


def history(df):

    while True:
        choice = (
            input(
                """
                        
                        Choose an option:
                        
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
                filterdf = df[(df["Date"].dt.year == yr)].copy()
                filterdf["Month"] = filterdf["Date"].dt.to_period("M").dt.month
                monthly_expense = (
                    filterdf.groupby("Month")["Amount"].sum().reset_index()
                )
                me = monthly_expense.plot.bar(x="Month", y="Amount", rot=0)
                plt.show()
                break
            except (ValueError, IndexError):
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

    f = Figlet(font="rounded")
    print(f.renderText("BUDGET TRACKER"))
    data, filepath = pathcheck()
    menu(filepath, data)


main()
