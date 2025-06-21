# mbti_job_recommender.py
import streamlit as st

# ------------------- 설정 -------------------
st.set_page_config(page_title="MBTI 직업 추천", page_icon="🧠", layout="centered")
st.markdown("<h1 style='text-align: center; color: #ff6f61;'>🌈 MBTI로 알아보는 나의 미래 직업 🌈</h1>", unsafe_allow_html=True)
st.markdown("### 당신의 성격 유형에 맞는 찰떡 직업을 추천해 드려요! 😎💼")

# ------------------- MBTI 목록 -------------------
mbti_types = {
    "INTJ": "🧠 전략가",
    "INTP": "🔬 논리학자",
    "ENTJ": "📈 통솔자",
    "ENTP": "🎙️ 변론가",
    "INFJ": "🌌 옹호자",
    "INFP": "🎨 중재자",
    "ENFJ": "📣 선도자",
    "ENFP": "🌈 활동가",
    "ISTJ": "📋 현실주의자",
    "ISFJ": "👼 수호자",
    "ESTJ": "🏗️ 경영자",
    "ESFJ": "🤝 외교관",
    "ISTP": "🛠️ 장인",
    "ISFP": "🎸 예술가",
    "ESTP": "🏎️ 사업가",
    "ESFP": "🎤 연예인"
}

# ------------------- 추천 직업 -------------------
recommendations = {
    "INTJ": ["💻 데이터 과학자", "🧠 전략 컨설턴트", "📊 금융 분석가"],
    "INTP": ["🔬 연구원", "👨‍💻 개발자", "📚 철학자"],
    "ENTJ": ["📈 CEO", "📊 비즈니스 기획자", "💼 변호사"],
    "ENTP": ["🎤 방송인", "🧠 창업가", "💡 마케터"],
    "INFJ": ["🧘‍♀️ 상담가", "🧑‍🏫 교육자", "📖 작가"],
    "INFP": ["🎨 일러스트레이터", "📖 시인", "🧑‍🎤 음악가"],
    "ENFJ": ["🧑‍🏫 교사", "🎤 MC", "👥 인사담당자"],
    "ENFP": ["📢 홍보 전문가", "🎬 영화감독", "🌍 여행가"],
    "ISTJ": ["📑 행정공무원", "💼 회계사", "⚖️ 법무사"],
    "ISFJ": ["🏥 간호사", "📘 도서관 사서", "👨‍👩‍👧‍👦 사회복지사"],
    "ESTJ": ["🏛️ 관리자", "💵 재무 관리자", "📈 영업팀장"],
    "ESFJ": ["🧑‍🍳 호텔리어", "👩‍🏫 유치원교사", "👩‍⚕️ 병원 코디네이터"],
    "ISTP": ["🚗 자동차정비사", "🧰 기계공학자", "🚒 소방관"],
    "ISFP": ["🎨 패션디자이너", "📸 사진작가", "🪴 플로리스트"],
    "ESTP": ["🚀 세일즈맨", "📸 유튜버", "🎢 이벤트 플래너"],
    "ESFP": ["🎤 가수", "💃 댄서", "🎭 배우"]
}

# ------------------- 사용자 선택 -------------------
selected_mbti = st.selectbox("🧬 당신의 MBTI를 선택하세요:", list(mbti_types.keys()), index=0, format_func=lambda x: f"{x} - {mbti_types[x]}")

if selected_mbti:
    st.markdown(f"<h2 style='color:#ffcc70;'>🎯 {selected_mbti} 유형에게 어울리는 직업은?</h2>", unsafe_allow_html=True)
    for job in recommendations[selected_mbti]:
        st.markdown(f"- {job}")
    
    st.success("🌟 꿈을 향해 나아가세요! 당신의 가능성은 무한합니다 💫")

# ------------------- 푸터 -------------------
st.markdown("---")
st.markdown("<p style='text-align: center;'>© 2025 by 진로꿈터. Powered by Streamlit 🚀</p>", unsafe_allow_html=True)

#-----------------추가



# 추천 직업 + 설명
recommendations = {
    "INTJ": [
        ("💻 데이터 과학자", "논리적인 사고와 분석력이 뛰어난 INTJ에게 딱 맞는 직업입니다. 데이터를 해석하고 미래를 예측하는 능력을 발휘할 수 있어요."),
        ("🧠 전략 컨설턴트", "복잡한 문제를 해결하고, 기업의 방향을 설계하는 데 탁월한 역량을 발휘할 수 있어요."),
        ("📊 금융 분석가", "수치에 강하고 신중한 성격이 금융 분야에서 강점을 가질 수 있게 합니다.")
    ],
    "INFP": [
        ("🎨 일러스트레이터", "감성적이고 창의적인 INFP에게 예술적인 직업은 최고의 선택이에요."),
        ("📖 시인", "마음속의 이야기를 글로 표현하는 재능을 발휘해보세요."),
        ("🧑‍🎤 음악가", "내면의 감정을 음악으로 표현하고, 사람들의 감성을 울릴 수 있어요.")
    ],
    "ENFP": [
        ("📢 홍보 전문가", "활동적인 성격과 열정적인 에너지를 활용할 수 있는 직업이에요."),
        ("🎬 영화감독", "아이디어가 넘치는 ENFP에게 창의력을 폭발시킬 무대가 되어줄 거예요."),
        ("🌍 여행가", "새로운 곳을 탐험하고 경험을 사람들과 나누는 걸 좋아한다면 이 직업이 제격!")
    ],
    # 👉 다른 MBTI도 원하면 추가해줄게!
}

# 사용자 선택
selected_mbti = st.selectbox("🧬 당신의 MBTI를 선택하세요:", list(mbti_types.keys()), index=0, format_func=lambda x: f"{x} - {mbti_types[x]}")

if selected_mbti:
    st.markdown(f"<h2 style='color:#ffcc70;'>🎯 {selected_mbti} 유형에게 어울리는 직업은?</h2>", unsafe_allow_html=True)
    
    jobs = recommendations.get(selected_mbti, [])
    
    if not jobs:
        st.warning("🙇‍♀️ 죄송해요! 아직 이 MBTI 유형에 대한 추천 직업이 준비되지 않았어요.")
    else:
        for title, description in jobs:
            with st.expander(f"{title}"):
                st.markdown(f"📝 **설명**: {description}")

    st.success("🌟 꿈을 향해 나아가세요! 당신의 가능성은 무한합니다 💫")

# 푸터
st.markdown("---")
st.markdown("<p style='text-align: center;'>© 2025 by 진로꿈터. Powered by Streamlit 🚀</p>", unsafe_allow_html=True)


