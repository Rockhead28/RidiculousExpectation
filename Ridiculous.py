#works as intended in python

import numpy as np
import pandas as pd

def unrealistic_expectation(gender, gender_selection, income_selection, income, age_min, age_max, age):
    # Convert lists to NumPy arrays for vectorized operations
    income = np.array(income)
    age = np.array(age)
    gender = np.array(gender)
    
    # Convert gender column to strings
    gender = gender.astype(str)
    
    # Convert gender selection to lowercase
    gender = np.char.lower(gender)
    
    # Create boolean masks to filter data based on criteria
    income_mask = income > income_selection
    gender_mask = gender == gender_selection  # Filter based on gender selection
    age_mask = (age >= age_min) & (age <= age_max)  # Filter based on age range
    
    # Combine masks using logical AND
    criteria_met_mask = income_mask & gender_mask & age_mask
    
    # Count the number of people meeting the criteria
    number_of_pax = np.count_nonzero(criteria_met_mask)
    
    # Calculate the percentage of people meeting the criteria
    total_pax = np.count_nonzero(np.logical_and(income > 0, age > 0))  # Total number of individuals with valid income and age
    
    percentage = (number_of_pax / total_pax) * 100
    return percentage

# Ask for minimum and maximum age inputs
while True:
    try:
        age_min = int(input("Enter Minimum Age: "))
        age_max = int(input("Enter Maximum Age: "))
        if age_min >= age_max:
            print("Maximum age should be greater than minimum age.")
        else:
            break  # Exit the loop if input is valid
    except ValueError:
        print("Invalid input. Please enter valid integers for age.")

# Read input and dataset from CSV file after age inputs are obtained
data = pd.read_csv('HH2022a.csv')
income = data['income'].values
age = data['age'].values

# Ask for preferred annual salary input
while True:
    try:
        income_selection = int(input("Enter Minimum Monthly Salary: "))
        break  # Exit the loop if input is valid
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Ask for gender preference
while True:
    gender_selection = input("Are you looking for male or female: ").lower()
    if gender_selection in ['male', 'female']:
        break
    else:
        print("Invalid input. Please enter either 'male' or 'female'.")

percentage = unrealistic_expectation(data['gender'].values, gender_selection, income_selection, income, age_min, age_max, age)
print(f"Percentage of people meeting the criteria: {percentage:.2f}%")
