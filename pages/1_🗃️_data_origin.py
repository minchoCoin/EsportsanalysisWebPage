import streamlit as st
import pandas as pd
def data_origin():
    st.markdown('## 분석한 데이터')
    st.markdown(
        '''
       - 2023_LOL_esports_match_data_from_OracleElixir.csv 
       - https://oracleselixir.com/tools/downloads
- 2023 리그오브레전드 이스포츠 대회 경기 데이터
경기에서 사용한 챔피언, 킬 ,데스, 더블 킬, 
  몬스터 처치 횟수, 타워 파괴 횟수 등이 csv파일로
  정리되어있음

        '''
    )
    df = pd.read_csv("2023_LoL_esports_match_data_from_OraclesElixir.csv")
    if st.button('데이터 보기'):
        st.dataframe(df)

st.set_page_config(page_title="data_origin", page_icon="🗃️")
data_origin()