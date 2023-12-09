import os
import streamlit as st
import bardapi.core

# Bard API 키 설정
os.environ['_BARD_API_KEY'] = "eAh1cm4gKu5R3BodgC-5dp-pJIkGRtDZnZzGGm3fV4ugp7Mr8ftXCzFs-paxGG21x_4Ycg."
# Chat 모델 설정
chat_model = bardapi.core.Bard()

st.title('인공지능 여행 계획')

# 입력 값
content = st.text_input('지역을 입력해주세요')

# 버튼
if st.button('계획 작성 요청하기'): 
    # 로딩
    with st.spinner('여행 계획 작성중'):
        # Chat 모델 사용
        result = chat_model.get_answer(content + "에 대해서 여행계획을 짜줘")
        
        # 이미지 주석 처리
        text_content = result['content'].replace("[Image of", "").replace("]", "").strip()
        
        # 텍스트 출력
        st.text(f"인공지능: {text_content}")
