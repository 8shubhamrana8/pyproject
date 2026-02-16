import sys
import os
from pyfiglet import Figlet
import pandas as pd


def pathcheck():
    askagain = True
    while askagain:
        try:    
            filepath = input('Enter the csv file path: ')
            if os.path.isfile(filepath):
                print(2*'\n','File Loaded')
                return filepath
            else:
                print('No such file at diectory')
                askagain = True
        except ValueError:
            print("Invalid Value")
            askagain = False
def menu():
    askagain = True

    while askagain:    
        option = input('''
                <<<<<<  MENU  >>>>>>
                (1) Add Expense
                (2) View Summary
                (3) History
                (4) Exit

                Choose an option: ''')
        print(f'Option {option} choosen')
        if option == '1':
            print('Add expense','\n')
            askagain = False
        elif option == '2':
            print('summary')
            askagain = False
        elif option == '3':
            print('history')
            askagain = False
        elif option == '4':
            print('Exiting')
            sys.exit()
        else:
            print("Enter Valid input in digits. Thank You!", end='\n')
            askagain = True

def budgetoverrun():
    '''set parameters given by user plus have ome default parameters 
       compare monthly sppending
       tell if it is more and by how much'''
    ...

def addexpense(filename, expense):
    '''
    while true
    ask for expense 
    check if valid expense
    if valid enter
    show tail to confirm changes
    ask if want to add again
    return updated csv

    '''
    ...

def summary(filename):
    
    
    
    
    ...
def catspending(filename):
    df = pd.read_csv(filename)
    total = df['Amount'].sum()
    categoryspending = df.groupby('Category').sum()
    categoryspending.drop(columns=['Date'], inplace=True)
    categoryspending = categoryspending.sort_values(by='Amount', ascending=False)
    categoryspending['Percentage'] = (categoryspending['Amount']/total)*100
    return categoryspending.to_markdown()


def history():
    month_map = {
    'January': '01',
    'February': '02',
    'March': '03',
    'April': '04',
    'May': '05',
    'June': '06',
    'July': '07',
    'August': '08',
    'September': '09',
    'October': '10',
    'November': '11',
    'December': '12'
    }
    df =  pd.read_csv('one_year_data.csv')
    df[['Year', 'Month', 'Day']] = df['Date'].str.split(('-'), expand=True)
    month = input('Enter the month you want to see history of :').strip().title()
    print(month_map[month])

    df.drop(columns='Date', inplace=True)
    filtered_df = df[ (df['Month'] == month_map[month])]
    filtered_df = filtered_df[['Day','Category','Amount']]
    filtered_df.reset_index(drop=True, inplace=True)
    print(filtered_df.to_string(),'\n'*3)

def main():
    #ask for csv file
    

    f = Figlet(font = 'rounded')
    print(f.renderText('BUDGET TRACKER'))
    pathcheck()
    menu()

    

    # Trends in spending
    #categoize the data
    #add data
    #total
    # budgeting exceed budget -- over spending under budget show rupees to be spared
    # sort list descending = most expenses
    #menu (1) Add Expense, (2) View Summary, or (3) Histoy, (4) Exit

main()








