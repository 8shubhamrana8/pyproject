📊 Personal Budget Tracker
A robust, command-line interface (CLI) application built with Python to help you track expenses, visualize spending habits, and manage budgets through CSV data.

🌟 Features
Secure Data Entry: Add expenses with multi-layer validation (Type, Range, and Calendar logic).

Visual Summaries: Generate high-quality pie charts showing category distribution and percentage-based spending.

Monthly/Yearly History: Filter and view bar charts of your spending trends over different timeframes.

Budget Overrun Alerts: Set custom budgets for each category and receive visual "Over!" alerts if you exceed them.

Data Integrity: Automatic CSV formatting (zero-padding dates) to ensure data stays machine-readable and sortable.

🛠️ Installation
1. Prerequisites
Ensure you have Python 3.x installed. You will also need the following libraries:

Bash
pip install pandas matplotlib pyfiglet tabulate numpy
2. File Structure
Ensure your CSV file (e.g., expenses.csv) follows this header format:
Date,Amount,Category

🚀 How to Use
Launch the App: Run the script using Python.

Bash
python budget_tracker.py
Load Data: Enter the path to your .csv file when prompted.

Navigate the Menu:

Option 1: Add a new expense.

Option 2: View a pie chart summary of total spending.

Option 3: View historical bar charts (Monthly or Yearly).

Option 4: Set budget limits and check for overspending.

Option 5: Securely exit the application.

🧠 Logic Flow
The application is built on a "Gatekeeper" architecture to ensure no "dirty data" enters your CSV:

Input Validator: Catches non-numeric entries (e.g., typing "Ten" instead of 10).

Lambda Constraints: Prevents logical errors (e.g., entering Month 13).

Calendar Check: Uses datetime logic to catch impossible dates (e.g., February 30th).

Formatting: Automatically converts all dates to YYYY-MM-DD for perfect sorting.

📈 Example Visualization
When you view your Budget Overrun, the app generates a side-by-side comparison bar chart:

Blue Bars: Your actual spending.

Red Bars: Your budgeted limit.

Red Text: An "Over!" tag specifically for categories that exceeded the limit.

📄 License
This project is open-source and free to use for personal financial management.