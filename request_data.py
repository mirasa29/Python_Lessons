import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta
import os
import time

def fetch_electricity_prices():
    # Calculate the date for the day ahead
    today = datetime.now()
    # Get tomorrow's date for the prediction
    # next_day = today + timedelta(days=1)
    next_day = today + timedelta(days=0) # UPDATE: Changed to today's date for testing
    formatted_date = next_day.strftime("%Y-%m-%d")
    # url = f"https://www.ote-cr.cz/cs/kratkodobe-trhy/elektrina/denni-trh?date={formatted_date}"

    # UPDATE: Added language parameter to the URL to make sure the page is in Czech to set up for text filter at line 30
    url = f"https://www.ote-cr.cz/cs/kratkodobe-trhy/elektrina/denni-trh?date={formatted_date}&set_language=cz"

    try:
        # Send a request to the website
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the specific table containing the price data
        # table = soup.find('table')  # Adjust this selector based on the actual structure

        # OPTION 1: Find the table by index
        # UPDATE: Grab the second table on the page - subject to change if a new table is added to the page
        #table = soup.find_all('table')[1]

        # OPTION 2: Find the table by column names
        # UPDATE: Grab the exact table containing the price per hour data - subject to change if columns are renamed
        table = [tab for tab in soup.findAll('table') if 'Hodina' and 'Cena' in tab.text].pop()

        # Extract data
        # data = []
        # for row in table.find_all('tr')[1:]:  # Skip header row
        #     cols = row.find_all('td')
        #     if len(cols) >= 2:
        #         hour = cols[0].text.strip()
        #         price = cols[1].text.strip().replace(" EUR/MWh", "")  # Clean up the price text
        #         data.append([hour, price])

        # Extract data
        data = []
        for row in table('tr')[1:-1]: # UPDATE: Simplified and Skip header and footer rows
            index = row('th') # UPDATE: First column is a table index which conveniently corresponds to the hour
            cols = row('td') # UPDATE: Simplified
            if index and cols: # UPDATE: Simplified to check if both index and cols are not empty
                hour = int(index[0].text.strip()) # UPDATE: Clean up the hour text and convert to integer
                price = float(cols[0].text.strip().replace(" EUR/MWh", "").replace(",", ".")) # UPDATE: Clean up the price text and convert to float
                data.append([hour, price])
            else:
                raise ValueError("Table structure has changed or no data found")  # UPDATE: Added error handling for missing data or structure changes

        # Create a DataFrame
        df = pd.DataFrame(data, columns=["Hour", "Price (EUR/MWh)"])
        
        # Define the filename for export
        filename = f"electricity_prices_{formatted_date}.csv"
        
        # Check if the directory exists, create if not
        if not os.path.exists('electricity_prices'):
            os.makedirs('electricity_prices')
        
        # Save to CSV
        df.to_csv(os.path.join('electricity_prices', filename), index=False)
        print(f"Data saved to {filename}")
    
    except requests.RequestException as e:
        print(f"Error accessing the website: {e}")
    except Exception as e:
        print(f"An error occurred during data extraction: {e}")

# Example usage
if __name__ == "__main__":
    # Schedule the program to run every day at 5 AM
    # while True:
    #     # Get current time
    #     now = datetime.now()
    #
    #     # Check if current time is 5 AM
    #     if now.hour == 5 and now.minute == 0:
    #         fetch_electricity_prices()
    #         # Wait for one minute to avoid multiple runs in the same minute
    #         time.sleep(60)
    #     else:
    #         # Wait for a while before checking again
    #         time.sleep(30)

    fetch_electricity_prices()


