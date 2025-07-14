
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# 비밀번호 설정
PASSWORD = "dndwo"

# 제목
st.title("🔐 InstaViewCP - 쿠팡 릴스 TOP 제품 분석기")
password_input = st.text_input("비밀번호를 입력하세요", type="password")

if password_input != PASSWORD:
    st.warning("올바른 비밀번호를 입력해야 이용할 수 있습니다.")
    st.stop()

st.success("✅ 인증 완료! 분석을 시작하세요.")

# 계정 입력
st.subheader("📱 분석할 인스타그램 계정을 입력하세요")
accounts_input = st.text_area("계정 리스트 입력 (쉼표로 구분)", "@salim_explorer, @deal_holic")
accounts = [acc.strip() for acc in accounts_input.split(",") if acc.strip()]

# 날짜 선택
st.subheader("🗓 분석 기간 설정")
start_date = st.date_input("시작일", datetime.today() - timedelta(days=7))
end_date = st.date_input("종료일", datetime.today())

# 분석 기준 선택
st.subheader("📊 분석 기준 선택")
analysis_type = st.selectbox("기준을 선택하세요", ["조회수 TOP 5", "댓글수 TOP 5"])

# 분석 시작
if st.button("🔍 분석 시작"):
    if not accounts:
        st.warning("계정을 하나 이상 입력해주세요.")
        st.stop()

    # 더미 데이터 생성
    dummy_data = {
        "계정": [accounts[0]] * 10,
        "제품명": [f"제품{i}" for i in range(1, 11)],
        "조회수": [100000 - i * 5000 for i in range(10)],
        "댓글수": [300 - i * 20 for i in range(10)],
        "릴스 링크": [f"https://instagram.com/reel/dummy{i}" for i in range(1, 11)],
        "업로드일": [datetime.today() - timedelta(days=i) for i in range(10)]
    }

    df = pd.DataFrame(dummy_data)

    # 날짜 필터 적용
    df_filtered = df[(df["업로드일"].dt.date >= start_date) & (df["업로드일"].dt.date <= end_date)]

    if analysis_type == "조회수 TOP 5":
        df_result = df_filtered.sort_values(by="조회수", ascending=False).head(5)
        st.subheader("🔥 조회수 기준 TOP 5 제품")
    else:
        df_result = df_filtered.sort_values(by="댓글수", ascending=False).head(5)
        st.subheader("💬 댓글수 기준 TOP 5 제품")

    st.dataframe(df_result)

    # CSV 다운로드
    csv = df_result.to_csv(index=False).encode("utf-8-sig")
    st.download_button("⬇️ 결과 CSV 다운로드", csv, "top5_result.csv", "text/csv")
