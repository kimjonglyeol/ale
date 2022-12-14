# streamlit 라이브러리 호출
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.write(
    """
    ## 데이터의 종류
    * 데이터의 특성에 따라서 시각화 방식도 달라짐
    * 정형 데이터 : 값으로 나타낼 수 있는 데이터 (숫자)
    * 비정형 데이터 : 정형 데이터가 아닌 것 (사진, 언어...)
    """
)

titanic = sns.load_dataset('titanic') 
st.write(titanic)
# st.table(titanic)

fig = plt.figure(figsize=(10,4))
sns.histplot(data=titanic, x='age')
st.pyplot(fig)

fig = plt.figure(figsize=(8,4))
sns.histplot(data=titanic, x='age', hue='alive', multiple='stack')
st.pyplot(fig)

x = [10, 60, 30] # 범주형 데이터별 파이 그래프의 비율
labels = ['A', 'B', 'C']
fig = plt.figure(figsize=(8, 4))
plt.pie(x=x, labels=labels, autopct='%.1f%%')
st.pyplot(fig)