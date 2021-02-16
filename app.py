from flask import Flask, render_template
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('bootstrap.html')


@app.route('/predict')
def index2():
    prediction_value = predict_f()
    # if news is None:
    #     print('taken1', news)
    # else:
    #     print('noa',news)
    return render_template('bootstrap_with_prediction.html', prediction= f'Expected variation in NIFTY50 stock exchange would be: {prediction_value}' )

# check
def predict_f():
    if int(np.random.random()*10)%2 ==0:
        num = - round(np.random.random()*1000,2)
        return (num)
    else:
        num = round(np.random.random()*1000,2)
        return (num)

if __name__ == '__main__':
 app.run()