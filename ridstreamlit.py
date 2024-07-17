import streamlit as st
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

# Load data from CSV file
data = pd.read_csv('HH2022a.csv')
income = data['income'].values
age = data['age'].values
gender = data['gender'].values

# Streamlit app
st.title("Partner Salary Check")

# Ask for minimum and maximum age inputs using sliders
age_min, age_max = st.slider(
    "Select age range",
    min_value=int(age.min()),
    max_value=int(age.max()),
    value=(20, 40)  # Default range
)

# Ask for preferred annual salary input
income_selection = st.number_input("Enter Minimum Monthly Salary (MYR):", min_value=0)

# Ask for gender preference
gender_selection = st.selectbox("Are you looking for male or female:", ['male', 'female'])

if st.button("Calculate"):
    percentage = unrealistic_expectation(gender, gender_selection, income_selection, income, age_min, age_max, age)
    st.write(f"Percentage of Malaysians meeting the criteria: {percentage:.2f}%")

# Add statement at the bottom
st.write("Dataset obtained from Department of Statistics Malaysia (DOSM) from a survey conducted in 2022. Sample size n = 38,413")
