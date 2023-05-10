import pickle

import numpy as np

from flask import render_template, redirect, url_for, request
from flask import Flask

app = Flask(__name__)

SVM= pickle.load(open('C:/Users/Yassine/PycharmProjects/pythonProject/modele.pkl', 'rb'))


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        x1 = int(request.form['LIMIT_BAL'])
        x2 = int(request.form['SEX'])
        x3 = int(request.form['EDU_TYPE_1'])
        x4 = int(request.form['EDU_TYPE_2'])
        x5 = int(request.form['EDU_TYPE_3'])
        x6 = int(request.form['EDU_TYPE_4'])
        x7 = int(request.form['Mar_TYPE_1'])
        x8 = int(request.form['Mar_TYPE_2'])
        x9 = int(request.form['Mar_TYPE_3'])
        x10 = int(request.form['Mar_TYPE_4'])
        x11 = int(request.form['AGE'])
        x12 = int(request.form['PAY_1'])
        x13 = int(request.form['PAY_2'])
        x14 = int(request.form['PAY_3'])
        x15 = int(request.form['PAY_4'])
        x16 = int(request.form['PAY_5'])
        x17 = int(request.form['PAY_6'])
        x18 = int(request.form['BILL_AMT1'])
        x19 = int(request.form['BILL_AMT2'])
        x20 = int(request.form['BILL_AMT3'])
        x21 = int(request.form['BILL_AMT4'])
        x22 = int(request.form['BILL_AMT5'])
        x23 = int(request.form['BILL_AMT6'])
        x24 = int(request.form['PAY_AMT1'])
        x25 = int(request.form['PAY_AMT2'])
        x26 = int(request.form['PAY_AMT3'])
        x27 = int(request.form['PAY_AMT4'])
        x28 = int(request.form['PAY_AMT5'])
        x29 = int(request.form['PAY_AMT6'])


        data = np.array([[ x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28 ,x29]])
    return render_template('result.html', prediction=SVM.predict(data))


if __name__== "__main__":
    app.run(host='localhost', port=5000)