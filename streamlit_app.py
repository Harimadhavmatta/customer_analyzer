import streamlit as st
import pandas as pd
st.title(' 🎂 Bakery Customer Analysis')
st.info(" Analyzer that shows what's happening in bakery ")
st.write('Hello world!')
df=pd.read_csv('bakery_customer_data.csv')
st.write(df.head())
