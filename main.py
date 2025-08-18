import streamlit as st

# MBTI별 직업 추천 데이터 (예시)
mbti_jobs = {
    "INTJ": ["전략 컨설턴트", "데이터 사이언티스트", "연구원", "정책 분석가"],
    "ENTP": ["기업가", "마케팅 매니저", "광고 기획자", "변호사"],
    "INFJ": ["심리상담사", "작가", "사회복지사", "교사"],
    "ENFP": ["광고 크리에이티브", "공연 예술가", "홍보 전문가", "교육자"],
    "ISTJ": ["회계사", "세무사", "군인", "프로젝트 매니저"],
    "ESTJ": ["경영자", "공무원", "팀 리더", "운영 매니저"],
    "ISFP": ["디자이너", "작곡가", "사진작가", "작가"],
    "ESFP": ["배우", "이벤트 기획자", "방송인", "여행 가이드"],
    # 필요에 따라 나머지 MBTI도 추가 가능
}

st.title("🔮 MBTI 기반 진로 추천 웹앱")
st.write("당신의 MBTI를 선택하면 어울리는 직업을 추천해드려요!")

# MBTI 선택
selected_mbti = st.selectbox("MBTI를 선택하세요", options=list(mbti_jobs.keys()))

if selected_mbti:
    st.subheader(f"✨ {selected_mbti} 유형을 위한 추천 직업")
    jobs = mbti_jobs.get(selected_mbti, ["추천 직업 데이터 없음"])
    for job in jobs:
        st.markdown(f"- {job}")


