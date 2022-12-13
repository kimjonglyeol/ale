# streamlit 라이브러리 호출
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns

st.write('hello')

titanic = sns.load_dataset('titanic') 
# st.write(titanic)
st.table(titanic)