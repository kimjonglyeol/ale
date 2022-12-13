import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.write(
   "https://www.naver.com/"
)
df = pd.read_csv('./subway/subway.csv', encoding='CP949')
st.write(df)
