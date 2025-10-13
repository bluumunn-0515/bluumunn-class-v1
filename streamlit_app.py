import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# --- Streamlit 요소 예시 (각주 포함) ---

st.header("1. 텍스트 및 제목 요소")  # 페이지의 섹션 구분용 헤더
st.subheader("1-1. 서브헤더")  # 소제목
st.text("이것은 일반 텍스트입니다.")  # 단순 텍스트
st.markdown("**마크다운** _스타일링_ 지원!")  # 마크다운 지원
st.caption("설명 또는 부가 정보에 사용")  # 작은 글씨 설명
st.code('print("Hello, Streamlit!")', language='python')  # 코드 블록
st.latex(r"E=mc^2")  # LaTeX 수식

st.header("2. 입력 위젯")
name = st.text_input("이름을 입력하세요")  # 텍스트 입력
age = st.number_input("나이", min_value=0, max_value=120, value=25)  # 숫자 입력
agree = st.checkbox("동의합니다")  # 체크박스
gender = st.radio("성별", ["남성", "여성", "기타"])  # 라디오 버튼
color = st.selectbox("좋아하는 색상", ["빨강", "초록", "파랑"])  # 셀렉트박스
colors = st.multiselect("선호 색상(복수 선택)", ["빨강", "초록", "파랑"])  # 다중 선택
date = st.date_input("날짜 선택")  # 날짜 입력
time = st.time_input("시간 선택")  # 시간 입력
file = st.file_uploader("파일 업로드")  # 파일 업로더
st.button("제출")  # 버튼

st.header("3. 출력 및 피드백")
st.success("성공 메시지!")  # 성공 메시지
st.info("정보 메시지")  # 정보 메시지
st.warning("경고 메시지")  # 경고 메시지
st.error("에러 메시지")  # 에러 메시지
st.exception(Exception("예외 메시지 예시"))  # 예외 메시지

st.header("4. 데이터 표시")
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(5, 3), columns=["A", "B", "C"])
st.dataframe(df)  # 동적 데이터프레임
st.table(df.head(3))  # 정적 테이블
st.json({"key": "value", "number": 123})  # JSON 표시

st.header("5. 차트와 시각화")
st.line_chart(df)  # 선 그래프
st.bar_chart(df)  # 막대 그래프
st.area_chart(df)  # 영역 그래프

st.header("6. 미디어")
st.image("https://placekitten.com/200/300", caption="고양이 이미지")  # 이미지
st.audio(np.random.randn(44100), sample_rate=44100)  # 오디오
st.video("https://www.w3schools.com/html/mov_bbb.mp4")  # 비디오

st.header("7. 레이아웃 및 기타")
col1, col2 = st.columns(2)  # 컬럼 분할
col1.write("왼쪽 컬럼")
col2.write("오른쪽 컬럼")

with st.expander("더보기(Expander)"):
    st.write("이곳에 추가 정보를 넣을 수 있습니다.")

st.sidebar.title("사이드바 예시")  # 사이드바
st.sidebar.button("사이드바 버튼")
