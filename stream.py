import streamlit as st
from streamlit_option_menu import option_menu
with st.sidebar:
    choose = option_menu("메뉴", ["분석한 데이터", "데이터 분석 방법", "데이터 분석 결과(kill&destroy)","데이터 분석 결과(first)","데이터 분석 결과(기타)",'레퍼런스'],
                         icons=['house', 'hourglass split', 'bar-chart-line','bar-chart-steps','pie-chart-fill','bookhalf'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "gray", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "skyblue"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )