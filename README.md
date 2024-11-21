Mutual Fund Data Scraper
Description
This script fetches mutual fund data (including daily NAV values) from the AMFI website and stores it in a persistent database. It supports fetching data for a specific date range, replaces missing values with NA, and avoids inserting duplicate records into the database.

Designed to be run daily, the script ensures accurate and up-to-date storage of mutual fund information.

Features
Fetch mutual fund data for a given date range.
Replace blank columns with NA.
Store data in a SQLite database for persistence.
Prevent duplicate entries in the database.
Modular and extensible codebase for easy maintenance.
Robust error handling and validation.
Prerequisites
Python 3.7 or higher.
Required Python libraries:
requests
pandas
sqlite3 (comes with Python standard library)
To install required libraries, run:

bash
Copy code
pip install pandas requests
Setup and Execution
1. Clone the Repository
Download or clone this repository to your local system:

bash
Copy code
git clone <repository-url>
cd <repository-folder>
2. Run the Script
The script can be executed using Python:

bash
Copy code
python mutual_fund_scraper.py
By default, it fetches and stores data for the current date.

Configuration
Modify Date Range
To fetch data for a specific date range, edit the fetch_mutual_fund_data function call in the script:

python
Copy code
data = fetch_mutual_fund_data("03-May-2023", "04-May-2023")
Change Database
By default, the script stores data in a SQLite database named mutual_funds.db.
To change the database name or location, update the save_to_db function:

python
Copy code
conn = sqlite3.connect("your_database_name.db")
Automation
To automate the script for daily execution, use a task scheduler:

Linux: Set up a cron job.
Windows: Use Task Scheduler.
Python Scheduler: Add the schedule library to run the script at a specific time.
Example using schedule:

python
Copy code
import schedule
import time

schedule.every().day.at("02:00").do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
Database Structure
The script creates a table named mutual_funds with the following schema:

Column Name	Data Type	Description
scheme_code	INTEGER	Unique identifier for the scheme.
scheme_name	TEXT	Name of the mutual fund scheme.
isin_div_payout	TEXT	ISIN for dividend payout.
isin_growth	TEXT	ISIN for growth.
net_asset_value	REAL	Daily NAV value.
repurchase_price	REAL	Repurchase price (if available).
sale_price	REAL	Sale price (if available).
date	TEXT	Date for the NAV value.
Error Handling
The script includes robust error handling:

Network Issues: Validates URL responses and retries if necessary.
Database Issues: Catches and logs errors during database operations.
Data Integrity: Ensures missing columns are replaced with NA.
Future Improvements
Add support for PostgreSQL or MySQL for large-scale data.
Improve performance with multithreading for large date ranges.
Add detailed logging using Python's logging module.
Contributing
Feel free to fork the repository and submit pull requests with improvements or bug fixes.