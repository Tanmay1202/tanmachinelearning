import streamlit as st
import pandas as pd

st.title('Machine Leaning Application')

st.info("This is a machine learning app")

with st.expander('Data'):
    st.write('**Raw Data**')
    df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
    df

    st.write('**X**')
    X = df.drop('species', axis=1)
    X

    st.write('**y**')
    y = df.species
    y
