import streamlit as st
import random
import uuid

# 기분별 음식 추천 데이터
mood_foods = {
    "행복 😊": ["🍰 케이크", "🍦 아이스크림", "🍫 초콜릿", "🍩 도넛"],
    "슬픔 😢": ["☕ 따뜻한 커피", "🍫 초콜릿", "🍲 따뜻한 수프"],
    "스트레스 😫": ["🥗 샐러드", "🍵 허브차", "🍌 바나나"],
    "피곤 😴": ["🥤 에너지 음료", "🍫 초콜릿 바", "🍌 바나나"],
    "짜증 😠": ["🍫 초콜릿", "🍪 쿠키", "🍟 감자튀김"],
    "심심 😐": ["🍿 팝콘", "🍕 피자", "🍡 간식"],
    "사랑 😍": ["🍓 딸기", "🍫 초콜릿", "🍰 케이크"]
}

# 페이지 설정
st.set_page_config(page_title="기분별 음식 추천 🍴", page_icon="🍔", layout="centered")

# 헤더
st.markdown(
    "<h1 style='text-align:center;color:#ff4500;'>🌈 기분별 음식 추천 & 폭발 🍔🍰🍕</h1>",
    unsafe_allow_html=True
)

# 기분 선택
selected_mood = st.selectbox("👇 지금 기분을 선택하세요", options=list(mood_foods.keys()))

if selected_mood:
    foods = mood_foods[selected_mood]
    random.shuffle(foods)

    # 1️⃣ 결과 텍스트 출력
    st.markdown(f"<h2 style='color:#ff6347;'>✨ {selected_mood}에 추천하는 음식 ✨</h2>", unsafe_allow_html=True)
    for food in foods:
        st.markdown(f"👉 {food}")
    st.success("😋 맛있는 음식으로 기분 업! 즐거운 하루 되세요!")

    # 2️⃣ 음식 폭발 애니메이션 (동시다발적)
    exploding_foods = "".join(
        f"<div class='food' style='left:{random.randint(10,90)}%; "
        f"top:{random.randint(20,80)}%; "
        f"animation-duration:{random.uniform(1,2)}s; "
        f"font-size:{random.randint(40,70)}px;'>{random.choice(foods)}</div>"
        for _ in range(50)
    )

    unique_key = str(uuid.uuid4())

    st.markdown(
        f"""
        <style>
        .explosion-container-{unique_key} {{
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
            transform: translate(-50%, -50%) scale(0);
            animation: explode linear forwards;
        }}
        @keyframes explode {{
            0% {{ transform: translate(-50%, -50%) scale(0); opacity: 1; }}
            50% {{ transform: translate(-50%, -50%) scale(1.5); opacity: 1; }}
            100% {{ transform: translate(-50%, -50%) scale(0); opacity: 0; }}
        }}
        </style>
        <div class="explosion-container-{unique_key}">
            {exploding_foods}
        </div>
        """,
        unsafe_allow_html=True
    )
