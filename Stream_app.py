import streamlit as st

st.set_page_config(page_title = "LOL data analysis",page_icon="🎮")

st.write("# Welcome to League of Legends data analysis streamlit!")

st.markdown(
  """
  ### 1. data_origin
  어떤 데이터를 분석했는지 알 수 있습니다.

  ### 2. How the data was analyzed
  데이터를 어떻게 분석했는지 알 수 있습니다.

  ### 3. analysis_result(kill)
  각 종 킬, 파괴 수와 승률관의 관계를 알 수 있습니다.

  ### 4. analysis_result(first)
  무엇을 첫번째로 하는 것이 좋은지 알 수 있습니다.

  ### 5. analysis_result(other)
  위 두개에 담지 못한 여러가지 결과를 알 수 있습니다.

  ### 6. reference
  이 결과를 도출하기까지 참고한 레퍼런스가 있습니다.

  ### 7. my_github
  데이터 분석 결과와 이 홈페이지의 소스코드의 github 링크입니다.
  """
)

#st.sidebar.success("Select a menu above.")







