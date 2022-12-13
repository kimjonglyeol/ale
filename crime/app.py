import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns





temp = pd.read_csv("./crime/crime.csv", sep="|", encoding="cp949")          #파일 불러오기

from glob import glob          #csv파일 읽기 위해 glob사용

file_names = glob("./crime/crime.csv")          #csv파일명 목록 불러오기

total = pd.DataFrame()

 for file_name in file_names:          #모든 csv파일 내용 병합하기

         temp = pd.read_csv(file_name, sep="|", encoding="CP949")

         total = pd.concat([total, temp])

data = total[['절도', '사기', '폭', '도로교통법(음주운전)']]          #필요한 columns 선택

