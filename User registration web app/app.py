from flask import Flask, url_for, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    state = db.Column(db.String(100))
    county = db.Column(db.String(100))
    q1 = db.Column(db.String(100))
    q2 = db.Column(db.String(100))
    q3 = db.Column(db.String(100))

    def __init__(self, username, email, state, county, q1, q2, q3):
        self.username = username
        self.email = email
        self.state = state
        self.county = county
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        forecasts_df = pd.read_csv('tomorrows_forecast.csv')
        unique_states = list(sorted(forecasts_df['state_name'].unique()))
        unique_counties = list(sorted(forecasts_df['county_name'].unique()))
        return render_template("base.html", 
                                message="Welcome to our app! \n Please register for daily weather/safety updates over email.",
                                states=unique_states,
                                counties=unique_counties,
                                options=['Yes', 'No'])
        #return render_template('register.html', message="Welcome to our app! Please register for daily weather/safety updates over email.")

@app.route('/register/', methods=['GET', 'POST'])
def register():
    db.session.add(User(username=request.form['username'], 
                        email=request.form['email'], 
                        state=request.form['state'],
                        county=request.form['county'],
                        q1=request.form['q1'],
                        q2=request.form['q2'],
                        q3=request.form['q3'],))
    db.session.commit()
    #return render_template('register.html', message="You have successfully registered!")
    forecasts_df = pd.read_csv('tomorrows_forecast.csv')
    unique_states = list(sorted(forecasts_df['state_name'].unique()))
    unique_counties = list(sorted(forecasts_df['county_name'].unique()))
    return render_template("base.html", 
                            message="You have successfully registered!",
                            states=unique_states,
                            counties=unique_counties,
                            options=['Yes', 'No'])

if __name__ == '__main__':
    app.secret_key = "ThisIsNotASecret:p"
    db.create_all()
    # Alternate idea: group by state and county to get unique state-county combinations, and display those as 
    # options in the dropdown
    app.run()