import streamlit as st

# --- 페이지 설정 ---
# st.set_page_config(layout="wide") # 넓은 레이아웃을 원할 경우 주석 해제

# --- 세션 상태 초기화 ---
# 퀴즈 진행 상태를 저장하기 위해 session_state를 초기화합니다.
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
    st.session_state.score = 0

# --- 사이드바 메뉴 ---
with st.sidebar:
    st.title('🚗 학습 메뉴')
    menu = st.radio(
        "메뉴를 선택하세요.",
        ('홈', '개념 학습', '개념 확인 퀴즈', '전기 장치 찾아보기'),
        label_visibility="collapsed"
    )

# --- 퀴즈 데이터 ---
quiz_data = [
    {
        "type": "multiple_choice",
        "question": "1. 옴의 법칙(V=IR)에 대한 설명으로 올바른 것은 무엇인가요?",
        "options": [
            "전류는 전압에 반비례하고 저항에 비례한다.",
            "전압은 전류와 저항의 곱과 같다.",
            "저항은 전압과 전류에 비례한다.",
            "전류의 단위는 볼트(V)이다."
        ],
        "answer": "전압은 전류와 저항의 곱과 같다.",
        "explanation": "옴의 법칙은 V = I x R 입니다. 즉, 전압(V)은 전류(I)와 저항(R)을 곱한 값과 같습니다. 따라서 전류(I)는 전압(V)에 비례하고 저항(R)에 반비례합니다."
    },
    {
        "type": "multiple_choice",
        "question": "2. 다음 중 자동차의 '전기 장치'에 속하지 **않는** 것은 무엇인가요?",
        "options": [
            "시동 모터 (Starting Motor)",
            "발전기 (Alternator)",
            "브레이크 (Brake)",
            "전조등 (Headlight)"
        ],
        "answer": "브레이크 (Brake)",
        "explanation": "브레이크는 자동차를 멈추게 하는 제동 장치로, '섀시(Chassis)' 장치에 속합니다. 시동 모터, 발전기, 전조등은 모두 전기를 사용하는 핵심 전기 장치입니다."
    },
    {
        "type": "multiple_choice",
        "question": "3. 자동차 엔진이 작동하는 동안 전기를 생산하여 배터리를 충전하는 역할을 하는 장치는 무엇인가요?",
        "options": [
            "점화 플러그",
            "시동 모터",
            "발전기",
            "연료 펌프"
        ],
        "answer": "발전기",
        "explanation": "발전기(알터네이터)는 엔진의 회전력을 이용하여 전기를 만들어내고, 이 전기로 배터리를 충전하며 다른 전기 장치에도 전원을 공급합니다."
    },
    {
        "type": "multiple_choice",
        "question": "4. 다음 중 자동차의 동력을 발생시키는 '기관(엔진) 장치'의 핵심 부품은 무엇인가요?",
        "options": [
            "조향 장치 (Steering System)",
            "현가 장치 (Suspension System)",
            "점화 플러그 (Spark Plug)",
            "라디에이터 그릴 (Radiator Grille)"
        ],
        "answer": "점화 플러그 (Spark Plug)",
        "explanation": "점화 플러그는 엔진 연소실에서 연료와 공기의 혼합기에 불꽃을 일으켜 폭발시켜 동력을 얻는 핵심 '기관' 부품입니다. 조향 장치와 현가 장치는 '섀시'에 속합니다."
    },
    {
        "type": "multiple_choice",
        "question": "5. 전기의 흐름인 '전류'에 대한 설명으로 틀린 것은 무엇인가요?",
        "options": [
            "단위는 암페어(A)를 사용한다.",
            "전자의 이동 방향과 반대 방향으로 흐른다고 약속했다.",
            "전류를 흐르게 하는 힘을 '저항'이라고 한다.",
            "전류가 흐르면 빛이나 열이 발생할 수 있다."
        ],
        "answer": "전류를 흐르게 하는 힘을 '저항'이라고 한다.",
        "explanation": "전류를 흐르게 하는 힘(전기적 압력)은 '전압'입니다. '저항'은 오히려 전류의 흐름을 방해하는 요소입니다."
    },
    {
        "type": "short_answer",
        "question": "6. 전압, 전류, 저항의 관계를 나타내는 법칙의 이름은 무엇인가요? (OOO 법칙)",
        "answer": "옴의 법칙",
        "explanation": "전압(V), 전류(I), 저항(R) 사이의 관계 V=IR을 '옴의 법칙'이라고 합니다."
    },
    {
        "type": "short_answer",
        "question": "7. 자동차의 엔진을 처음 가동시키기 위해 배터리의 전기를 이용해 강력한 회전력을 만들어주는 전기 장치의 이름은 무엇인가요? (OO OO)",
        "answer": "시동 모터",
        "explanation": "'시동 모터' 또는 '시동 전동기'는 엔진을 맨 처음 돌려주는 중요한 전기 장치입니다."
    }
]


# --- 각 페이지 구현 ---

# 1. 홈 페이지
if menu == '홈':
    st.title('자동차 전기전자제어 학습 도우미')
    st.divider() # 구분선
    st.subheader('1단원: 자동차 전기전자 개요를 인터랙티브하게 학습해 보세요.')
    
    st.write("""
    이 앱은 '자동차 전기전자제어' 교과의 첫 단원인 **'자동차 전기전자 개요'**의 내용을 학습하는 데 도움을 주기 위해 만들어졌습니다.  
    왼쪽 사이드바에서 원하는 학습 메뉴를 선택하여 진행해 주세요.
    """)
    
    st.info("##### 📖 개념 학습\n전기, 전류, 전압 등 기초 개념을 시각 자료와 함께 배워봅니다.", icon="ℹ️")
    st.info("##### ✍️ 개념 확인 퀴즈\n객관식 퀴즈를 풀며 학습한 내용을 점검해 보세요.", icon="ℹ️")
    st.info("##### 🔍 전기 장치 찾아보기\n실제 자동차 사진을 보고 전기 장치의 종류와 명칭을 맞춰봅니다.", icon="ℹ️")


# 2. 개념 학습 페이지
elif menu == '개념 학습':
    st.title('📖 개념 학습: 자동차 전기전자 개요')
    st.divider()

    # 탭을 사용하여 콘텐츠 구성
    tab1, tab2, tab3 = st.tabs(["⚡ 전기와 전류의 기초", "💡 옴의 법칙 (V=IR)", "🚗 자동차 전기 장치"])

    with tab1:
        st.subheader("1. 전기(Electricity)와 전류(Current)")
        st.write(
            """
            전기는 우리 생활과 자동차에 없어서는 안 될 중요한 에너지입니다. 
            모든 물질은 **원자**로 이루어져 있고, 원자는 원자핵(+)과 그 주위를 도는 **전자(-)**로 구성됩니다.
            
            **전기**란 바로 이 '전자'가 이동하면서 발생하는 에너지 현상을 의미합니다.
            """
        )
        # 이미지 URL을 웹에서 직접 접근 가능한 주소로 변경했습니다.
        st.image("https://i.imgur.com/8Qk5W6B.png", caption="[그림 1] 원자의 구조", width=400)
        
        st.markdown(
            """
            ---
            #### 전류: 전기의 흐름
            **전류**는 물이 높은 곳에서 낮은 곳으로 흐르는 것처럼, 전하(전자)가 한 방향으로 이동하는 흐름을 말합니다.
            - **전류의 방향:** 전자가 이동하는 방향과 **반대** 방향 (양극(+) → 음극(-))
            - **단위:** **A (암페어)**
            
            회로에 전구와 같은 부하(일을 하는 장치)가 연결되어 있으면, 전류가 흐르면서 빛이나 열을 발생시킵니다.
            """
        )
        st.image("https://i.imgur.com/rN5wD5k.png", caption="[그림 2] 전류와 전자의 이동 방향")

        st.markdown("---") # 구분선 추가

        # --- 잠깐 퀴즈 섹션 추가 ---
        st.subheader("🧐 잠깐 퀴즈!")
        st.write("일상생활의 예시를 통해 교류와 직류를 구분해 봅시다.")

        question = st.radio(
            "**Q. 우리가 가정에서 사용하는 콘센트의 전기와 자동차에서 사용하는 배터리 전기는 각각 무엇일까요?**",
            ('둘 다 직류(DC)입니다.', 
             '둘 다 교류(AC)입니다.', 
             '가정용은 교류(AC), 자동차용은 직류(DC)입니다.', 
             '가정용은 직류(DC), 자동차용은 교류(AC)입니다.'),
            index=None, # 사용자가 선택하기 전까지 아무것도 선택되지 않도록 설정
        )

        if st.button('정답 확인'):
            if question == '가정용은 교류(AC), 자동차용은 직류(DC)입니다.':
                st.success('정답입니다! 짝짝짝 👏')
                st.info(
                    """
                    **해설:**
                    - **가정용 전기(교류, AC):** 발전소에서 만들어진 전기는 먼 거리를 효율적으로 보내기 위해 교류 형태를 사용합니다.
                    - **자동차 배터리(직류, DC):** 배터리는 화학 에너지를 전기 에너지로 저장하는데, 이때는 한 방향으로만 흐르는 직류 형태를 띕니다.
                    """
                )
            elif question is None:
                st.warning("답을 선택해주세요!")
            else:
                st.error('아쉽지만 틀렸어요. 다시 한번 생각해 보세요! 🤔')
        # --- 퀴즈 섹션 끝 ---

    with tab2:
        st.subheader("2. 전압, 전류, 저항의 관계: 옴의 법칙")
        st.write(
            """
            전기 회로에서는 전압, 전류, 저항 세 가지 요소가 서로 밀접한 관계를 맺고 있습니다. 이 관계를 설명하는 것이 바로 **옴의 법칙**입니다.
            - **전압(V):** 전류를 흐르게 하는 힘 (전기적인 압력). 단위는 **V(볼트)**.
            - **전류(I):** 전하의 흐름. 단위는 **A(암페어)**.
            - **저항(R):** 전류의 흐름을 방해하는 정도. 단위는 **Ω(옴)**.
            """
        )
        
        st.image("https://i.imgur.com/xLKj32b.png", caption="[그림 3] 옴의 법칙 (E는 전압 V와 같음)")

        st.success(
            """
            **"회로에 흐르는 전류(I)는 전압(V)에 비례하고, 저항(R)에 반비례한다."**
            #### $I = V / R$
            """
        )
        
        st.markdown("---")
        
        st.subheader("🔢 옴의 법칙 계산기")
        st.write("슬라이더를 조절하여 전압과 저항의 변화에 따른 전류의 변화를 직접 확인해보세요.")
        
        col1, col2 = st.columns(2)
        with col1:
            voltage = st.slider('전압 (V) 선택', 1, 24, 12, 1)
        with col2:
            resistance = st.slider('저항 (R) 선택', 1, 100, 10, 1)

        if resistance > 0:
            current = voltage / resistance
            st.metric(label="계산된 전류 (I)", value=f"{current:.2f} A")
        else:
            st.error("저항은 0보다 커야 합니다.")


    with tab3:
        st.subheader("3. 자동차의 주요 전기 장치")
        st.write("자동차에는 다양한 전기 장치들이 있으며, 크게 다음과 같이 분류할 수 있습니다.")

        col1, col2 = st.columns(2)
        with col1:
            st.info("#### 시동 장치 (Starting System)")
            st.write("엔진을 처음 가동시키기 위해 크랭크축에 회전력을 공급하는 장치입니다. (예: 시동 모터)")
            st.image("https://i.imgur.com/w2Yg0oT.png", caption="시동 모터")

            st.info("#### 등화 장치 (Lighting System)")
            st.write("야간 주행 시 시야를 확보하고, 다른 차에게 신호를 보내는 장치입니다. (예: 전조등, 방향지시등)")
            st.image("https://i.imgur.com/pYvj7B5.png", caption="전조등")
        
        with col2:
            st.info("#### 충전 장치 (Charging System)")
            st.write("엔진이 작동하는 동안 전기를 생산하여 배터리를 충전하고, 각 부품에 전원을 공급하는 장치입니다. (예: 발전기)")
            st.image("https://i.imgur.com/X2d2aZk.png", caption="발전기 (알터네이터)")

            st.info("#### 점화 장치 (Ignition System)")
            st.write("가솔린 엔진의 연소실 내 압축된 혼합기에 전기 불꽃을 일으켜 점화하는 장치입니다. (예: 점화 코일, 점화 플러그)")
            st.image("https://i.imgur.com/Xl9k7aQ.png", caption="점화 플러그")


# 3. 개념 확인 퀴즈 페이지 (구현)
elif menu == '개념 확인 퀴즈':
    st.title('✍️ 개념 확인 퀴즈')
    st.divider()

    # 퀴즈가 모두 끝났을 때
    if st.session_state.current_question >= len(quiz_data):
        st.success(f"🎉 모든 퀴즈를 완료했습니다! 당신의 점수는: {st.session_state.score} / {len(quiz_data)}")
        st.balloons()
        if st.button("다시 풀기"):
            # 세션 상태 초기화
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.rerun() # 페이지를 새로고침하여 퀴즈를 다시 시작
    else:
        # 현재 문제 가져오기
        question_data = quiz_data[st.session_state.current_question]
        
        st.subheader(f"문제 {st.session_state.current_question + 1} / {len(quiz_data)}")
        
        user_answer = None
        # 문제 유형에 따라 입력 방식 변경
        if question_data["type"] == "multiple_choice":
            user_answer = st.radio(
                question_data["question"],
                question_data["options"],
                index=None
            )
        elif question_data["type"] == "short_answer":
            user_answer = st.text_input(
                question_data["question"],
                placeholder="정답을 입력하세요."
            )

        # 제출 버튼
        if st.button("제출하기"):
            correct_answer = question_data["answer"]
            
            # 주관식 문제의 경우, 공백을 제거하고 비교
            is_correct = False
            if question_data["type"] == "short_answer" and user_answer:
                is_correct = user_answer.strip() == correct_answer
            else:
                is_correct = user_answer == correct_answer

            if is_correct:
                st.success("정답입니다! 👍")
                st.info(f"**해설:** {question_data['explanation']}")
                st.session_state.score += 1
                
                # 다음 문제로 넘어가기 위한 버튼
                if st.button("다음 문제로 이동"):
                    st.session_state.current_question += 1
                    st.rerun() # 페이지를 새로고침하여 다음 문제를 표시
            
            elif user_answer is None or user_answer == "":
                 st.warning("답을 입력하거나 선택해주세요.")
            else:
                st.error("오답입니다. 다시 한번 생각해 보세요. 💡")


# 4. 전기 장치 찾아보기 페이지 (뼈대)
elif menu == '전기 장치 찾아보기':
    st.title('🔍 전기 장치 찾아보기')
    st.write("이곳에서 자동차 사진을 보고 전기 장치를 찾아봅니다.")
    # (추후 4단계에서 내용 구현 예정)

