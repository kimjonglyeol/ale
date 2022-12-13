import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.write(
   "https://www.data.go.kr/data/15081069/fileData.do"
)
df = pd.read_csv('./cafe/cafe.csv', encoding='CP949')
st.write(df)

from glob import glob

file_names = glob('./cafe/cafe.csv')
total = pd.DataFrame()

for file_name in file_names:
   temp = pd.read.csv(file_name, sep='|', encoding='utf=--8')
   total = pd.concat([total, temp])

 total.reset_index(inplace=True, drop=True)
st.write(total)