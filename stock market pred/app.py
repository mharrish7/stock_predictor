import imp
from flask import Flask,request,render_template,jsonify
import joblib
import requests
app = Flask(__name__)

model = joblib.load('stock_model')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/pred",methods = ['POST'])
def predict():
    try:
        r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&outputsize=compact&apikey=11YDSTQBB9OV29FI')
        r = r.json()
        r = r['Time Series (Daily)']
        for i in r:
            date = i
            dat = r[i]
            break
        L = []
        for i in dat:
            L.append(float(dat[i]))
        pred = model.predict([L])

        if pred[0] == 1:
            return jsonify({'data':'Up','d':1,'date' : date})
        else:
            return jsonify({'data':'Down','d':0})
    except:
        return jsonify({'data':'error'})

if __name__ == "__main__":
    app.run(debug=True)
