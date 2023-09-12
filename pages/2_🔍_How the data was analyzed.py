import streamlit as st
from PIL import Image
def data_method():
    st.markdown('## 사용한 라이브러리')
    st.markdown(
        '''
|사용 라이브러리|이유|
|---|---|
|Pandas|대용량 데이터 처리에 필요,효율적으로 데이터의 평균구하기,csv파일 읽기|
|Numpy|사이킷런에서 Linear Regression에 필요한 데이터를 Numpy.array로 변경|
|Matplotlib|그래프 그릴 때 필요|
|Seaborn|그래프를 효율적으로 그릴 때 필요|
|Scikit-learn|Linear Regression을 사용하기 위해 필요|
        '''
    )
    st.markdown('## 분석방법')
    img1 = Image.open('picture/method1.PNG')
    img2 = Image.open('picture/method2.PNG')
    img3 = Image.open('picture/method3.PNG')
    img4 = Image.open('picture/method4.PNG')
    img5 = Image.open('picture/method5.PNG')
    img6 = Image.open('picture/method6.PNG')
    img7 = Image.open('picture/method7.PNG')
    img8 = Image.open('picture/method8.PNG')
    img9 = Image.open('picture/method9.PNG')

    st.markdown('### csv파일 불러오기')
    st.image(img1,use_column_width=True)
    
    st.write('csv파일을 불러옴')
    
    st.markdown('### teamdata만 추출')
    st.image(img2,use_column_width=True)
    st.markdown(
        '''
        1. 주어진 데이터에서 teamid 열을 추출하여 중복을 없애 teamList 추출
        2. 팀의 각 경기 당 승리/패배 여부, 더블 킬, 드래곤 처치 횟수 등 추출
        3. NaN제거(=match_data_filtered)
        '''
    )
    
    st.markdown('### match_data_filtered')
    st.image(img3,use_column_width=True)
    st.write('match_data_filtered')
    
    st.markdown('### 각 팀의 승률 구하기')
    st.image(img4,use_column_width=True)
    st.markdown(
        '''
        1. 방금 추출한 팀 리스트를 순회하면서 match_data_filtered에서 그 팀의 데이터만 추출(=teamFiltered)
        2. 승리는 1, 패배는 1이므로, teamFiltered['result']의 평균을 구하면 승률이 나옴.
        3. 이것을 winRate[각 팀]에 저장
        '''
    )
    

    st.markdown('### 각 팀의 승률')
    st.image(img5,use_column_width=True)
    st.write('각 팀의 승률')
    
    st.markdown('### 팀의 평균 킬 수, 평균 드래곤 처치 횟수 구하기')
    st.image(img6,use_column_width=True)
    st.write('킬 수, 드래곤 처치 횟수 등도 같은 방법으로 처리함')
    

    st.markdown('### 데이터 합치기')
    st.image(img7,use_column_width=True)
    st.write('구한 데이터를 팀별로 합침')

    st.markdown('### 그래프 그리기')
    st.image(img8,use_column_width=True)
    st.write('Regplot을 이용하여 각종 지표와 승률의 산점도(scatterplot)과 추세선(trendline)을 그림')

    st.markdown('### Linear Regression')
    st.image(img9,use_column_width=True)
    st.write('Scikit learn의 Linear Regression을 이용하여 각 지표와 승률의 정확한 상관관계 분석')

st.set_page_config(page_title="How the data was analyzed", page_icon="🔍")
data_method()