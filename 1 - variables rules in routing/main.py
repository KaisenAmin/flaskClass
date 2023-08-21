from flask import Flask 
from flask import url_for

app = Flask(__name__)


@app.route('/username/<name>')
def show_name(name):
    return f"<h1> My name is {name}</h1>"


@app.route('/id/<int:my_id>')
def show_my_id(my_id):
    return f"<h2>My id number is {my_id}</h2>"


@app.route('/info/username/<name>/age/<int:my_age>')
def show_information(name, my_age):
    info = {
        'name': name,
        'age': my_age
    }

    return info


@app.route('/showpath/<path:my_path>')
def show_my_path(my_path):
    return f"<h1>the path of folder is {my_path}</h1>"


@app.route('/projects/')
def show_projects():
    return "<h2>my project is good</h2>"

@app.route('/about/')
@app.route('/about')
def about():
    return "Kaisen Channel is perfect:))"


@app.route('/channel', defaults={'channel_name': 'Kaisen'})
@app.route('/channel/<channel_name>')
def show_my_channel_name(channel_name):
    return f"<h2>My Channel name is {channel_name}</h2>"


@app.route('/')
def index():
    my_url = url_for('show_name', name="Python_Flask_Framwork")
    return f"The url is {my_url}"