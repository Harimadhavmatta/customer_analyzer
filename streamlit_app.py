import streamlit as st
import pandas as pd

# Title and Info
st.title('🎂 Bakery Customer Analysis')
st.info("Analyzer tells you what happened this year in the bakery")

# Load dataset
df = pd.read_csv('bakery_customer_data.csv')

# Display Sample Dataset
st.subheader("Sample Dataset")
st.write(df.head())

# Basic Description of Data
st.subheader('Basic Description Of Data')
with st.expander("**Describe**"):
    st.write("This Describe display's the aggregates of each numeric column")
    st.write(df.describe())

# Top Customers Section
st.subheader("Want to know your top customers?")
with st.expander("**Top Customer List**"):
    st.write("How many top customers do you want to see?")
    user_input = st.text_input('Enter a number, e.g., 10, 20, 5...')
    
    if user_input.isdigit():
        num_customers = int(user_input)
        sorted_customers = df.sort_values("bill_amount", ascending=False)
        st.write(sorted_customers.head(num_customers))
    else:
        st.write("Please enter a valid number.")

# Top Performing Items Section
st.subheader("Want to know which item performed well?")
with st.expander("**Top Item List**"):
    st.write("Here are the sales of each item in order:")
    target=['bill_amount']
    grouped=df.groupby(['item_category'])['bill_amount'].mean()
    grouped=grouped.sort_values( ascending=False)
    st.write(grouped)
