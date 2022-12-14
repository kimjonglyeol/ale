import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title("지하철")

st.image(
        'https://imgnews.pstatic.net/image/421/2022/12/03/0006498364_001_20221203063104186.jpg?type=w647'

)
# st.write(
#    "https://www.naver.com/"
# )
df = pd.read_csv('./subway/subway.csv', encoding='CP949')
st.write(df)

# df2 = pd.read_csv('./subway/subway_part.csv')
# st.write(df2)

# fig = plt.figure(figsize=(10,4))
# sns.histplot(data=df, x='호선', hue='조사일자', multiple='stack')
# st.pyplot(fig)

# fig2 = plt.figure(figsize=(10,4))
# sns.kdeplot(data=df, x='호선')
# sns.rugplot(data=df, x='호선')
# st.pyplot(fig2)

# fig3 = plt.figure(figsize=(10,4))
# sns.kdeplot(data=df, x='호선', hue='조사일자', multiple='stack')
# st.pyplot(fig3)

# fig4 = plt.figure(figsize=(10,4))
# sns.displot(data=df, x='호선')
# st.pyplot(fig4)

# x = [10, 60, 30] # 범주형 데이터별 파이 그래프의 비율
# labels = ['A', 'B', 'C']
# fig5 = plt.figure(figsize=(10, 4))
# plt.pie(x=x, labels=labels, autopct='%.1f%%')
# st.pyplot(fig5)

tab1, tab2, tab3, tab4, tab5 = st.tabs(['호선별 이용자수','5시30분 이용자수','6시30분 이용자수','7시30분 이용자수','8시30분 이용자수'])
fig = px.histogram(df, x='호선')
tab1.plotly_chart(fig)

df.pivot_table(index='호선', columns='구분', values='5시30분', aggfunc='sum')
fp = df.pivot_table(index='호선', columns='구분', values='5시30분', aggfunc='sum')
zp = fp.fillna(0)
# zp

# df7 = px.data.df()
fig7 = px.density_heatmap(df, x='호선', y="5시30분", marginal_x="rug", marginal_y="histogram", colorscale = 'RdBu' )
tab2.plotly_chart(fig7)

fig8 = px.density_heatmap(df, x='호선', y="6시30분", marginal_x="rug", marginal_y="histogram")
tab3.plotly_chart(fig8)

fig9 = px.density_heatmap(df, x='호선', y="7시30분", marginal_x="rug", marginal_y="histogram")
tab4.plotly_chart(fig9)

fig0 = px.density_heatmap(df, x='호선', y="8시30분", marginal_x="rug", marginal_y="histogram")
tab5.plotly_chart(fig0)

