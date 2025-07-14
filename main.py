import streamlit as st

st.set_page_config(page_title="MBTI 직업 추천기", layout="centered")

st.title("🌟 MBTI 기반 직업 추천기")
st.write("당신의 MBTI 유형을 선택하면, 그에 맞는 직업 3가지를 추천해드립니다!")

# MBTI 목록
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# MBTI별 추천 직업 사전
job_recommendations = {
    "INTJ": ["전략 컨설턴트", "데이터 과학자", "시스템 엔지니어"],
    "INTP": ["연구원", "이론 물리학자", "소프트웨어 개발자"],
    "ENTJ": ["기업 CEO", "프로젝트 매니저", "변호사"],
    "ENTP": ["광고 기획자", "기업가", "프로덕트 디자이너"],
    "INFJ": ["상담가", "작가", "심리학자"],
    "INFP": ["예술가", "시인", "사회복지사"],
    "ENFJ": ["교사", "HR 매니저", "정신건강 상담가"],
    "ENFP": ["마케터", "기획자", "작곡가"],
    "ISTJ": ["회계사", "행정 공무원", "품질 관리자"],
    "ISFJ": ["간호사", "초등학교 교사", "사회복지사"],
    "ESTJ": ["군인", "기업 관리자", "감사원"],
    "ESFJ": ["영업 관리자", "서비스 매니저", "간호 관리자"],
    "ISTP": ["기계공", "전기 기술자", "파일럿"],
    "ISFP": ["패션 디자이너", "플로리스트", "사진작가"],
    "ESTP": ["영업직", "응급 구조사", "스턴트 배우"],
    "ESFP": ["연예인", "이벤트 플래너", "여행 가이드"]
}

# 사용자 입력
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_types)

# 추천 결과 출력
if selected_mbti:
    st.subheader(f"🔍 {selected_mbti} 유형에게 추천하는 직업:")
    for i, job in enumerate(job_recommendations[selected_mbti], 1):
        st.write(f"{i}. {job}")
