''' ITERATION 5

Module: Suarez Analytics - Company and Client Information

'''

#####################################
# Import modules at the Top
#####################################

import statistics

#####################################
# Declare a global variables
#####################################

# Boolean variable to indicate if the company has international clients
has_international_clients: bool = True

# Boolean variable to indicate if company has a dog
has_pet_dog: bool = True

# Integer variable for the number of years in operation
years_in_operation: int = 10

# Integer variable for number of dogs company owns
dogs_company_owns: int = 2

# Float variable for the average client satisfaction scores
average_client_satisfaction: float = 4.7

# Float variable for the average company ages
average_company_age: float = 30

# List of strings representing the skills offered by the company
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]

# List of name of all pets owned by company
company_pet_names: list = ["Victor", "Maggie", "Charlie"]

# List of floats representing individual client satisfaction scores
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]

# List of ages of those in the company_pet_names
current_company_ages: list = [3, 6, 30, 33, 45, 60]

#####################################
# Calculate Basic statistics
#####################################

# Calculate basic stats using built-in functions min(), max(), and statistics module functions mean() and stdev().
min_score: float = min(client_satisfaction_scores)
max_score: float = max(client_satisfaction_scores)
mean_score: float = statistics.mean(client_satisfaction_scores)
stdev_score: float = statistics.stdev(client_satisfaction_scores)
min_age: float = min(current_company_ages)
max_age: float = max(current_company_ages)
mean_age: float = statistics.mean(current_company_ages)
stdev_age: float = statistics.stdev(current_company_ages)

#####################################
# Declare a global variable named byline.
#####################################

byline: str = f"""
------------------------------------------------------
Suarez Analytics: Company and Client Information
------------------------------------------------------
Has International Clients:  {has_international_clients}
Years in Operations:        {years_in_operation}
Skills Offered:             {skills_offered}
Client Satisfaction scores: {client_satisfaction_scores}
Has Pet dog                 {has_pet_dog}
Dogs Company Owns           {dogs_company_owns}
Company Pet Names           {company_pet_names}
Current Company Ages        {current_company_ages}
Minimum Satisfaction Score: {min_score}
Maximum Satisfaction Score: {max_score}
Mean Satisfaction Score: {mean_score:.2f}
Standard Deviation of Satisfaction Scores: {stdev_score:.2f}
Minimum Company Age: {min_age}
Maximum Company Age: {max_age}
Mean Company Age: {mean_age:.2f}
Standard Deviation of Company Age: {stdev_age:.2f}
"""

#####################################
# Define the get_byline() Function
#####################################

def get_byline() -> str:
    '''Return a byline for my analytics projects.'''
    return byline
    
#####################################
# Define a main() function for this module.
#####################################

#The main function now calls get_byline() to retrieve the byline.
def main() -> None:
    '''Print results of get_byline() when main() is called.'''
    print(get_byline())

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()
    
    
