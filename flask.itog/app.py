import flask
from flask import render_template  # взаимодействие с html
import pickle # pickle-mixin
# import gunicorn
import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import tensorflow as tf


# приложение flask и каталог шаблонов
# flask app and templates folder
app = flask.Flask(__name__, template_folder='templates')

# декоратор для страницы и методы
# page decorator and methods
@app.route('/', methods=['POST', 'GET'])

@app.route('/index', methods=['POST', 'GET'])
def main():
    # если метод GET просто отдаем страничку
    # if method GET simply return main page
    if flask.request.method == 'GET':
        return render_template('main.html')

    # если метод POST, тогда делаем обработчик
    # if method POST, then process data
    if flask.request.method == 'POST':
        # загружаем scaler
        # loading StandartScaler
        with open('./fitted_models/scaler.pkl', 'rb') as f:
            scaler = pickle.load(f)

        # загружаем сохраненную линейную модель
        # loading presaved LinearRegression model
        with open('./fitted_models/linear_model.pkl', 'rb') as f:
            linear_model = pickle.load(f)

        # получаем параметры с веб формы
        # getting parameters from web page input
        param_iw = float(flask.request.form['param_iw'])
        param_if = float(flask.request.form['param_if'])
        param_vw = float(flask.request.form['param_vw'])
        param_fp = float(flask.request.form['param_fp'])

        # собираем параметры в массив
        # collection parameter to numpy array
        X = np.array([[param_iw, param_if, param_vw, param_fp]])

        # масштабируем полученные параметры
        # scaling parameters
        X = scaler.transform(X)

        # прогнозируемый размер сварного шва
        # predicting weld width and depth
        y_pred = linear_model.predict(X)
        
        result = []
        result.append('Прогноз модели линейной регрессии')
        result.append(f'Глубина (Depth): {y_pred[0][0]:.2f};  Ширина (Width): {y_pred[0][1]:.2f}')

        # загружаем сохраненную модель keras
        # loading presaved keras model
        nn_model = tf.keras.models.load_model('./fitted_models/nn_model')

        y_pred = nn_model.predict(X)

        result.append('Прогноз предобученной нейронной сети')
        result.append(f'Глубина (Depth): {y_pred[0][0]:.2f};  Ширина (Width): {y_pred[0][1]:.2f}')

        
        # загружаем сохраненную модель случайного леса
        # loading RandomForestRegressor model
        with open('./fitted_models/forest_model.pkl', 'rb') as f:
            forest_model = pickle.load(f)
         
        y_pred = forest_model.predict(X)

        result.append('Прогноз модели Random Forest Regressor')
        result.append(f'Глубина (Depth): {y_pred[0][0]:.2f};  Ширина (Width): {y_pred[0][1]:.2f}')

        return render_template('main.html', result=result)

if __name__=='__main__':
    app.run()