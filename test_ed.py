import streamlit as st

st.set_page_config(page_title="지속 가능한 교육 접근성", layout="centered")

st.title("📚 지속 가능한 교육 접근성 확대")
st.write("지속 가능한 발전 목표(SDGs) 중 하나인 교육 접근성 확대에 대해 알아봅니다.")

# 정보 요약
st.header("🌍 왜 중요한가?")
st.markdown("""
- 전 세계 약 2억 명의 어린이와 청소년이 학교에 다니지 못합니다.
- 교육은 **빈곤을 줄이고**, **성 평등을 촉진**하며, **지속 가능한 사회를 만드는 핵심**입니다.
- 디지털 격차, 지역 간 교육 인프라 불균형 등은 해결해야 할 과제입니다.
""")

st.header("📌 주요 해결 방안")
st.markdown("""
1. 온라인 학습 플랫폼의 확대
2. 무료/공공 교재 및 콘텐츠 보급
3. 소외 지역(농촌, 개발도상국)에 대한 교육 인프라 투자
4. 특수교육과 평생교육의 강화
5. 정부·NGO·민간기업 간 협력
""")

# 사용자 입력
st.header("📝 나의 생각")
user_idea = st.text_area("당신은 '지속 가능한 교육 접근성 확대'를 위해 어떤 아이디어나 의견이 있나요?", height=150)

if user_idea:
    st.success("좋은 의견이에요! 아래에 요약해드립니다:")
    st.markdown(f"**✏️ 요약:** {user_idea}")

# 출처/참고
st.caption("참고: 유엔 지속가능발전목표(SDG 4) - https://sdgs.un.org/goals")
