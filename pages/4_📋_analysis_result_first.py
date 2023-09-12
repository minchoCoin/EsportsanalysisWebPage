import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from collections import defaultdict
import numpy as np
import seaborn as sb

col = ['firstblood','firstdragon','firstherald','firstbaron','firsttower','firstmidtower','firsttothreetowers']
st.set_page_config(page_title="analysis_result(first and winRate)", page_icon="📋")
match_data = pd.read_csv("2023_LoL_esports_match_data_from_OraclesElixir.csv")

match_data_origin=match_data

teamList = match_data_origin['teamid'].unique()

match_data_first = match_data_origin.loc[match_data_origin['position']=='team',['teamid','result','firstblood','firstdragon','firstherald','firstbaron','firsttower','firstmidtower','firsttothreetowers']]

match_data_first = match_data_first.dropna(axis=0)



winRate = defaultdict()
for team in teamList:
    teamFiltered = match_data_first.loc[match_data_first['teamid'] == team]
    winRate[team] = teamFiltered['result'].mean()
col2 = ['firstblood','firstdragon','firstherald','firstbaron','firsttower','firstmidtower','firsttothreetowers']


firstbloodDict = {}
firstdragonDict = {}
firstheraldDict = {}
firstbaronDict={}
firsttowerDict = {}
firstmidtowerDict={}
firsttothreetowersDict={}
for team in teamList:
    teamFiltered = match_data_first.loc[match_data_first['teamid'] == team]
    firstbloodDict[team] = teamFiltered['firstblood'].mean()
    firstdragonDict[team] = teamFiltered['firstdragon'].mean()
    firstheraldDict[team] = teamFiltered['firstherald'].mean()
    firsttowerDict[team] = teamFiltered['firsttower'].mean()
    firstmidtowerDict[team] = teamFiltered['firstmidtower'].mean()
    firsttothreetowersDict[team] = teamFiltered['firsttothreetowers'].mean()
    firstbaronDict[team] =  teamFiltered['firstbaron'].mean()
    
relationDf_first = pd.DataFrame(columns=["teamid","winRate",'firstblood','firstdragon','firstherald','firstbaron','firsttower','firstmidtower','firsttothreetowers'])

#winRate는 이전에 계산한 값을 씀
for team in teamList:
    relationDf_first.loc[-1] = [team,winRate[team],firstbloodDict[team],firstdragonDict[team],firstheraldDict[team],firstbaronDict[team],firsttowerDict[team],firstmidtowerDict[team],firsttothreetowersDict[team]]
    relationDf_first.index = relationDf_first.index + 1

relationDf_first = relationDf_first.sort_index()

relationDf_first = relationDf_first.dropna(axis=0)


option = st.selectbox('choose option',col)
    
sb.set(font_scale=1.5)    
fig=plt.figure(figsize=(10, 10))
sb.regplot(data=relationDf_first,x=option,y='winRate')
plt.title(option + ' and winRate')
plt.xlabel(option)
plt.ylabel('winRate')
st.pyplot(fig)

trendData = pd.DataFrame(columns = ['category','coefficient','intercept','r2 score'])
for c in col:
    model=LinearRegression()
    var = np.array(relationDf_first[c]).reshape((-1,1))
    winRate = np.array(relationDf_first['winRate']).reshape((-1,1))
    model.fit(var,winRate)
    coef = model.coef_[0][0]
    intercept = model.intercept_[0]
    r2 = model.score(var,winRate)
    #print(c + ' - coefficient of determination and r2 score is ',coef,r2)
    trendData.loc[-1] = [c,coef,intercept,r2]
    trendData.index +=1

trendData = trendData.round(3)

trendData.insert(4,'form','tmp')

form = []
for idx, row in trendData.iterrows():
    form.append(str(row['coefficient']) + "x + " + str(row['intercept']))

trendData['form'] = form

plt.figure(figsize=(10,5))
plt.xticks(rotation=45)
sb.set(font_scale=1.5)
gp_plot = sb.barplot(y='coefficient',x='category',data=trendData)
gp_plot.set_xlabel("category",fontsize="15")
gp_plot.set_ylabel("coefficient",fontsize="15")



for p in gp_plot.patches:
    gp_plot.text(p.get_x() + (p.get_width()/2.0) ,  
            p.get_y() + p.get_height(),   
            f"{p.get_height():.3f}",    
            ha = 'center' )   



plt.title("coefficient of winRate and Kill")
st.pyplot(plt)

form = []
for idx, row in trendData.iterrows():
    form.append(str(row['coefficient']) + "x + " + str(row['intercept']))

trendData['form'] = form
st.table(trendData)