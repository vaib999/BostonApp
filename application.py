import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

application = app = Flask(__name__)

def create_app():
    model = pickle.load(open('model.pkl', 'rb'))

    @application.route('/')
    def home():
        return render_template('index.html')

    @application.route('/predict',methods=['POST'])
    def predict():
        '''
        For rendering results on HTML GUI
        '''
        int_features = [float(x) for x in request.form.values()]
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)

        output = prediction[0]

        return render_template('index.html', prediction_text='Price of house $ {}'.format(output))

    return application

my_app = create_app()
# my_app.run(host='0.0.0.0', port=8080)