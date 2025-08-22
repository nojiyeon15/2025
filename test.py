import streamlit as st
import random

st.set_page_config(page_title="스트레스 관리 솔루션", page_icon="🧘", layout="centered")

# 세션 상태 초기화
if "page" not in st.session_state:
    st.session_state.page = "form"

# ------------------------------
# 1️⃣ 설문 입력 페이지
# ------------------------------
if st.session_state.page == "form":
    st.title("🧘 스트레스 관리 솔루션")
    st.write("아래 질문에 답하면, 당신만의 맞춤 스트레스 해소법을 추천해드려요!")

    st.header("📋 설문 질문")

    # 6개 이상의 간접 질문
    q1 = st.radio("최근 잠들기 어렵거나 자주 깨나요?", ["전혀 아니다", "가끔 그렇다", "자주 그렇다"])
    q2 = st.radio("식사 시간이 불규칙한 편인가요?", ["전혀 아니다", "가끔 그렇다", "자주 그렇다"])
    q3 = st.radio("작은 일에도 쉽게 짜증이 나나요?", ["전혀 아니다", "가끔 그렇다", "자주 그렇다"])
    q4 = st.radio("집중력이 떨어지거나 일을 미루는 일이 잦나요?", ["전혀 아니다", "가끔 그렇다", "자주 그렇다"])
    q5 = st.radio("두통, 근육 긴장, 소화 불량을 느낀 적이 있나요?", ["전혀 아니다", "가끔 그렇다", "자주 그렇다"])
    q6 = st.radio("최근 피로감을 자주 느끼나요?", ["전혀 아니다", "가끔 그렇다", "자주 그렇다"])
    q7 = st.radio("하루 중 기분이 쉽게 변하거나 우울감을 느낀 적이 있나요?", ["전혀 아니다", "가끔 그렇다", "자주 그렇다"])

    # 버튼 클릭 시 결과 페이지로 이동
    if st.button("결과 보기 👉"):
        # 점수 계산 (0,1,2)
        mapping = {"전혀 아니다":0, "가끔 그렇다":1, "자주 그렇다":2}
        score = sum([mapping[q] for q in [q1,q2,q3,q4,q5,q6,q7]])
        st.session_state.score = score

        # 페이지 전환
        st.session_state.page = "result"
        st.rerun()

# ------------------------------
# 2️⃣ 결과 페이지
# ------------------------------
elif st.session_state.page == "result":
    st.title("💡 스트레스 관리 솔루션 결과")

    score = st.session_state.score

    # 스트레스 수준 피드백
    if score <= 5:
        st.success("스트레스 수준이 낮습니다. 현재 상태를 유지하세요! 😌")
    elif 6 <= score <= 10:
        st.warning("중간 정도의 스트레스가 감지되었습니다. 작은 휴식이 필요해요.")
    else:
        st.error("스트레스 수준이 높습니다. 적극적인 관리가 필요해요! 🛑")

    # 맞춤형 추천
    st.subheader("✨ 맞춤형 스트레스 해소법 추천")
    if score <= 5:
        st.write("- 가벼운 산책이나 스트레칭으로 하루를 여유롭게 보내세요 🚶‍♀️")
        st.write("- 좋아하는 음악을 들으며 마음을 정리해보세요 🎶")
    elif 6 <= score <= 10:
        st.write("- 짧은 명상이나 호흡법으로 마음을 진정시키세요 🧘")
        st.write("- 충분한 수면과 규칙적인 식사로 생활 패턴을 안정화하세요 🛌")
    else:
        st.write("- 적극적인 운동과 명상으로 스트레스 해소를 시도하세요 💪")
        st.write("- 필요시 친구, 가족, 전문가와 솔직한 대화를 해보세요 🗣️")
        st.write("- 일상에서 작은 휴식 시간을 자주 가져보세요 🍵")

    # 랜덤 긍정 메시지
    messages = [
        "오늘도 충분히 잘하고 있어요 💪",
        "스스로를 칭찬하는 하루를 보내세요 🌸",
        "작은 쉼이 큰 힘이 됩니다 🍀",
        "당신은 혼자가 아니에요 🤝"
    ]
    st.info(random.choice(messages))

    # 다시 하기 버튼
    if st.button("🔄 다시 검사하기"):
        st.session_state.page = "form"
        st.rerun()
