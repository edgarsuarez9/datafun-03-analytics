"""Project Demonstrates skill in fetching data, processing, and git push command"""

# Standard Library imports
import csv
import json
import pathlib
import pandas as pd

# External library imports (requires virtual environment)
import requests

# Local module imports
import suarez_projsetup  
import utils_suarez      

# Data Acquisition
def fetch_and_write_txt_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_txt_file(folder_name, filename, response.text)
    else:
        print(f"Failed to fetch TXT data: {response.status_code}")

def fetch_and_write_csv_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_csv_file(folder_name, filename, response.content)
    else:
        print(f"Failed to fetch CSV data: {response.status_code}")

def fetch_and_write_json_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_json_file(folder_name, filename, response.text)
    else:
        print(f"Failed to fetch JSON data: {response.status_code}")

def fetch_and_write_excel_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_excel_file(folder_name, filename, response.content)
    else:
        print(f"Failed to fetch Excel data: {response.status_code}")

# Write Data
def write_txt_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name) / filename
    file_path.write_text(data)
    print(f"Text data saved to {file_path}")

def write_csv_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name) / filename
    with open(file_path, 'wb') as file:
        file.write(data)
    print(f"CSV data saved to {file_path}")

def write_json_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name) / filename
    with open(file_path, 'w') as file:
        file.write(data)
    print(f"JSON data saved to {file_path}")

def write_excel_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name) / filename
    with open(file_path, 'wb') as file:
        file.write(data)
    print(f"Excel data saved to {file_path}")

# Process and Generate Output
def process_txt_file(folder_name, filename, result_filename):
    file_path = pathlib.Path(folder_name) / filename
    result_path = pathlib.Path(folder_name) / result_filename
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        # Process data if needed
        with open(result_path, 'w') as file:
            file.write(data)  # For demonstration, just writing back the same data
        print(f"Processed text data saved to {result_path}")
    except Exception as e:
        print(f"Error processing text file: {e}")

def process_csv_file(folder_name, filename, result_filename):
    file_path = pathlib.Path(folder_name) / filename
    result_path = pathlib.Path(folder_name) / result_filename
    try:
        with open(file_path, 'rb') as file:
            data = file.read().decode('utf-8').splitlines()
        reader = csv.reader(data)
        rows = [row for row in reader]
        # Process data if needed
        with open(result_path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print(f"Processed CSV data saved to {result_path}")
    except Exception as e:
        print(f"Error processing CSV file: {e}")

def process_json_file(folder_name, filename, result_filename):
    file_path = pathlib.Path(folder_name) / filename
    result_path = pathlib.Path(folder_name) / result_filename
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        # Process data if needed
        with open(result_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Processed JSON data saved to {result_path}")
    except Exception as e:
        print(f"Error processing JSON file: {e}")

def process_excel_file(folder_name, filename, result_filename):
    file_path = pathlib.Path(folder_name) / filename
    result_path = pathlib.Path(folder_name) / result_filename
    try:
        data = pd.read_excel(file_path, sheet_name=None)
        with open(result_path, 'w') as file:
            for sheet_name, df in data.items():
                file.write(f"Sheet: {sheet_name}\n")
                file.write(df.to_csv(index=False))
                file.write("\n")
        print(f"Processed Excel data saved to {result_path}")
    except Exception as e:
        print(f"Error processing Excel file: {e}")

# Main Function
def main():
    ''' Main function to demonstrate module capabilities. '''

    # URL definitions
    txt_url = 'https://github.com/denisecase/datafun-03-spec/raw/main/data.txt'
    csv_url = 'https://github.com/denisecase/datafun-03-spec/raw/main/data.csv'
    excel_url = 'https://github.com/denisecase/datafun-03-spec/raw/main/data.xls'
    json_url = 'https://github.com/denisecase/datafun-03-spec/raw/main/data.json'

    # Folder and file names
    txt_folder_name = 'data-txt'
    csv_folder_name = 'data-csv'
    excel_folder_name = 'data-excel'
    json_folder_name = 'data-json'

    txt_filename = 'data.txt'
    csv_filename = 'data.csv'
    excel_filename = 'data.xls'
    json_filename = 'data.json'

    # Create directories if they don't exist
    pathlib.Path(txt_folder_name).mkdir(exist_ok=True)
    pathlib.Path(csv_folder_name).mkdir(exist_ok=True)
    pathlib.Path(json_folder_name).mkdir(exist_ok=True)
    pathlib.Path(excel_folder_name).mkdir(exist_ok=True)

    # Fetch and write data
    fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)
    fetch_and_write_csv_data(csv_folder_name, csv_filename, csv_url)
    fetch_and_write_excel_data(excel_folder_name, excel_filename, excel_url)
    fetch_and_write_json_data(json_folder_name, json_filename, json_url)

    # Process data
    process_txt_file(txt_folder_name, txt_filename, 'results_txt.txt')
    process_csv_file(csv_folder_name, csv_filename, 'results_csv.txt')
    process_excel_file(excel_folder_name, excel_filename, 'results_excel.txt')
    process_json_file(json_folder_name, json_filename, 'results_json.txt')

if __name__ == '__main__':
    main()


