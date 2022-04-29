from extensions.database import db
from http import cookies
from os import environ
from flask import Flask, redirect, render_template, url_for, send_file

app = Flask(__name__)
app.config.from_object('config')



@app.route('/')
def index():
    return render_template('login.html')

@app.route('/to_do')
def toDo():
  return render_template('to-do.html')
  
@app.route('/about-me')
def about_me():
  return redirect('https://codecookies.xyz')

def register_extensions(app: Flask):
  db.init_app(app)
  
if __name__ == '__main__':
    app.run()