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
            print("⚠️⚠️⚠️  No such file at diectory  ⚠️⚠️⚠️")



def check_valid_input(prompt, input_type, condition = None, error_msg = "\n⚠️⚠️⚠️ INVALID INPUT ⚠️⚠️⚠️\n" ):
    while True:
        try:
            value = input_type(input(prompt))
            if condition:
                if not condition(value):
                    print(error_msg)
                    continue
            return value
        except ValueError:
            print(f"⚠️⚠️⚠️   Please enter a valid {input_type.__name__}.  ⚠️⚠️⚠️")



def check_valid_date(year, month, day):
    try:
        datetime(int(year), int(month), int(day))
        return True
    except ValueError:
        return False



def getpercentage(value, total):
    if total == 0:
        return 0.0
    return round((value / total) * 100, 2)



def no_duplicate(datalist):
    outputlist = []
    for data in datalist:
        if data in outputlist:
            pass
        else:
            outputlist.append(data)
    return sorted(outputlist)



def menu(filepath, df):

    while True:
        option = check_valid_input(
            """
                <<<<<<  MENU  >>>>>>

                (1) Add Expense
                
                (2) View Summary
                
                (3) History
                
                (4) Check Budget Overrun
                
                (5) Exit

                Choose an option: """, str
        )
        option.strip().lower()
        print(f"Option {option} choosen")
        if option == "1" or option == "add expense":
            print(f"\n✅✅✅ Add Expense to your CSV file ✅✅✅\n")
            df = addexpense(filepath, df)

        elif option == "2" or option == "summary":
            print(f"\n✅✅✅ Loading Summary ✅✅✅\n")
            summary(df)
            show_monthly_expenses(df)
            

        elif option == "3" or option == "history" :
            print(f"\n✅✅✅ Loading History ✅✅✅\n")
            history(df)

        elif option == "4" or option == "check budget overrun":
            print(f"\n✅✅✅ Loading Budget Overrun ✅✅✅\n")
            budgetoverrun(df)

        elif option == "5" or option == "exit":
            print("\nExiting!!! Thank You for using this programme!!!!!\n")
            sys.exit()
        else:
            print("⚠️⚠️⚠️   Enter Valid input in digits. Thank You!  ⚠️⚠️⚠️\n")



def getexpense(df):

    while True:
        year = check_valid_input(prompt="\nEnter Year: ",
                                input_type=int,
                                condition=lambda x: x>0,
                                error_msg="⚠️⚠️⚠️  Invalid Year  ⚠️⚠️⚠️")
        month = check_valid_input(prompt="\nEnter Month: ",
                                input_type=int,
                                condition=lambda x: 0<x<13,
                                error_msg="⚠️⚠️⚠️  Please check the month (1-12)  ⚠️⚠️⚠️")
        day = check_valid_input(prompt="\nEnter Day: ",
                                input_type=int,
                                condition=lambda x: 0<x<32,
                                error_msg="⚠️⚠️⚠️  Please check the days (1-31)  ⚠️⚠️⚠️")
        if check_valid_date(year, month, day):
            date = f"{year}-{month:02}-{day:02}"
            break
        else:
            print("⚠️⚠️⚠️   Invalid Date! Please check the month (1-12) and days (1-31).   ⚠️⚠️⚠️ \n")


    print("\n" * 2)
    
    amount = check_valid_input("Enter amount : ", float, lambda x: x > 0)

    print("\n" * 2)

    all_categories = no_duplicate(df["Category"].tolist())
    category_dict = {i: category for i, category in enumerate(all_categories, start=1)}
    category_keys = list(category_dict.keys())
    print("Select Category : \n")

    for num, category in category_dict.items():
        print(f"({num})--> {category}")
    print("\n" * 2)


     
    usr_cat_num = check_valid_input(
        prompt="Select Category : ", 
        input_type=int,
        condition = lambda x: x in category_dict,
        error_msg = "\n⚠️⚠️⚠️   Invalid choice. Try again.   ⚠️⚠️⚠️\n"
        )

    category = category_dict[usr_cat_num]


    new_expense_format = {"Date": date, "Amount": amount, "Category": category}

    return new_expense_format



def addexpense(filename, df):

    user_data = getexpense(df)
    new_data_df = pd.DataFrame([user_data])
    df = pd.concat([df, new_data_df], ignore_index=True)
    df.to_csv(filename, mode="w", index=False)
    print("\n✅✅✅   File updated successfully   ✅✅✅\n")
    return df



def summary(df):

    if df.empty:
        print("\n⚠️⚠️⚠️ CSV EMPTY  ⚠️⚠️⚠️\n")
        return

    total = df["Amount"].sum()
    print(f"\n TOTAL SPENDING = ${total:,.2f}\n")
    categoryspending = df.groupby("Category", as_index=False)["Amount"].sum()
    categoryspending = categoryspending.sort_values(by="Amount", ascending=False)
    categoryspending["Percentage"] = getpercentage(categoryspending["Amount"], total)
    print(categoryspending.to_markdown(index=False))

    categoryspending = categoryspending.set_index("Category")
    
    
    plt.style.use('dark_background')
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
    plt.title(f"Category Distribution (TOTAL: ${total:,.2f})")
    plt.axis("equal")
    
    plt.show()



def show_monthly_expenses(df):
    copydf = df.copy()
    copydf["Date"] = pd.to_datetime(copydf["Date"])
    copydf["Year-Month"] = copydf["Date"].dt.strftime("%Y-%m")
    copydf["Day"] = copydf["Date"].dt.strftime("%d")

    unq_date = no_duplicate(copydf["Year-Month"].tolist())

 
    usr_date = check_valid_input(
                prompt="\n Enter year and month (YYYY-MM) : ",
                input_type= str,
                condition= lambda x: x in unq_date,
                error_msg="⚠️⚠️⚠️  Date Not Found! Please choose from the list above.  ⚠️⚠️⚠️"
                                    )

    data = copydf[(copydf["Year-Month"] == usr_date)]
    data = data[["Day", "Category", "Amount"]]
    data = data.set_index("Day")
    print(data.to_markdown())



def budgetoverrun(df):

    budget_dict = {}
    categories = no_duplicate(df["Category"].to_list())
    print("\n"*3)
    for category in categories:
        budget = check_valid_input( prompt=f"Set Budget for {category}--> $", 
                                    input_type = float, 
                                    condition=lambda x : x > 0,
                                    error_msg=f"⚠️⚠️⚠️INVALID INPUT!! Setting budget for {category} to $0.00⚠️⚠️⚠️"
                                    )
        budget_dict[category] = budget


    category_spending = df.groupby("Category", as_index=False)["Amount"].sum()
    category_spending["Budget"] = category_spending["Category"].map(budget_dict)
    category_spending["Overrun"] = (category_spending["Amount"] - category_spending["Budget"])
    
    over_limit = category_spending[category_spending["Overrun"] > 0]

    if not over_limit.empty:
        print("\n⚠️⚠️⚠️ Alert: You exceeded your budget in these categories: ")
        
        print("\n"*2,over_limit[["Category", "Overrun"]].to_markdown(index= False))
    else:
        print("\n✅✅✅  Great job! You are within budget for all categories.  ✅✅✅")
    
    plt.style.use('dark_background')
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
    plt.show()



def history(df):

    while True:
        choice = check_valid_input(
                """
                        
                        Choose an option:
                        
                        (A) Monthly Spending History of Selected Year
                        
                        (B) Yearly Spending history

                        (C) Exit History
                        
                        Enter Choice ----> """,
                        str
            )
        choice = choice.strip().lower()
        data_years = no_duplicate(df["Date"].dt.year.tolist())

        if choice == "a":
            yr = check_valid_input(
                prompt="Enter Year : ",
                input_type=int,
                condition=lambda x: x in data_years,
                error_msg="\n ⚠️⚠️⚠️  Invalid Year ⚠️⚠️⚠️"
                )
            print("\n" * 2)
            print(f"Filtering Year {yr}", "\n" * 3)
            try:
                df["Date"] = pd.to_datetime(df["Date"])
                filterdf = df[(df["Date"].dt.year == yr)].copy()
                filterdf["Month"] = filterdf["Date"].dt.to_period("M").dt.month
                monthly_expense = (
                    filterdf.groupby("Month")["Amount"].sum().reset_index()
                )
                if monthly_expense.empty:
                    return
                plt.style.use('dark_background')
                monthly_expense.plot.bar(x="Month", y="Amount", rot=0)
                print(f"\n Showing monthly spending of year {yr} \n")
                plt.show()
                break
            except (ValueError, IndexError):
                print(f"⚠️⚠️⚠️   Year {yr} not found   ⚠️⚠️⚠️", "\n" * 3)
                continue

        if choice == "b":
            df["Date"] = pd.to_datetime(df["Date"])
            df["Year"] = df["Date"].dt.to_period("Y").dt.year
            yearly_expense = df.groupby("Year")["Amount"].sum().reset_index()
            yearly_expense.plot.bar(x="Year", y="Amount", rot=0)
            plt.show()
            break

        if choice == "c":
            break

        else:
            print("\n⚠️⚠️⚠️    Kindly enter A , B , C. Thank You!!   ⚠️⚠️⚠️\n")



def main():

    f = Figlet(font="rounded")
    print(f.renderText("BUDGET TRACKER"))
    data, filepath = pathcheck()
    menu(filepath, data)


main()
