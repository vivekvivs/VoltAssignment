import requests
import pandas as pd
from datetime import datetime
from db_handler import save_to_db
from config import DATA_URL

def fetch_data(from_date, to_date):
    try:
        url = DATA_URL.format(from_date=from_date, to_date=to_date)
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def parse_data(raw_data):
    try:
        # Split data into sections
        lines = raw_data.split("\n")
        sections = [line for line in lines if ";" in line]

        # Load data into a DataFrame
        data = pd.DataFrame(
            [line.split(";") for line in sections],
            columns=["Scheme Code", "Scheme Name", "ISIN Div Payout",
                     "ISIN Growth", "Net Asset Value",
                     "Repurchase Price", "Sale Price", "Date"]
        )

        # Replace blanks with 'NA'
        data.fillna("NA", inplace=True)
        return data
    except Exception as e:
        print(f"Error parsing data: {e}")
        return None


def main(from_date, to_date):
    raw_data = fetch_data(from_date, to_date)
    if raw_data:
        parsed_data = parse_data(raw_data)
        if parsed_data is not None:
            save_to_db(parsed_data)

if __name__ == "__main__":
    from_date = "01-Jan-2023"
    to_date = "01-Jan-2024"
    main(from_date, to_date)
