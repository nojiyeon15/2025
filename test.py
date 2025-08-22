import streamlit as st

st.set_page_config(page_title="스트레스 관리 솔루션", page_icon="🧘", layout="centered")

st.title("🧘 스트레스 관리 솔루션")
st.write("간단한 질문에 답하고, 당신만의 스트레스 해소법을 추천받아보세요!")

# 1. 사용자 입력
st.header("📋 스트레스 체크")

mood = st.radio("현재 기분 상태를 선택하세요", ["😃 좋음", "😐 보통", "😫 나쁨"])
stress_source = st.selectbox("주요 스트레스 원인은 무엇인가요?", 
                             ["학교/직장", "인간관계", "건강", "경제적 문제", "기타"])
sleep = st.radio("최근 수면 상태는 어떤가요?", ["충분", "보통", "부족"])
preference = st.multiselect("선호하는 해소 방법을 골라주세요", 
                            ["운동", "음악", "명상", "휴식", "대화"])

# 2. 스트레스 점수 계산
score = 0
if mood == "😐 보통":
    score += 2
elif mood == "😫 나쁨":
    score += 4

if sleep == "보통":
    score += 2
elif sleep == "부족":
    score += 4

if stress_source in ["학교/직장", "경제적 문제"]:
    score += 3
else:
    score += 2

# 3. 추천 솔루션
st.header("💡 나만의 스트레스 해소법")

if score <= 4:
    st.success("스트레스 수준이 낮습니다. 현재 상태를 유지하세요! 😌")
elif 5 <= score <= 8:
    st.warning("중간 정도의 스트레스가 감지되었습니다. 작은 휴식이 필요해요.")
else:
    st.error("스트레스 수준이 높습니다. 적극적인 관리가 필요해요! 🛑")

# 맞춤형 추천
st.subheader("✨ 추천 방법")
if "운동" in preference:
    st.write("- 가벼운 스트레칭이나 산책을 해보세요 🚶‍♀️")
if "음악" in preference:
    st.write("- 좋아하는 음악이나 힐링 음악을 들어보세요 🎶")
if "명상" in preference:
    st.write("- 5분 명상이나 호흡법을 시도해보세요 🧘")
if "휴식" in preference:
    st.write("- 따뜻한 차와 함께 잠시 휴식하세요 🍵")
if "대화" in preference:
    st.write("- 믿을 수 있는 사람과 솔직하게 대화해보세요 🗣️")

# 랜덤 긍정 메시지
import random
messages = [
    "오늘도 충분히 잘하고 있어요 💪",
    "스스로를 칭찬하는 하루를 보내세요 🌸",
    "작은 쉼이 큰 힘이 됩니다 🍀",
    "당신은 혼자가 아니에요 🤝"
]
st.info(random.choice(messages))

