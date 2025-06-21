# streamlit_app.py

import streamlit as st
import pandas as pd

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("list.csv")  # 로컬에 있는 파일 또는 URL 가능
    return df

# 제목
st.title("📍 지역별 맛집 리스트")

# 데이터 로딩
data = load_data()

# 지역 선택 필터
regions = data["지역"].dropna().unique()
selected_region = st.selectbox("지역을 선택하세요", sorted(regions))

# 음식 종류 필터 (선택적)
food_types = data[data["지역"] == selected_region]["음식종류"].dropna().unique()
selected_food = st.selectbox("음식 종류를 선택하세요", sorted(food_types))

# 필터 적용
filtered_data = data[
    (data["지역"] == selected_region) &
    (data["음식종류"] == selected_food)
]

# 출력
st.subheader(f"🔍 '{selected_region}' 지역 '{selected_food}' 맛집 리스트")
st.dataframe(filtered_data[["업체명", "주소", "전화번호"]].reset_index(drop=True))
