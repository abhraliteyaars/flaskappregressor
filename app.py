from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio.input import *
from pywebio.output import *
import argparse
from pywebio import start_server
from flask import Flask, send_from_directory
import pandas as pd

import pickle
import numpy as np
model = pickle.load(open('model.pkl', 'rb'))
app = Flask(__name__)


def predict():
    Visits=input("Visits",type=NUMBER)
    Pageviews=input("Pageviews",type=NUMBER)
    Bounce=input("BounceRate",type=FLOAT)
    prediction = model.predict([[Visits,Pageviews,Bounce]])
    output=prediction[0]
    put_text(output)
    data = [[Visits, Pageviews, BounceRate, output]]
    df = pd.DataFrame(data, columns = ['Visits', 'Pageviews', 'BounceRate','Output'])
    df.to_csv('data2.csv', index=False)
    
    
from pywebio.platform.flask import webio_view
app.add_url_rule('/', 'webio_view', webio_view(predict),
            methods=['GET', 'POST', 'OPTIONS'])



@app.route('/')
def refresh():
    return webio_view(predict)

app.add_url_rule('/', 'refresh', refresh)


app.run()