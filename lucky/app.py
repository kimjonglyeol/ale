# streamlit 라이브러리 호출
import streamlit as st
import numpy as np

st.title("조 추첨 페이지")
st.header("여러분의 참여를 환영합니다")

# 추첨 대상인 13명의 이름을 넣을 수 있는 text.input
# 3 x 4 (row, col)
# 열을 배치하는 메소드
columns = st.columns(4)    # 화면을 열로 나누어서 배치
# 가로 4개의 열
for idx, col in enumerate(columns):
    col.text_input(f"조 추첨 대상 {idx + 1}", key=idx)
# 13명이 소속될 조 이름을 넣을 위치

# <추첨 버튼>
# 13개의 짝을 지어서 표시해줄 그래픽
