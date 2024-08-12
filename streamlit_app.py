import streamlit as st
import pandas as pd
st.title(' 🎂 Bakery Customer Analysis')
st.info(" Analyzer tells you what happened this year in the bakery ")
df=pd.read_csv('bakery_customer_data.csv')
st.subheader("Sample Dataset")
st.write(df.head())
st.subheader('Basic Description Of Data')
with st.expander("**Describe**"):
  st.write(" This Describe display's the aggregates of each numeric column ")
  st.write(df.describe())

st.subheader("want to know you top customers ? ")
st.write("who many customers you want to see ? ")
x=st.text_input('eg:- 10,20,5...')
if x is not None:
  st.write(df.nlargest(x,"bill_amount"))
