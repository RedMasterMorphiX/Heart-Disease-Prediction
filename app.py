import streamlit as st
import pickle
import numpy as np

age_m = 53.333333333333333
age_std = 9.229016
trestbps_m = 128.671053
trestbps_std = 15.349142
chol_m = 242.372807
chol_std = 44.329827
thalach_m = 151.070175
thalach_std = 22.492963
oldpeak_m = 0.946053
oldpeak_std = 1.035422
def load_model():
    # Load your trained machine learning model
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

def main():
    st.title('Are You Having Heart Disease!!! Dont Fear, Check Here')

    name = st.text_input('What is your name?')
    age = st.number_input("Enter age")
    age = (age - age_m) / age_std
    trestbps = st.number_input("Enter Resting blood pressure")
    trestbps = (trestbps - trestbps_m) / trestbps_std
    chol = st.number_input("Enter Cholestrol")
    chol = (chol - chol_m) / chol_std
    thalach = st.number_input("Enter Maximum heart rate achieved")
    thalach = (thalach - thalach_m) / thalach_std
    oldpeak = st.number_input("Enter ST depression induced by exercise relative to rest, example- 1.1,1.2,1.3...")
    oldpeak = (oldpeak - oldpeak_m) / oldpeak_std

    sex = st.selectbox("Select gender:", options=['Male', 'Female'])
    if sex == 'Male':
        sex_0 = False
        sex_1 = True
    else:
        sex_0 = True
        sex_1 = False

    cp = st.selectbox("Select Constrictive pericarditis:", options=[0, 1, 2, 3])
    if cp == 0:
        cp_0 = True
        cp_1 = False
        cp_2 = False
        cp_3 = False
    elif cp == 1:
        cp_0 = False
        cp_1 = True
        cp_2 = False
        cp_3 = False
    elif cp == 2:
        cp_0 = False
        cp_1 = False
        cp_2 = True
        cp_3 = False
    else:
        cp_0 = False
        cp_1 = False
        cp_2 = False
        cp_3 = True

    fbs_0 = st.selectbox("Select Fasting blood sugar:", options=[0])

    restecg = st.selectbox("Select Resting electrocardiographic measurement:", options=[0, 1, 2])
    if restecg == 0:
        restecg_0 = True
        restecg_1 = False
        restecg_2 = False
    elif restecg == 1:
        restecg_0 = False
        restecg_1 = True
        restecg_2 = False
    else:
        restecg_0 = False
        restecg_1 = False
        restecg_2 = True

    exang = st.selectbox("Select Resting electrocardiographic:", options=[0, 1])
    if exang == 0:
        exang_0 = True
        exang_1 = False
    else:
        exang_0 = False
        exang_1 = True

    slope = st.selectbox("Select The ST segment shift:", options=[0, 1, 2])
    if slope == 0:
        slope_0 = True
        slope_1 = False
        slope_2 = False
    elif slope == 1:
        slope_0 = False
        slope_1 = True
        slope_2 = False
    else:
        slope_0 = False
        slope_1 = False
        slope_2 = True

    ca = st.selectbox("Select Calcium:", options=[0, 1, 2])
    if ca == 0:
        ca_0 = True
        ca_1 = False
        ca_2 = False
    elif ca == 1:
        ca_0 = False
        ca_1 = True
        ca_2 = False
    else:
        ca_0 = False
        ca_1 = False
        ca_2 = True

    thal = st.selectbox("Select Thalasemia", options=[1, 2, 3])
    if thal == 1:
        thal_1 = True
        thal_2 = False
        thal_3 = False
    elif thal == 1:
        thal_1 = False
        thal_2 = True
        thal_3 = False
    else:
        thal_1 = False
        thal_2 = False
        thal_3 = True

    # Load the model
    model = load_model()

    input_values = [
        age, trestbps, chol, thalach, oldpeak,
        sex_0, sex_1, cp_0, cp_1, cp_2, cp_3,
        fbs_0, restecg_0, restecg_1, restecg_2,
        exang_0, exang_1, slope_0, slope_1, slope_2,
        ca_0, ca_1, ca_2, thal_1, thal_2, thal_3
    ]

    input_array = np.array(input_values).reshape(1, -1)

    # Make predictions
    prediction = model.predict(input_array)

    st.write('Hey ', name, end=" ")
    if prediction==1:
        st.write('You are having heart disease')
    else:
        st.write('You are not having heart disease')

if __name__ == '__main__':
    main()
