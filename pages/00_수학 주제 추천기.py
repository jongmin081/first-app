import streamlit as st

st.set_page_config(page_title="수학 주제 추천기", layout="centered")

st.title("📘 수학 주제 추천기")
st.write("관심 있는 수학 분야를 선택하면, 주제를 추천해드릴게요!")

# 분야 목록
categories = [
    "실생활 응용 수학",
    "순수수학",
    "수학사/수학자",
    "컴퓨터와 수학",
    "수학과 예술"
]

# 추천 주제 사전 (순수수학으로 이름 변경됨)
topic_recommendations = {
    "실생활 응용 수학": [
        "삼각함수로 소리와 파동 분석하기",
        "통계로 여론조사 해석하기",
        "함수 모델링으로 인구 예측하기"
    ],
    "순수수학": [
        "피보나치 수열과 황금비",
        "정수론으로 보는 암호의 원리",
        "리만 적분의 개념과 직관적인 이해"
    ],
    "수학사/수학자": [
        "가우스의 수학적 생애와 업적",
        "고대 바빌로니아 수학 탐구",
        "여성 수학자들의 기여"
    ],
    "컴퓨터와 수학": [
        "이진수와 컴퓨터 연산의 원리",
        "그래프 이론과 네트워크 분석",
        "프랙탈과 알고리즘의 세계"
    ],
    "수학과 예술": [
        "에셔의 작품에 숨겨진 대칭성",
        "프랙탈 아트: 수학으로 그리는 그림",
        "황금비와 건축 디자인"
    ]
}

# 사용자 입력
selected_category = st.selectbox("관심 있는 수학 분야를 선택하세요:", categories)

# 추천 주제 출력
if selected_category:
    st.subheader(f"🔎 '{selected_category}' 분야 추천 주제:")
    for i, topic in enumerate(topic_recommendations[selected_category], 1):
        st.write(f"{i}. {topic}")

