import streamlit as st
import pandas as pd
import os

# Define the path to the Excel file
excel_file = 'user_data.xlsx'

# Check if the Excel file exists, and if not, create it with appropriate columns
if not os.path.exists(excel_file):
    df = pd.DataFrame(columns=['Name', 'Gender'])
    df.to_excel(excel_file, index=False)

# Streamlit form interface
st.title('User Information Form')

with st.form(key='user_form'):
    # Create input fields for the form
    name = st.text_input('Enter your name:')
    gender = st.selectbox('Select your gender:', ['Male', 'Female', 'Other'])
    
    # Submit button for the form
    submit_button = st.form_submit_button(label='Submit')

# When the form is submitted, save the input data to the Excel file
if submit_button:
    if name:
        # Read the existing data from the Excel file
        df = pd.read_excel(excel_file)

        # Append the new user data
        new_data = pd.DataFrame({'Name': [name], 'Gender': [gender]})
        df = pd.concat([df, new_data], ignore_index=True)

        # Save the updated DataFrame back to the Excel file
        df.to_excel(excel_file, index=False)

        # Display a success message to the user
        st.success(f'Thank you {name}, your information has been saved!')
    else:
        # Error message if the name field is empty
        st.error("Name is required to submit the form!")
