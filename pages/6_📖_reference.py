import streamlit as st

def reference():
        st.set_page_config(page_title="reference", page_icon="📖")
        st.markdown(
        '''
|reference|이유|
|---|---|
|Do it! 쉽게 배우는 파이썬 데이터 분석,김영우 저, 이지스 퍼블리싱|데이터 분석의 전형적인 방법|
|혼자 공부하는 머신러닝+딥러닝, 박해선 저, 한빛미디어|선형회귀 및 로지스틱 회귀를 구하는 방법|
|https://seaborn.pydata.org/|그래프 그리기|
|https://blog.naver.com/PostView.naver?blogId=kiddwannabe&logNo=222655678945&categoryNo=0&parentCategoryNo=0&currentPage=1|Seaborn 막대그래프에 값표시|
|https://mindscale.kr/course/python-visualization-basic/grid/|한번에 여러 그래프 그리기|
|https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=dotorimj2&logNo=222117972039|산점도와 선형회귀선 그리기|
        '''
        )

reference()
