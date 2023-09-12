import streamlit as st


def github():
    
    st.set_page_config(page_title="my_github", page_icon="🌐")
    st.markdown(
        '''
        #### 아래 깃허브 repository에서 ipynb파일로 더 정확하게 데이터 분석 결과를 볼 수 있습니다.
         - https://github.com/minchoCoin/LOL_data_analysis_prj

        #### 아래 깃허브 repository에서 이 사이트가 어떤 방식으로 만들어졌는지 볼 수 있습니다.
         - https://github.com/minchoCoin/EsportsanalysisWebPage
        '''
    )

github()