from flask import Flask, render_template
import os
import jinja2
app = Flask(__name__)
# connects default URL to a function
@app.route('/')
def home():
    # Flask import uses Jinga to render HTML
    return render_template("home.html")

@app.route('/centralpark')
def centralpark():
    return render_template("centralpark.html")


# connects to journals page
@app.route('/madisonsquare')
def madisonsquare():
    return render_template("madisonsquare.html")
if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True, port='5000', host='127.0.0.1')