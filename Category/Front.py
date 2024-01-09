import streamlit as st
import pandas as pd

def intro():
    import streamlit as st

    st.write("# Welcome to Jongwon's Analysis! 👋")
    st.sidebar.success("Select a menu above.")

    st.markdown(
         """
        This project is for analysis **B-LEX Document** sequentially.

        **👈 Select a menu from the dropdown on the left** to see some examples
        of what Streamlit can do!

        ### Want to know B-LEX?

        - Check out [B-LEX🔋](https://blex.rnd.lgensol.com)
        - Check out [B-LEXMS](https://blexmd.rnd.lgensol.com)

    """
    )

def dictonary_analysis():
    import streamlit as st
    import plotly.express as px
    import datetime as dt

    st.write("## 용어사전 카테고리 분석")
    st.write('### Data Upload')
    ## file_path = "C:/Users/LG/Desktop/"
    ## file_name = "TB_KLDGINFO_TERM_CTGRY_202312261335.csv"

    ## df = pd.read_csv(file_path + file_name)

    df = pd.read_csv('Category/TB_KLDGINFO_TERM_CTGRY_202312261335.csv')

    df.replace({'TERM_CTGRY_CODE' : {'TRNC_TECH' : '기술', 'TRNC_RND' : 'R&D', 'TRNC_PROD' : '생산',
                                     'TRNC_QLITY' : '품질', 'TRNSLAT_IT' : 'IT', 'TRNC_MNGMT_INV' : '경영/혁신',
                                     'TRNC_SCM_PURCH' : 'SCM/구매', 'TRNC_INFR_SAFE' : '인프라/안전',
                                     'TRNC_ETC' : '기타', 'TRNC_BSN_MARKT' : '영업/마케팅', 'TRNC_BMS' : 'BMS',
                                     'TRNC_ESG' : 'ESG', 'TRNC_HR' : 'HR', 'TRNC_NFF' : 'NFF'}}, inplace = True)
    df.rename(columns={'TERM_CTGRY_CODE' : '카테고리'}, inplace = True)

    df['RGST_DT'] = pd.to_datetime(df['RGST_DT']).dt.strftime('%Y-%m-%d')
    df['UPDT_DT'] = pd.to_datetime(df['UPDT_DT']).dt.strftime('%Y-%m-%d')
    str = " df = pd.read_csv('Category/TB_KLDGINFO_TERM_CTGRY_202312261335.csv')"
    st.code(str, language = 'python')
    st.dataframe(df.head())

    st.write('### Data Info')
    col1, col2 = st.columns(2)

    with col1:
        st.metric(label = 'Total count', value = df['TERM_ID'].nunique(dropna=False))
        st.dataframe(df['카테고리'].value_counts())
    with col2:
        st.metric(label = 'Category count', value = df['카테고리'].nunique(dropna=False))
        fig = px.pie(df['카테고리'].value_counts(), values = 'count',
                     names=df['카테고리'].unique(), title = 'Category 별 분포')
        st.plotly_chart(fig, thema = 'streamlit', use_container_width=True)
    
def gym_analysis():
    import streamlit as st
    import plotly.express as px

    st.write("## 지식포럼 카테고리 분석")
    st.write('### Data Upload')
    str = "df = pd.read_csv('Category/TB_GYM_FORUM_BZDP_CATEGORY_MAPNG_202312270953.csv')"
    st.code(str, language='python')

    df = pd.read_csv('Category/TB_GYM_FORUM_BZDP_CATEGORY_MAPNG_202312270953.csv')
    
    st.dataframe(df.head())

    st.write('### 컬럼명과 값 변경')
    df.replace({'FORUM_CATEGORY_CODE' : {'TRNC_TECH' : '기술', 'TRNC_RND' : 'R&D', 'TRNC_PROD' : '생산',
                                     'TRNC_QLITY' : '품질', 'TRNSLAT_IT' : 'IT', 'TRNC_MNGMT_INV' : '경영/혁신',
                                     'TRNC_SCM_PURCH' : 'SCM/구매', 'TRNC_INFR_SAFE' : '인프라/안전',
                                     'TRNC_ETC' : '기타', 'TRNC_BSN_MARKT' : '영업/마케팅', 'TRNC_BMS' : 'BMS',
                                     'TRNC_ESG' : 'ESG', 'TRNC_HR' : 'HR', 'TRNC_NFF' : 'NFF'}}, inplace = True)
    df.rename(columns={'FORUM_CATEGORY_CODE' : '카테고리'}, inplace = True)
    st.code('df.replace(...) \n df.rename(columns = {...})', language = 'python')
    st.dataframe(df.head(5))

    st.write('### 데이터 분포 확인')
    col1, col2 = st.columns(2)

    with col1:
        st.dataframe(df['카테고리'].value_counts().reset_index())
    with col2:
        st.metric(label = 'Category count', value = df['카테고리'].nunique(dropna=False))
        fig = px.pie(df['카테고리'].value_counts(), values = 'count',
                     names=df['카테고리'].unique(), title = 'Category 별 분포')
        st.plotly_chart(fig, thema = 'streamlit', use_container_width=True)

    st.write("### 데이터 다운로드 ")
    

page_names_to_funcs = {
    "-" : intro,
    "Dictonary Analysis" : dictonary_analysis,
    "Knowledge Gym Analysis" : gym_analysis
}

demo_name = st.sidebar.selectbox("Choose a menu", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()