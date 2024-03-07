from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

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
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

model = load_model()

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        name = request.form['name']
        age = (float(request.form['age']) - age_m) / age_std
        trestbps = (float(request.form['trestbps']) - trestbps_m) / trestbps_std
        chol = (float(request.form['chol']) - chol_m) / chol_std
        thalach = (float(request.form['thalach']) - thalach_m) / thalach_std
        oldpeak = (float(request.form['oldpeak']) - oldpeak_m) / oldpeak_std
        sex = request.form['sex']
        cp = int(request.form['cp'])
        fbs_0 = int(request.form['fbs'])
        restecg = int(request.form['restecg'])
        exang = int(request.form['exang'])
        slope = int(request.form['slope'])
        ca = int(request.form['ca'])
        thal = int(request.form['thal'])

        
        if sex == 1:
            sex_0 = False
            sex_1 = True
        else:
            sex_0 = True
            sex_1 = False

    
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

    
        if exang == 0:
            exang_0 = True
            exang_1 = False
        else:
            exang_0 = False
            exang_1 = True

    
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

    

        input_features = [
            age, trestbps, chol, thalach, oldpeak,
            sex_0, sex_1, cp_0, cp_1, cp_2, cp_3,
            fbs_0, restecg_0, restecg_1, restecg_2,
            exang_0, exang_1, slope_0, slope_1, slope_2,
            ca_0, ca_1, ca_2, thal_1, thal_2, thal_3
        ]

        input_array = np.array(input_features).reshape(1, -1)
        prediction = model.predict(input_array)

        return render_template('result.html', name=name, prediction=int(prediction[0]))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)