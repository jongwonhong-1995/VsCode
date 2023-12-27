import pandas as pd
import streamlit as st

file_path = 'C:/Users/LG/Desktop/'
file_name = 'TB_KLDGINFO_TERM_CTGRY_202312261335.csv'

df = pd.read_csv(file_path + file_name)
st.dataframe(df)
