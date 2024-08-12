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

st.subheader("Want to know you top customers ? ")
with st.expander("**Top List**"):
  st.write("Who many top customers you want to see ? ")
  x=st.text_input('eg:- 10,20,5...')
  x=int(x)
  s=df.sort_values("bill_amount", ascending=False)
  st.write(s.head(x))
  
