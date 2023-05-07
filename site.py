# CS484: Layoff Prediction App
import flask
import pickle
import sklearn
import pandas as pd
import numpy as np

app = flask.Flask(__name__)


# Load model and scaler from disk
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

# Column names, in order:
column_names = ['funds_raised', 'industry_Aerospace', 'industry_Construction',                                                                    'industry_Consumer', 'industry_Crypto', 'industry_Data',                                                                    'industry_Education', 'industry_Energy', 'industry_Finance',                                                                'industry_Fitness', 'industry_Food', 'industry_HR', 'industry_Hardware',                                                    'industry_Healthcare', 'industry_Infrastructure', 'industry_Legal',                                                         'industry_Logistics', 'industry_Manufacturing', 'industry_Marketing',                                                       'industry_Media', 'industry_Other', 'industry_Product',                                                                     'industry_Real Estate', 'industry_Recruiting', 'industry_Retail',                                                           'industry_Sales', 'industry_Security', 'industry_Support',                                                                  'industry_Transportation', 'industry_Travel', 'stage_Acquired',                                                             'stage_Post-IPO', 'stage_Private Equity', 'stage_Seed',                                                                     'stage_Series A', 'stage_Series B', 'stage_Series C', 'stage_Series D',                                                     'stage_Series E', 'stage_Series F', 'stage_Series G', 'stage_Series H',                                                     'stage_Series I', 'stage_Series J', 'stage_Subsidiary',                                                                     'stage_Unknown']

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = flask.request.form

    # Massage data to fit in the categorical columns;
    # industry and stage are the only categorical columns
    # we need to worry about.
    
    if 'industry_' + data['industry'] not in column_names:
        # Bad request
        return flask.make_response('Invalid industry', 400)
    if 'stage_' + data['stage'] not in column_names:
        # Bad request
        return flask.make_response('Invalid stage', 400)

    # Create a new row of data to predict on
    new_row = pd.DataFrame(columns=column_names)
    new_row.loc[0] = 0
    new_row['funds_raised'] = data['funds_raised']
    new_row['industry_' + data['industry']] = 1
    new_row['stage_' + data['stage']] = 1

    # Scale and predict
    new_row = scaler.transform(new_row)
    prediction = model.predict(new_row)

    # Convert prediction to string
    thresholds = [0.17, 0.25, 0.37]
    risks = ['low', 'medium', 'high', 'very high']
    prediction = risks[int(np.digitize(prediction, thresholds))]

    # Render the template with the prediction
    return flask.render_template('index.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)
