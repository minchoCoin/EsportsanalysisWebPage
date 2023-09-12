import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from collections import defaultdict
import numpy as np
import seaborn as sb

def data_result1():
    st.set_page_config(page_title="analysis_result(kill and winRate)", page_icon="📊")

    match_data = pd.read_csv("2023_LoL_esports_match_data_from_OraclesElixir.csv")

    match_data_origin=match_data


    
    
    teamList = match_data_origin['teamname'].unique()

    match_data_filtered = match_data_origin.loc[match_data_origin['position']=='team',['result','teamname','teamid','kills','doublekills','triplekills','quadrakills','pentakills','minionkills','monsterkills','dragons','opp_dragons','elementaldrakes','opp_elementaldrakes','elders','opp_elders','heralds','opp_heralds','barons','opp_barons','towers','opp_towers','turretplates','opp_turretplates','inhibitors','opp_inhibitors']]

    match_data_filtered = match_data_filtered.dropna(axis=0)

    optionName = st.selectbox(
    'team select',
    ['all'].extend(list(teamList)))

    winRate = defaultdict()


    if optionName !='all':
        teamList = [optionName]
    for team in teamList:
        teamFiltered = match_data_filtered.loc[match_data_filtered['teamname'] == team]
        winRate[team] = teamFiltered['result'].mean()
    

    killDict = {}
    doubleDict = {}
    tripleDict = {}
    quadraDict = {}
    pentaDict = {}
    minionDict = {}
    monsterDict = {}
    dragonDict = {}
    oppDragonDict = {}
    elementaldrakesDict = {}
    oppElementaldrakes = {}
    elders = {}
    oppElders = {}
    heralds = {}
    opp_heralds = {}
    barons = {}
    opp_barons = {}
    towers = {}
    opp_towers = {}
    turretplates = {}
    opp_turretplates = {}
    inhibitors = {}
    opp_inhibitors = {}
    for team in teamList:
        teamFiltered = match_data_filtered.loc[match_data_filtered['teamname'] == team]
        killDict[team] = teamFiltered['kills'].mean()
        doubleDict[team] = teamFiltered['doublekills'].mean()
        tripleDict[team] = teamFiltered['triplekills'].mean()
        quadraDict[team] = teamFiltered['quadrakills'].mean()
        pentaDict[team] = teamFiltered['pentakills'].mean()
        minionDict[team] = teamFiltered['minionkills'].mean()
        monsterDict[team] = teamFiltered['monsterkills'].mean()
        dragonDict [team] = teamFiltered['dragons'].mean()
        oppDragonDict[team] = teamFiltered['opp_dragons'].mean()
        elementaldrakesDict[team] = teamFiltered['elementaldrakes'].mean()
        oppElementaldrakes[team] = teamFiltered['opp_elementaldrakes'].mean()
        elders[team]= teamFiltered['elders'].mean()
        oppElders [team]= teamFiltered['opp_elders'].mean()
        heralds[team]= teamFiltered['heralds'].mean()
        opp_heralds[team]= teamFiltered['opp_heralds'].mean()
        barons[team]= teamFiltered['barons'].mean()
        opp_barons[team]= teamFiltered['opp_barons'].mean()
        towers[team]= teamFiltered['towers'].mean()
        opp_towers [team]= teamFiltered['opp_towers'].mean()
        turretplates[team]= teamFiltered['turretplates'].mean()
        opp_turretplates [team]= teamFiltered['opp_turretplates'].mean()
        inhibitors[team]= teamFiltered['inhibitors'].mean()
        opp_inhibitors[team]= teamFiltered['opp_inhibitors'].mean()

    relationDf = pd.DataFrame(columns=["teamname","winRate","Kills","doubleKills","tripleKill","quadraKill","pentaKill","minionKill","monsterKill",'dragons','opp_dragons','elementaldrakes','opp_elementaldrakes','elders','opp_elders','heralds','opp_heralds','barons','opp_barons','towers','opp_towers','turretplates','opp_turretplates','inhibitors','opp_inhibitors'])

    for team in teamList:
        relationDf.loc[-1] = [team,winRate[team],killDict[team],doubleDict[team],tripleDict[team],quadraDict[team],pentaDict[team],minionDict[team],monsterDict[team],dragonDict[team],oppDragonDict[team],elementaldrakesDict[team],oppElementaldrakes[team],elders[team],oppElders[team],heralds[team],opp_heralds[team],barons[team],opp_barons[team],towers[team],opp_towers [team],turretplates[team],opp_turretplates [team],inhibitors[team],opp_inhibitors[team]]
        relationDf.index = relationDf.index + 1

    relationDf = relationDf.sort_index()

    relationDf = relationDf.dropna(axis=0)

    col = ["Kills","doubleKills","tripleKill","quadraKill","pentaKill","minionKill","monsterKill",'dragons','opp_dragons','elementaldrakes','opp_elementaldrakes','elders','opp_elders','heralds','opp_heralds','barons','opp_barons','towers','opp_towers','turretplates','opp_turretplates','inhibitors','opp_inhibitors']

    
    option = st.selectbox('choose option',col)
    
    
    fig=plt.figure(figsize=(10, 10))
    sb.regplot(data=relationDf,x=option,y='winRate')
    plt.title(option + ' and winRate')
    plt.xlabel(option)
    plt.ylabel('winRate')
    st.pyplot(fig)
    

    trendData = pd.DataFrame(columns = ['category','coefficient','intercept','r2 score'])
    for c in col:
        model=LinearRegression()
        var = np.array(relationDf[c]).reshape((-1,1))
        winRate = np.array(relationDf['winRate']).reshape((-1,1))
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
    
    option2 = st.selectbox('choose option',['kill','monster_kill','opp_monster_kill','destroying','opp_destorying'])


    if option2 == 'kill':
        fig=plt.figure(figsize=(5,5))
        plt.xticks(rotation=45)
        sb.set(font_scale=1.5)
        gp_plot = sb.barplot(y='coefficient',x='category',data=trendData.loc[trendData['category'].isin(["Kills","doubleKills","tripleKill","quadraKill","pentaKill"]),:],errorbar=None)
        gp_plot.set_xlabel("category",fontsize="15")
        gp_plot.set_ylabel("coefficient",fontsize="15")



        for p in gp_plot.patches:
            gp_plot.text(p.get_x() + (p.get_width()/2.0) ,  
            p.get_y() + p.get_height(),   
            f"{p.get_height():.3f}",    
            ha = 'center' )   



        plt.title("coefficient of winRate and Kill")
        st.pyplot(fig)  

    elif option2=='monster_kill':
        fig=plt.figure(figsize=(10,5))
        plt.xticks(rotation=45)
        sb.set(font_scale=1.5)
        gp_plot = sb.barplot(y='coefficient',x='category',data=trendData.loc[trendData['category'].isin(['dragons','elementaldrakes','elders','heralds','barons']),:],errorbar=None)
        gp_plot.set_xlabel("category",fontsize="15")
        gp_plot.set_ylabel("coefficient",fontsize="15")



        for p in gp_plot.patches:
            gp_plot.text(p.get_x() + (p.get_width()/2.0) ,  
            p.get_y() + p.get_height(),   
            f"{p.get_height():.3f}",    
            ha = 'center' )   



        plt.title("coefficient of winRate and monster kill")
        st.pyplot(fig)  

    elif option2 =='opp_monster_kill':
        #'towers','opp_towers','turretplates','opp_turretplates','inhibitors','opp_inhibitors'
        fig=plt.figure(figsize=(10,5))
        plt.xticks(rotation=45)
        sb.set(font_scale=1.5)
        gp_plot = sb.barplot(y='coefficient',x='category',data=trendData.loc[trendData['category'].isin(['opp_dragons','opp_elementaldrakes','opp_elders','opp_heralds','opp_barons']),:],errorbar=None)
        gp_plot.set_xlabel("category",fontsize="15")
        gp_plot.set_ylabel("coefficient",fontsize="15")



        for p in gp_plot.patches:
            gp_plot.text(p.get_x() + (p.get_width()/2.0) ,  
                    p.get_y() + p.get_height(),   
                    f"{p.get_height():.3f}",    
                    ha = 'center' )   



        plt.title("coefficient of winRate and opp_monster")
        st.pyplot(fig)  

    elif option2 == 'destroying':
            #'towers','opp_towers','turretplates','opp_turretplates','inhibitors','opp_inhibitors'
        fig=plt.figure(figsize=(5,5))
        #plt.xticks(rotation=45)
        sb.set(font_scale=1.5)
        gp_plot = sb.barplot(y='coefficient',x='category',data=trendData.loc[trendData['category'].isin(['towers','turretplates','inhibitors']),:],errorbar=None)
        gp_plot.set_xlabel("category",fontsize="15")
        gp_plot.set_ylabel("coefficient",fontsize="15")



        for p in gp_plot.patches:
            gp_plot.text(p.get_x() + (p.get_width()/2.0) ,  
                    p.get_y() + p.get_height(),   
                    f"{p.get_height():.3f}",    
                    ha = 'center' )   



        plt.title("coefficient of winRate and destroying")
        st.pyplot(fig)  

    elif option2 =='opp_destroying':
                #'towers','opp_towers','turretplates','opp_turretplates','inhibitors','opp_inhibitors'
        fig=plt.figure(figsize=(7,5))
        #plt.xticks(rotation=45)
        sb.set(font_scale=1.5)
        gp_plot = sb.barplot(y='coefficient',x='category',data=trendData.loc[trendData['category'].isin(['opp_towers','opp_turretplates','opp_inhibitors']),:],errorbar=None)
        gp_plot.set_xlabel("category",fontsize="15")
        gp_plot.set_ylabel("coefficient",fontsize="15")



        for p in gp_plot.patches:
            gp_plot.text(p.get_x() + (p.get_width()/2.0) ,  
                    p.get_y() + p.get_height(),   
                    f"{p.get_height():.3f}",    
                    ha = 'center' )   



        plt.title("coefficient of winRate and opp_destroying")
        st.pyplot(fig)  
    
    st.table(trendData)
data_result1()

st.write('**모든데이터는 소수 넷째자리에서 반올림함**')


