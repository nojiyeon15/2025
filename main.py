import streamlit as st
import random

# MBTI별 직업 추천 데이터
mbti_jobs = {
    "INTJ": ["🧠 전략 컨설턴트", "📊 데이터 사이언티스트", "🔬 연구원", "📑 정책 분석가"],
    "ENTP": ["🚀 기업가", "📢 마케팅 매니저", "🎨 광고 기획자", "⚖️ 변호사"],
    "INFJ": ["💬 심리상담사", "✍️ 작가", "🤝 사회복지사", "👩‍🏫 교사"],
    "ENFP": ["🎭 공연 예술가", "🎤 방송인", "📸 크리에이터", "🎉 이벤트 기획자"],
    "ISTJ": ["📂 회계사", "💼 세무사", "🛡 군인", "📋 프로젝트 매니저"],
    "ESTJ": ["👔 경영자", "🏛 공무원", "👥 팀 리더", "⚙️ 운영 매니저"],
    "ISFP": ["🎨 디자이너", "🎵 작곡가", "📷 사진작가", "📖 작가"],
    "ESFP": ["🎬 배우", "🎉 이벤트 플래너", "🎙 방송인", "🧳 여행 가이드"],
}

# 페이지 설정
st.set_page_config(page_title="MBTI 진로 추천 🎯", page_icon="✨", layout="centered")

# 헤더
st.markdown(
    """
    <h1 style='text-align: center; color: #ff69b4;'>
    🌈🔮 MBTI 기반 진로 추천 🎓✨
    </h1>
    """,
    unsafe_allow_html=True,
)

st.write("당신의 성격을 반짝이는 직업과 연결해 드립니다! 💎💼")

# MBTI 선택
selected_mbti = st.selectbox("👇 당신의 MBTI를 선택하세요!", options=list(mbti_jobs.keys()))

# 결과 출력
if selected_mbti:
    st.markdown(
        f"<h2 style='color: #ff1493;'>✨ {selected_mbti} 유형 추천 직업 ✨</h2>",
        unsafe_allow_html=True,
    )

    jobs = mbti_jobs.get(selected_mbti, ["❌ 데이터 없음"])
    random.shuffle(jobs)

    for job in jobs:
        st.markdown(f"👉 {job}")

    st.success("💡 자신의 성격을 잘 살려서 꿈을 키워 보세요! 🚀🌟")
    st.balloons()
