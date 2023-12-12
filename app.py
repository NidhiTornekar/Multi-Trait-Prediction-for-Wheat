from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load('random_forest_model_means.joblib')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    sequence = request.form['sequence']
    new_data = {'Allele_Sequence': [sequence]}
    new_df = pd.DataFrame(new_data)
    prediction = model.predict(new_df)
    return render_template('predict.html', sequence=sequence, prediction=prediction)

# for deployment
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# use this for running in local system 
#if __name__ == '__main__':
#    app.run()
