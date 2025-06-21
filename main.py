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
