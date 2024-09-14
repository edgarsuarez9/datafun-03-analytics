# Opening DocString
''' This module provides functions for creating a series of project folders. '''

# Import Dependencies
import pathlib
import utils_suarez
import time
from datetime import datetime, timedelta

# Create a path object
project_path = pathlib.Path.cwd()

# Define the new sub folder path
data_path = project_path.joinpath('data')

# Create new if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

# Define functions for folders
def create_folders_for_range(start_year: int, end_year: int) -> None:
    '''
    Create folders for a given range of years.
    '''
    for year in range(start_year, end_year + 1):
        year_folder = data_path / str(year)
        year_folder.mkdir(exist_ok=True)
        time.sleep(1)
        print(f"Created Folder for: {year}")
        
def create_folders_from_list(folder_list: list, to_lowercase: bool = True, remove_spaces: bool = True) -> None:
    '''Create folders from the provided list with optional transformations.'''
    for folder_name in folder_list:
        # Apply transformations if specified
        if to_lowercase:
            folder_name = folder_name.lower()
        if remove_spaces:
            folder_name = folder_name.replace(' ', '_')

        folder_path = data_path / folder_name
        folder_path.mkdir(exist_ok=True)
        print(f"Created folder for: {folder_name}")
        time.sleep(1)
    
def create_prefixed_folders(folder_list: list, prefix: str) -> None:
    '''Function to add a prefix to folders'''
    for folder_name in folder_list:
        folder_path = data_path / f"{prefix}{folder_name}"
        folder_path.mkdir(exist_ok=True)
        print(f"Created folder: {folder_path}")

def create_folders_periodically(folder_count: int, duration_seconds: int) -> None:
    '''Function to create folders periodically'''
    # Calculate the end time based on the duration
    end_time = datetime.now() + timedelta(seconds=duration_seconds)
    
    # Initialize folder index
    folder_index = 1
    
    # Loop until the current time exceeds the end time
    while datetime.now() < end_time:
        # Create a folder name with an index
        folder_name = f"folder_{folder_index}"
        folder_path = data_path / folder_name
        folder_path.mkdir(exist_ok=True)
        print(f"Created folder: {folder_name}")
        
        # Increment the folder index
        folder_index += 1
        
        # Wait for the specified time before creating the next folder
        # Adjust sleep to avoid overlapping folder creation
        time.sleep(duration_seconds / folder_count)

# Define Main Function
def main():
    ''' Main function to demonstrate module capabilities. '''

    # Start of main execution
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")

    print(f"Byline: {utils_suarez.get_byline()}")
    
    # Call function 1 to create folders for a range (e.g., years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using a prefix
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically
    create_folders_periodically(folder_count=3, duration_seconds=15)

    # Add options e.g., to force lowercase and remove spaces 
    # to one or more of your functions (e.g., function 2)
    regions = [
        "North America", 
        "South America", 
        "Europe", 
        "Asia", 
        "Africa", 
        "Oceania", 
        "Middle East"
    ]
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")

# Conditional Script
# At the end of the file 
if __name__ == '__main__':
    main()