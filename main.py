import streamlit as st
import random
import uuid

# MBTI별 직업 추천 데이터 (16유형 모두)
mbti_jobs = {
    "INTJ": ["🧠 전략 컨설턴트", "📊 데이터 사이언티스트", "🔬 연구원", "📑 정책 분석가"],
    "INTP": ["💻 프로그래머", "🔎 연구원", "🤖 AI 개발자", "📚 학자"],
    "ENTJ": ["👔 CEO", "📈 투자 분석가", "🏛 경영 컨설턴트", "⚙️ 프로젝트 매니저"],
    "ENTP": ["🚀 기업가", "📢 마케팅 매니저", "🎨 광고 기획자", "⚖️ 변호사"],
    "INFJ": ["💬 심리상담사", "✍️ 작가", "🤝 사회복지사", "👩‍🏫 교사"],
    "INFP": ["🎨 아티스트", "🎶 작곡가", "📖 소설가", "🧘‍♂️ 상담사"],
    "ENFJ": ["🎤 강연가", "👩‍🏫 교육자", "🤝 인사 전문가", "🌍 사회운동가"],
    "ENFP": ["🎭 공연 예술가", "🎉 이벤트 기획자", "📸 크리에이터", "🎙 방송인"],
    "ISTJ": ["📂 회계사", "💼 세무사", "🛡 군인", "📋 프로젝트 매니저"],
    "ISFJ": ["🩺 간호사", "🍎 영양사", "👩‍🏫 교사", "👮 경찰관"],
    "ESTJ": ["👔 경영자", "🏛 공무원", "👥 팀 리더", "⚙️ 운영 매니저"],
    "ESFJ": ["💝 상담사", "🧑‍🍳 요리사", "🎤 아나운서", "👩‍🏫 교육 전문가"],
    "ISTP": ["🛠 기술자", "🚗 자동차 정비사", "🏍 레이서", "🔧 엔지니어"],
    "ISFP": ["🎨 디자이너", "🎵 작곡가", "📷 사진작가", "📖 작가"],
    "ESTP": ["🏅 운동선수", "💼 영업 전문가", "🎤 MC", "🎲 사업가"],
    "ESFP": ["🎬 배우", "🎉 이벤트 플래너", "🎙 방송인", "🧳 여행 가이드"],
}

# 🍕🍩🍦 음식 이모지 모음
food_emojis = ["🍕", "🍔", "🍟", "🌭", "🍣", "🍜", "🍦", "🍩", "🍫", "🍪", "🥞", "🍓", "🍉", "🍇"]

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

st.write("💡 당신의 성격과 딱 맞는 직업을 찾아보세요! 🚀🌟")

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

    st.success("🌟 자신만의 장점을 살려 꿈을 펼쳐보세요! 🌍✨")

    # 🎉 음식 떨어지는 애니메이션 (한 번, MBTI 바뀔 때마다 새로 실행)
    falling_foods = "".join(
        f"<div class='food' style='left:{random.randint(0,95)}%; "
        f"animation-delay:{random.uniform(0,3)}s; "
        f"animation-duration:{random.uniform(3,8)}s; "
        f"font-size:{random.randint(20,45)}px;'>{random.choice(food_emojis)}</div>"
        for _ in range(100)   # 음식 개수 넉넉하게
    )

    unique_key = str(uuid.uuid4())  # 매번 고유 key 생성

    st.markdown(
        f"""
        <style>
        .falling-container-{unique_key} {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 9999;
        }}
        .food {{
            position: absolute;
            top: -50px;
            animation: fall linear forwards;
        }}
        @keyframes fall {{
            0% {{ transform: translateY(0); opacity: 1; }}
            100% {{ transform: translateY(100vh); opacity: 0; }}
        }}
        </style>
        <div class="falling-container-{unique_key}">
            {falling_foods}
        </div>
        """,
        unsafe_allow_html=True,
    )
