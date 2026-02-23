from datetime import datetime
import pandas as pd 

def clean_currency(price_str):
    """
    Takes a string like "$1,200.50" or "€ 50.00" and returns a float 1200.50.
    If input is None or empty, return 0.0.
    """
    try:
        price_str = str(price_str)
        clean_str = price_str.strip().replace("$", "").replace("€", "").replace(",", "")
        return float(clean_str)
    except:
        return 0.0

    

def parse_timestamp(date_str):
    """
    Takes a string in format "MM/DD/YYYY" and returns "YYYY-MM-DD".
    If the date is invalid or None, return None.
    Hint: Use datetime.strptime() and strftime(), or try/except blocks.
    """
    try:
        date_str = str(date_str)
        return datetime.strptime
    except:
        return None

def summarize_sales(transactions):
    """
    Takes a list of dictionaries: [{'category': 'A', 'amount': 10}, {'category': 'A', 'amount': 20}]
    Returns a dictionary summing amounts by category: {'A': 30}
    """
