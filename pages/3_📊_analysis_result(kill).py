import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from collections import defaultdict
import seaborn as sb
st.set_page_config(page_title="analysis_result(kill and winRate)", page_icon="📊")

match_data = pd.read_csv("2023_LoL_esports_match_data_from_OraclesElixir.csv")

match_data_origin=match_data

teamList = match_data_origin['teamid'].unique()

match_data_filtered = match_data_origin.loc[match_data_origin['position']=='team',['result','teamid','kills','doublekills','triplekills','quadrakills','pentakills','minionkills','monsterkills','dragons','opp_dragons','elementaldrakes','opp_elementaldrakes','elders','opp_elders','heralds','opp_heralds','barons','opp_barons','towers','opp_towers','turretplates','opp_turretplates','inhibitors','opp_inhibitors']]

match_data_filtered = match_data_filtered.dropna(axis=0)

winRate = defaultdict()
for team in teamList:
    teamFiltered = match_data_filtered.loc[match_data_filtered['teamid'] == team]
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
    teamFiltered = match_data_filtered.loc[match_data_filtered['teamid'] == team]
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

relationDf = pd.DataFrame(columns=["teamid","winRate","Kills","doubleKills","tripleKill","quadraKill","pentaKill","minionKill","monsterKill",'dragons','opp_dragons','elementaldrakes','opp_elementaldrakes','elders','opp_elders','heralds','opp_heralds','barons','opp_barons','towers','opp_towers','turretplates','opp_turretplates','inhibitors','opp_inhibitors'])

for team in teamList:
    relationDf.loc[-1] = [team,winRate[team],killDict[team],doubleDict[team],tripleDict[team],quadraDict[team],pentaDict[team],minionDict[team],monsterDict[team],dragonDict[team],oppDragonDict[team],elementaldrakesDict[team],oppElementaldrakes[team],elders[team],oppElders[team],heralds[team],opp_heralds[team],barons[team],opp_barons[team],towers[team],opp_towers [team],turretplates[team],opp_turretplates [team],inhibitors[team],opp_inhibitors[team]]
    relationDf.index = relationDf.index + 1

relationDf = relationDf.sort_index()

relationDf = relationDf.dropna(axis=0)

col = ["Kills","doubleKills","tripleKill","quadraKill","pentaKill","minionKill","monsterKill",'dragons','opp_dragons','elementaldrakes','opp_elementaldrakes','elders','opp_elders','heralds','opp_heralds','barons','opp_barons','towers','opp_towers','turretplates','opp_turretplates','inhibitors','opp_inhibitors']

tabs = st.tabs(col)

for i in range(len(tabs)):
    with tabs[i]:
        fig=plt.figure(figsize=(10, 10))
        sb.regplot(data=relationDf,x=col[i],y='winRate')
        plt.title(col[i] + ' and winRate')
        plt.xlabel(col[i])
        plt.ylabel('winRate')
        st.pyplot(fig)


