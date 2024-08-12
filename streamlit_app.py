import streamlit as st
import pandas as pd
st.title(' 🎂 Bakery Customer Analysis')
st.info(" Analyzer tells you what happened this year in the bakery ")
df=pd.read_csv('bakery_customer_data.csv')
st.subheader("Sample Dataset")
st.write(df.head())
st.subheader('Basic Description Of Data')
with st.expander("**Info**"): 
  st.write(" This info tells you about datasets schema ")
  st.write(str(df.info()))
with st.expander("**Describe**"):
  st.write(" This Describe display's the aggregates of each numeric column ")
  st.write(df.describe())
