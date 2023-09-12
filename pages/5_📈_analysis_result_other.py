import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import r2_score
from collections import defaultdict
import numpy as np
import seaborn as sb



st.set_page_config(page_title="analysis_result(other)", page_icon="📈")
League = pd.read_csv('Champion Stats - OraclesElixir.csv')

gp_data = League[["Champion","Pos","GP"]]
gp_data["Champion"] = gp_data["Champion"] +'(' +gp_data["Pos"] + ')'

gp_data_with_pos = gp_data

gp_data_with_pos_filtered = gp_data_with_pos[["Champion","GP"]]
gp_data_with_pos_filtered = gp_data_with_pos_filtered.sort_values(by=['GP'],ascending=False)

plt.figure(figsize=(10,100))
sb.set(font_scale=1.5)
gp_plot = sb.barplot(y='Champion',x='GP',data=gp_data_with_pos_filtered,orient='h',errorbar=None)
gp_plot.set_xlabel("Champion(position)",fontsize="15")
gp_plot.set_ylabel("Game played",fontsize="15")



for p in gp_plot.patches:
    gp_plot.text(p.get_x() + (p.get_width()*2.0/3.0) ,  
            p.get_y() + p.get_height(),   
            f"{p.get_width():.0f}",    
            ha = 'center' )   



plt.title("Number of Game plays by champion")
st.pyplot(plt)

match_data = pd.read_csv("2023_LoL_esports_match_data_from_OraclesElixir.csv")

match_data_origin=match_data

match_data_filtered = match_data.loc[match_data['position']=='team',['result','firstblood']]

match_data_filtered = match_data_filtered.dropna(axis=0)


#match_data_filtered

model=LogisticRegression()
FB = np.array(match_data_filtered.loc[:,'firstblood']).reshape((-1,1))
result = np.array(match_data_filtered.loc[:,'result'])
model.fit(FB,result)
print(' - coefficient of determination and r2 score is ',model.coef_[0],model.score(FB,result))

match_data_filtered_player = match_data.loc[match_data['position']!='team',['position','result','firstblood']]

match_data_filtered_player = match_data_filtered_player.dropna(axis=0)


#match_data_filtered_player

pos = ['top','mid','sup','bot','jng']
coef_W_FB = []

FB=""
W=""
for p in pos:
    model=LogisticRegression()
    FB = np.array(match_data_filtered_player.loc[match_data_filtered_player['position']==p,'firstblood']).reshape((-1,1))
    W = np.array(match_data_filtered_player.loc[match_data_filtered_player['position']==p,'result'])
    model.fit(FB,W)
    #print(p + ' - coefficient of determination and r2 score is ',model.coef_[0],model.score(FB,W))
    coef_W_FB.append(model.coef_[0][0])

tmp = pd.DataFrame({'position' : pos, 'coefficient' : coef_W_FB})


plt.figure(figsize=(10,10))
sb.set(font_scale=1.5)
gp_plot = sb.barplot(y='coefficient',x='position',data=tmp,errorbar=None)
gp_plot.set_xlabel("position",fontsize="15")
gp_plot.set_ylabel("coefficient",fontsize="15")



for p in gp_plot.patches:
    gp_plot.text(p.get_x() + (p.get_width()/2.0) ,  
            p.get_y() + p.get_height(),   
            f"{p.get_height():.2f}",    
            ha = 'center' )   



plt.title("coefficient of winRate and firstblood")
st.pyplot(plt)

st.write('**모든데이터는 소수 셋째자리에서 반올림함**')