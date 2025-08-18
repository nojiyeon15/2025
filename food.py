import streamlit as st
import random
import uuid

# 기분별 음식 추천 데이터
mood_foods = {
    "행복 😊": ["🍰", "🍦", "🍫", "🍩"],
    "슬픔 😢": ["☕", "🍫", "🍲"],
    "스트레스 😫": ["🥗", "🍵", "🍌"],
    "피곤 😴": ["🥤", "🍫", "🍌"],
    "짜증 😠": ["🍫", "🍪", "🍟"],
    "심심 😐": ["🍿", "🍕", "🍡"],
    "사랑 😍": ["🍓", "🍫", "🍰"]
}

# 페이지 설정
st.set_page_config(page_title="기분별 음식 폭발 🍴", page_icon="🍔", layout="centered")

st.markdown(
    "<h1 style='text-align:center;color:#ff4500;'>🌈 기분별 음식 폭발 🍔🍰🍕</h1>",
    unsafe_allow_html=True
)

selected_mood = st.selectbox("👇 지금 기분을 선택하세요", options=list(mood_foods.keys()))

if selected_mood:
    foods = mood_foods[selected_mood]

    # 랜덤으로 음식 배치, 속도, 크기 결정
    exploding_foods = "".join(
        f"<div class='food' style='left:{random.randint(10,90)}%; "
        f"top:{random.randint(20,80)}%; "
        f"animation-duration:{random.uniform(1,2)}s; "
        f"font-size:{random.randint(40,70)}px;'>{random.choice(foods)}</div>"
        for _ in range(50)  # 동시다발적 폭발
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
