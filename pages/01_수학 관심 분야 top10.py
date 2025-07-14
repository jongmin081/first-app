import streamlit as st
import plotly.express as px

# 페이지 설정
st.set_page_config(page_title="수학 관심 분야 TOP 10", layout="wide")

st.title("📊 학생들이 관심 갖는 수학 분야 TOP 10")
st.write("아래 그래프는 학생들이 가장 관심 있어 하는 수학 분야 상위 10개를 보여줍니다.")

# 수학 관심 분야 데이터 (예시)
data = {
    "분야": [
        "암호학", "프랙탈", "확률과 통계", "게임 이론", "수학과 예술",
        "정수론", "수학사", "파동과 삼각함수", "기하학", "리만 가설"
    ],
    "관심도(표 수)": [95, 88, 84, 80, 76, 73, 68, 65, 60, 55]
}

# Plotly Bar Chart
fig = px.bar(
    x=data["분야"],
    y=data["관심도(표 수)"],
    labels={"x": "수학 분야", "y": "관심도(표 수)"},
    title="📈 수학 관심 분야 TOP 10",
    text=data["관심도(표 수)"],
    color=data["관심도(표 수)"],
    color_continuous_scale="Blues"
)

fig.update_layout(xaxis_tickangle=-45)

# 그래프 출력
st.plotly_chart(fig, use_container_width=True)
