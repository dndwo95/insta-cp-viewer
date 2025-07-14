
import streamlit as st
import pandas as pd

# 비밀번호 설정
PASSWORD = "dndwo"

# 비밀번호 입력
st.title("🔐 InstaViewCP - 쿠팡 릴스 인기 제품 분석기")
password_input = st.text_input("비밀번호를 입력하세요", type="password")

if password_input != PASSWORD:
    st.warning("올바른 비밀번호를 입력해야 이용할 수 있습니다.")
    st.stop()

# 로그인 성공 시 아래 실행
st.success("✅ 비밀번호 인증 완료! 분석 도구를 사용할 수 있어요.")

# 계정 입력
st.subheader("📱 분석할 인스타그램 계정을 입력하세요")
accounts = st.text_area("계정 리스트 입력 (쉼표로 구분)", "@salim_explorer, @deal_holic")

# 기간 선택
st.subheader("🗓 분석 기간 설정")
period = st.selectbox("기간 선택", ["최근 7일", "최근 30일"])

# 분석 버튼
if st.button("🔍 분석 시작"):
    # 입력된 계정 처리
    accounts_list = [acc.strip() for acc in accounts.split(",") if acc.strip()]
    if not accounts_list:
        st.warning("최소 1개 이상의 계정을 입력해주세요.")
        st.stop()

    # 더미 데이터 생성
    data = {
        "순위": [1, 2, 3, 4, 5],
        "제품명": ["라탄 조명", "무소음 벽시계", "플러피 러그", "4단 수납장", "LED 무드등"],
        "조회수": [245000, 198000, 157000, 139000, 122000],
        "계정": [accounts_list[0]] * 5,
        "영상 링크": [
            "https://instagram.com/reel/abc1",
            "https://instagram.com/reel/abc2",
            "https://instagram.com/reel/abc3",
            "https://instagram.com/reel/abc4",
            "https://instagram.com/reel/abc5"
        ]
    }

    df = pd.DataFrame(data)
    st.subheader("📊 분석 결과 (예시 데이터)")
    st.dataframe(df)

    # 다운로드
    csv = df.to_csv(index=False).encode("utf-8-sig")
    st.download_button("⬇️ 결과 CSV 다운로드", csv, "insta_analysis.csv", "text/csv")
