import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from PIL import Image
import streamlit.components.v1 as components
st.set_page_config(page_title = "LOL data analysis")

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
def data_result1():
    result1 = Image.open('picture/result1.png')
    result2 = Image.open('picture/result2.png')
    result3 = Image.open('picture/result3.png')
    result4 = Image.open('picture/result4.png')
    result5 = Image.open('picture/result5.png')
    result6 = Image.open('picture/result6.png')
    result7 = Image.open('picture/result7.png')

    st.image(result1,use_column_width=True)
    st.image(result2,use_column_width=True)
    st.image(result3,use_column_width=True)
    st.image(result4,use_column_width=True)
    st.image(result5,use_column_width=True)
    st.image(result6,use_column_width=True)
    st.image(result7,use_column_width=True)

    components.html(
        '''
        <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>category</th>
      <th>coefficient</th>
      <th>intercept</th>
      <th>r2 score</th>
      <th>form</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>22</th>
      <td>Kills</td>
      <td>0.050</td>
      <td>-0.237</td>
      <td>0.584</td>
      <td>0.05x + -0.237</td>
    </tr>
    <tr>
      <th>21</th>
      <td>doubleKills</td>
      <td>0.284</td>
      <td>0.009</td>
      <td>0.595</td>
      <td>0.284x + 0.009</td>
    </tr>
    <tr>
      <th>20</th>
      <td>tripleKill</td>
      <td>0.701</td>
      <td>0.248</td>
      <td>0.375</td>
      <td>0.701x + 0.248</td>
    </tr>
    <tr>
      <th>19</th>
      <td>quadraKill</td>
      <td>1.056</td>
      <td>0.396</td>
      <td>0.118</td>
      <td>1.056x + 0.396</td>
    </tr>
    <tr>
      <th>18</th>
      <td>pentaKill</td>
      <td>1.995</td>
      <td>0.434</td>
      <td>0.057</td>
      <td>1.995x + 0.434</td>
    </tr>
    <tr>
      <th>17</th>
      <td>minionKill</td>
      <td>0.001</td>
      <td>-0.455</td>
      <td>0.139</td>
      <td>0.001x + -0.455</td>
    </tr>
    <tr>
      <th>16</th>
      <td>monsterKill</td>
      <td>0.006</td>
      <td>-0.512</td>
      <td>0.313</td>
      <td>0.006x + -0.512</td>
    </tr>
    <tr>
      <th>15</th>
      <td>dragons</td>
      <td>0.304</td>
      <td>-0.178</td>
      <td>0.609</td>
      <td>0.304x + -0.178</td>
    </tr>
    <tr>
      <th>14</th>
      <td>opp_dragons</td>
      <td>-0.302</td>
      <td>1.137</td>
      <td>0.490</td>
      <td>-0.302x + 1.137</td>
    </tr>
    <tr>
      <th>13</th>
      <td>elementaldrakes</td>
      <td>0.316</td>
      <td>-0.190</td>
      <td>0.621</td>
      <td>0.316x + -0.19</td>
    </tr>
    <tr>
      <th>12</th>
      <td>opp_elementaldrakes</td>
      <td>-0.323</td>
      <td>1.169</td>
      <td>0.519</td>
      <td>-0.323x + 1.169</td>
    </tr>
    <tr>
      <th>11</th>
      <td>elders</td>
      <td>0.716</td>
      <td>0.428</td>
      <td>0.026</td>
      <td>0.716x + 0.428</td>
    </tr>
    <tr>
      <th>10</th>
      <td>opp_elders</td>
      <td>-0.105</td>
      <td>0.460</td>
      <td>0.001</td>
      <td>-0.105x + 0.46</td>
    </tr>
    <tr>
      <th>9</th>
      <td>heralds</td>
      <td>0.384</td>
      <td>0.087</td>
      <td>0.305</td>
      <td>0.384x + 0.087</td>
    </tr>
    <tr>
      <th>8</th>
      <td>opp_heralds</td>
      <td>-0.393</td>
      <td>0.859</td>
      <td>0.321</td>
      <td>-0.393x + 0.859</td>
    </tr>
    <tr>
      <th>7</th>
      <td>barons</td>
      <td>0.611</td>
      <td>0.031</td>
      <td>0.651</td>
      <td>0.611x + 0.031</td>
    </tr>
    <tr>
      <th>6</th>
      <td>opp_barons</td>
      <td>-0.643</td>
      <td>0.961</td>
      <td>0.545</td>
      <td>-0.643x + 0.961</td>
    </tr>
    <tr>
      <th>5</th>
      <td>towers</td>
      <td>0.111</td>
      <td>-0.181</td>
      <td>0.885</td>
      <td>0.111x + -0.181</td>
    </tr>
    <tr>
      <th>4</th>
      <td>opp_towers</td>
      <td>-0.121</td>
      <td>1.230</td>
      <td>0.919</td>
      <td>-0.121x + 1.23</td>
    </tr>
    <tr>
      <th>3</th>
      <td>turretplates</td>
      <td>0.123</td>
      <td>-0.070</td>
      <td>0.428</td>
      <td>0.123x + -0.07</td>
    </tr>
    <tr>
      <th>2</th>
      <td>opp_turretplates</td>
      <td>-0.118</td>
      <td>0.999</td>
      <td>0.468</td>
      <td>-0.118x + 0.999</td>
    </tr>
    <tr>
      <th>1</th>
      <td>inhibitors</td>
      <td>0.431</td>
      <td>0.078</td>
      <td>0.780</td>
      <td>0.431x + 0.078</td>
    </tr>
    <tr>
      <th>0</th>
      <td>opp_inhibitors</td>
      <td>-0.408</td>
      <td>0.881</td>
      <td>0.802</td>
      <td>-0.408x + 0.881</td>
    </tr>
  </tbody>
</table>
</div>

	
        '''
    ,height=700)

def data_result2():
    result1 = Image.open('picture/result_first1.png')
    result2 = Image.open('picture/result_first2.png')

    st.image(result1,use_column_width=True)
    st.image(result2,use_column_width=True)

    components.html(
        '''
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>category</th>
      <th>coefficient</th>
      <th>intercept</th>
      <th>r2 score</th>
      <th>form</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6</th>
      <td>firstblood</td>
      <td>0.575</td>
      <td>0.175</td>
      <td>0.185</td>
      <td>0.575x + 0.175</td>
    </tr>
    <tr>
      <th>5</th>
      <td>firstdragon</td>
      <td>0.570</td>
      <td>0.179</td>
      <td>0.182</td>
      <td>0.57x + 0.179</td>
    </tr>
    <tr>
      <th>4</th>
      <td>firstherald</td>
      <td>0.455</td>
      <td>0.235</td>
      <td>0.144</td>
      <td>0.455x + 0.235</td>
    </tr>
    <tr>
      <th>3</th>
      <td>firstbaron</td>
      <td>0.954</td>
      <td>0.026</td>
      <td>0.730</td>
      <td>0.954x + 0.026</td>
    </tr>
    <tr>
      <th>2</th>
      <td>firsttower</td>
      <td>0.806</td>
      <td>0.078</td>
      <td>0.522</td>
      <td>0.806x + 0.078</td>
    </tr>
    <tr>
      <th>1</th>
      <td>firstmidtower</td>
      <td>0.787</td>
      <td>0.087</td>
      <td>0.529</td>
      <td>0.787x + 0.087</td>
    </tr>
    <tr>
      <th>0</th>
      <td>firsttothreetowers</td>
      <td>0.801</td>
      <td>0.087</td>
      <td>0.671</td>
      <td>0.801x + 0.087</td>
    </tr>
  </tbody>
</table>
</div>
        '''
   ,height=300 )
def data_result3():
    result1 = Image.open('picture/other1.png')
    result2 = Image.open('picture/other2.png')

    st.image(result1,use_column_width=True)
    st.image(result2,use_column_width=True)
def reference():
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
def github():
    st.markdown(
        '''
        https://github.com/minchoCoin/LOL_data_analysis_prj
        '''
    )

menu_dict = {
    "분석한 데이터":{"fn": data_origin},
    "데이터 분석 방법":{"fn": data_method},
    "데이터 분석 결과(kill)":{"fn": data_result1},
    "데이터 분석 결과(first)":{"fn": data_result2},
    "데이터 분석 결과(기타)":{"fn": data_result3},
    "레퍼런스":{"fn": reference},
    "my github":{"fn": github}
}

with st.sidebar:
    choose = option_menu("메뉴", ["분석한 데이터", "데이터 분석 방법", "데이터 분석 결과(kill)","데이터 분석 결과(first)","데이터 분석 결과(기타)",'레퍼런스','my github'],
                         icons=['house', 'hourglass split', 'bar-chart-line','bar-chart-steps','pie-chart-fill','book-half','github'],
                         menu_icon="menu-up", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "gray", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "skyblue"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )
    #choose
if choose in menu_dict.keys():
    menu_dict[choose]["fn"]()