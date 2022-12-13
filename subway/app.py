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

fig = plt.figure(figsize=(10,4))
sns.histplot(data=df, x='호선', hue='조사일자', multiple='stack')
st.pyplot(fig)

fig2 = plt.figure(figsize=(10,4))
sns.kdeplot(data=df, x='호선')
sns.rugplot(data=df, x='호선')
st.pyplot(fig2)

fig3 = plt.figure(figsize=(10,4))
sns.kdeplot(data=df, x='호선', hue='조사일자', multiple='stack')
st.pyplot(fig3)

fig4 = plt.figure(figsize=(10,4))
sns.displot(data=df, x='호선')
st.pyplot(fig4)

fig5 = plt.figure(figsize=(10,4))
sns.kdeplot(data=df, x='호선')
sns.rugplot(data=df, x='호선')
st.pyplot(fig5)

x = [10, 60, 30] # 범주형 데이터별 파이 그래프의 비율
labels = ['A', 'B', 'C']
fig6 = plt.figure(figsize=(8, 4))
plt.pie(x=x, labels=labels, autopct='%.1f%%')
st.pyplot(fig6)
