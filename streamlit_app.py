import streamlit as st

# --- 페이지 설정 ---
# st.set_page_config(layout="wide") # 넓은 레이아웃을 원할 경우 주석 해제

# --- 사이드바 메뉴 ---
with st.sidebar:
    st.title('🚗 학습 메뉴')
    menu = st.radio(
        "메뉴를 선택하세요.",
        ('홈', '개념 학습', '개념 확인 퀴즈', '전기 장치 찾아보기'),
        label_visibility="collapsed"
    )

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


# 2. 개념 학습 페이지 (구현)
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
        
        st.image("https://storage.googleapis.com/gweb-aip-demos/proxima/car-app/atom.png", caption="[그림 1] 원자의 구조", width=400)
        
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
        st.image("https://storage.googleapis.com/gweb-aip-demos/proxima/car-app/circuit.png", caption="[그림 2] 전류와 전자의 이동 방향")

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
        
        st.image("https://storage.googleapis.com/gweb-aip-demos/proxima/car-app/ohms_law.png", caption="[그림 3] 옴의 법칙 (E는 전압 V와 같음)")

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
            st.image("https://storage.googleapis.com/gweb-aip-demos/proxima/car-app/starter_motor.png", caption="시동 모터")

            st.info("#### 등화 장치 (Lighting System)")
            st.write("야간 주행 시 시야를 확보하고, 다른 차에게 신호를 보내는 장치입니다. (예: 전조등, 방향지시등)")
            st.image("https://storage.googleapis.com/gweb-aip-demos/proxima/car-app/headlight.png", caption="전조등")
        
        with col2:
            st.info("#### 충전 장치 (Charging System)")
            st.write("엔진이 작동하는 동안 전기를 생산하여 배터리를 충전하고, 각 부품에 전원을 공급하는 장치입니다. (예: 발전기)")
            st.image("https://storage.googleapis.com/gweb-aip-demos/proxima/car-app/alternator.png", caption="발전기 (알터네이터)")

            st.info("#### 점화 장치 (Ignition System)")
            st.write("가솔린 엔진의 연소실 내 압축된 혼합기에 전기 불꽃을 일으켜 점화하는 장치입니다. (예: 점화 코일, 점화 플러그)")
            st.image("https://storage.googleapis.com/gweb-aip-demos/proxima/car-app/spark_plug.png", caption="점화 플러그")


# 3. 개념 확인 퀴즈 페이지 (뼈대)
elif menu == '개념 확인 퀴즈':
    st.title('✍️ 개념 확인 퀴즈')
    st.write("이곳에서 학습한 내용을 퀴즈로 확인합니다.")
    # (추후 3단계에서 내용 구현 예정)


# 4. 전기 장치 찾아보기 페이지 (뼈대)
elif menu == '전기 장치 찾아보기':
    st.title('🔍 전기 장치 찾아보기')
    st.write("이곳에서 자동차 사진을 보고 전기 장치를 찾아봅니다.")
    # (추후 4단계에서 내용 구현 예정)

