'''
Phase 1: Data Architecture
Before you can analyze money, you need a place to put it.

Define the Schema: Decide what a single transaction looks like (Date, Amount, Category, Description).

Setup CSV/JSON: Create a transactions.csv file with some dummy data.

File I/O Functions: Write a function to load the data into a list of dictionaries and a function to save new entries back to the file.
'''

'''
Phase 2: Core Logic (The "CS50P" Part)
This is where your three required functions and pytest files will likely live.

The Categorizer: Write a function that uses Regular Expressions to scan descriptions.

Task: If description contains "Uber" or "Lyft", return "Transport".

The Calculator: Create a function that sums up totals by category.

Task: Input: List of dicts. Output: A dictionary like {"Food": 150.00, "Rent": 1000.00}.

The Validator: Write a function to ensure user input is a valid positive float (to prevent your program from crashing if someone types "five dollars").
'''















'''
Phase 3: The User Interface (CLI)
Make it interactive using the input() loop.

Main Menu: Create a loop where users can choose to (1) Add Expense, (2) View Summary, or (3) Exit.

The "Add" Flow: Prompt for amount and description, auto-categorize it using your Phase 2 logic, and save it.

The "View" Flow: Use the tabulate library to print the CSV data in a clean, readable table.
'''


















'''
Phase 4: Polish & Visualization
Data Summary: Print a "Budget Status" report (e.g., "You have spent 80% of your Food budget").

Visuals: Add a function that uses matplotlib to save a simple pie chart (chart.png) based on your category totals.
'''






'''
Gemini said
To push your Personal Finance Dashboard from "good" to "CS50P Great," you want to add features that show off Python’s ability to handle data visualization, automation, and robust error handling.

Here are four feature sets that fit perfectly into the "moderate" difficulty bracket:

1. Automated "Monthly Report" (PDF Generation)
Instead of just printing text to the terminal, generate a physical report.

The Library: Use fpdf or reportlab.

Why it's cool: It transforms your script into a professional tool.

Tasks:

Create a function generate_pdf_report(data, month) that summarizes totals.

Include a "Top 3 Categories" list and a "Total Spent" highlight.

Use the datetime library to name the file automatically (e.g., Report_Feb_2026.pdf).

2. Interactive "Goal Tracker"
Add a feature where you set a savings goal (e.g., "$1,000 for a new PC") and the program tracks your progress.

The Logic: Store a goals.json file.

Why it's cool: It adds a "state" to your app—the program remembers your goals even after you close it.

Tasks:

Write a function to calculate the percentage of the goal reached:

Percentage=( 
Goal Amount
Current Savings
​
 )×100
Use a "Progress Bar" in the terminal (you can build a simple one using strings like [#####-----] 50%).

3. CSV Bulk Import (Data Cleaning)
Manually typing every expense is boring. Let the user point your program at a CSV file exported from their actual bank.

The Library: csv (built-in).

Why it's cool: It solves the "garbage in, garbage out" problem by cleaning messy bank data.

Tasks:

Write a function clean_bank_csv(filepath) that ignores unnecessary columns (like "Transaction ID" or "Status") and extracts only Date, Description, and Amount.

Use Try/Except blocks to handle cases where the file doesn't exist or is formatted incorrectly.

4. Recurring Subscription Detector
Since you are already using Regex, you can look for patterns that repeat every month.

The Logic: Compare dates and descriptions.

Why it's cool: It feels "smart"—the program can tell you, "Hey, you spent $15.99 on Netflix last month and this month; that looks like a subscription."

Tasks:

Build a function that scans the transaction list for identical descriptions occurring roughly 30 days apart.

Print a summary of your "Fixed Monthly Costs."

Suggested "Menu" Structure
If you add these, your main() loop will look like a real application:

Option	Function Name	CS50P Concept Used
1. Add Expense	add_entry()	User Input & File I/O
2. Import Bank File	import_csv()	File Handling & Exception Handling
3. View Stats	get_summary()	Loops & Dictionaries
4. Export PDF	save_report()	External Libraries (fpdf)
5. Goal Status	check_goals()	Math & Logic
'''