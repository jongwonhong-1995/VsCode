import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup

df = pd.read_csv("C:/Users/LG/Desktop/TB_GYM_FORUM_BBS_202401050825.csv")
df1 = pd.read_csv("C:/Users/LG/Desktop/TB_GYM_FORUM_BZDP_BBS_202401050849.csv")
df2 = pd.read_csv("C:/Users/LG/Desktop/TB_GYM_FORUM_CATEGORY_MAPNG_202401050853.csv")

st.dataframe(df)


def remove_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    text_temp = soup.get_text()

    return text_temp

df['FORUM_CONTENTS'] = df['FORUM_CONTENTS'].apply(remove_tags)
df['FORUM_CONTENTS'] = df['FORUM_CONTENTS'].apply(remove_tags)

df1['FORUM_CONTENTS'] = df1['FORUM_CONTENTS'].apply(remove_tags)
df1['FORUM_CONTENTS'] = df1['FORUM_CONTENTS'].apply(remove_tags)

writer = pd.ExcelWriter("C:/Users/LG/Desktop/포럼정리.xlsx", engine = 'openpyxl')

df.to_excel(writer, sheet_name = "지식포럼")
df1.to_excel(writer, sheet_name = "자동차,소형 지식포럼")
df2.to_excel(writer, sheet_name = "카테고리 매핑")

writer.close()