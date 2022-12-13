import streamlit as st
import numpy as np
import pandas as pd
import joblib

def run_ml_app():
    # 성별은 여자이고, 나이는 50이며, 연봉은 4만달러, 카드 빛 5만달라,자신 20만
    # 성별,나이,연봉,카드빚,자신을 유저한테 모두 입력받아서
    # 자동차 금액을 예측하세요.


    
    gender=st.radio('성별 선택',['여자','남자'])
    if gender == '여자':
        gender =0
    else:
        gender=1

    age=st.number_input("나이를 입력하세요",20,100)
    salary=st.number_input("연봉을 입력하세요",20000,100000)
    debt=st.number_input("카드 빚을 입력하세요",100,20000)
    worth=st.number_input("자산을 입력하세요",9000,80000)

    new_data=np.array([gender,age,salary,debt,worth])
    
    new_data=new_data.reshape(1,5)
    
    regressor = joblib.load('regressor.pkl')

    y_pred2=regressor.predict(new_data)

    y_pred2=round(y_pred2[0],1)
    
    if y_pred2>1000:
        st.info('예측한 자동차금액은{}달러입니다.'.format(y_pred2))

    else:
        st.info('입력한 데이터로는 금액을 예측하기 어렵습니다.')
    
    