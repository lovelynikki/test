
from flask import *
import json,os
import pandas as pd

app = Flask(__name__)

html_file1 = """<style>table{
    border-collapse: collapse;
      margin: 20px 0;
      font-size: 0.9em;
      font-family: sans-serif;
      box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
  }
  thead tr {
      background-color: #009879;
      color: #ffffff;
      text-align: left;
  }
  th, td {
      padding: 25px 15px;
  }
  th {
      text-align: center;
      font-size: 1.3em;
  }
  
  tbody tr {
      border-bottom: 1px solid #000000;
  }
  tbody tr:nth-of-type(even) {
      background-color: #c1eee5;
  }
  tbody tr:last-of-type {
      border-bottom: 2px solid #009879;
  }
  tbody tr.active-row {
      font-weight: bold;
      color: #009879;
  }
        button {
    background-color: #009879; /* Green */
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    }</style>"""

html2_file = """<button><a href="/" >Back</a></button> &emsp; &emsp; &emsp;"""

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/favicon.png')

@app.route('/',methods=['GET'])
def home_page():
    return render_template('main.html')


@app.route('/news/',methods=['GET'])
def news_page():
    return render_template('index.html')

@app.route('/java/',methods=['GET'])
def vaccine_page():
    csv_file = pd.read_csv("https://docs.google.com/spreadsheets/d/1fKkj4LwR5cbifcverlOLQ4V8CizSAFanJ6MCtyZzOTc/export?format=csv&gid=1324241192")
    html_file = csv_file.to_html()
    #print(html_file1+html_file+html2_file)
    return html_file1+html_file+html2_file

@app.route('/python/',methods=['GET'])
def python_page():
    csv_file = pd.read_csv("https://docs.google.com/spreadsheets/d/1sJWXHRINXwi-pOFHts4kRXsouWTgP9yVWOIApCjf6ak/export?format=csv&gid=0")
    html_file = csv_file.to_html()
    
    return html_file1+html_file+html2_file

@app.route('/sql/',methods=['GET'])
def sql_page():
    csv_file = pd.read_csv("https://docs.google.com/spreadsheets/d/1hLkp6jV-5eAQ1F8wha77SMa57em4jscOhDDgqYXNJFY/export?format=csv&gid=0")
    html_file = csv_file.to_html()
    
    return html_file1+html_file+html2_file



if __name__ == '__main__':
    app.run(debug=True)
