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
    """
    <h1 style='text-align: center; color: #ff4500;'>
    🌈 오늘의 기분에 맞는 음식 추천 🍔🍰🍕
    </h1>
    """,
    unsafe_allow_html=True,
)

st.write("💡 당신의 기분을 선택하면 딱 맞는 음식을 추천해드려요!")

# 기분 선택
selected_mood = st.selectbox("👇 지금 기분을 선택하세요", options=list(mood_foods.keys()))

if selected_mood:
    foods = mood_foods[selected_mood]
    random.shuffle(foods)

    # 결과 출력
    st.markdown(f"<h2 style='color: #ff6347;'>✨ {selected_mood}에 추천하는 음식 ✨</h2>", unsafe_allow_html=True)
    for food in foods:
        st.markdown(f"👉 {food}")
    st.success("😋 맛있는 음식으로 기분 업! 즐거운 하루 되세요!")

    # 🍔🍩 음식 터지는 애니메이션 (한 번)
    falling_foods = "".join(
        f"<div class='food' style='left:{random.randint(10,90)}%; "
        f"animation-delay:{random.uniform(0,1.5)}s; "
        f"animation-duration:{random.uniform(0.5,2.5)}s; "
        f"font-size:{random.randint(30,60)}px;'>{food}</div>"
        for food in foods * 5  # 각 음식 여러 번 터지도록
    )

    unique_key = str(uuid.uuid4())  # 매번 고유 key 생성

    st.markdown(
        f"""
        <style>
        .falling-container-{unique_key} {{
            position: fixed;
            top: 50%;
            left: 50%;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 9999;
        }}
        .food {{
            position: absolute;
            top: 50%;
            transform: translate(-50%, -50%);
            animation: pop linear forwards;
        }}
        @keyframes pop {{
            0% {{
                transform: translate(-50%, -50%) scale(0);
                opacity: 1;
            }}
            50% {{
                transform: translate(-50%, -50%) scale(1.5);
                opacity: 1;
            }}
            100% {{
                transform: translate(-50%, -50%) scale(0);
                opacity: 0;
            }}
        }}
        </style>
        <div class="falling-container-{unique_key}">
            {falling_foods}
        </div>
        """,
        unsafe_allow_html=True,
    )

