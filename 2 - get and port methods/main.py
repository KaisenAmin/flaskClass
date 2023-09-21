from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/show-me')
def show_message():
    return "Hello World"

@app.route('/form')
def get_form():
    return render_template('index.html')

@app.route('/process', methods=['POST', 'GET', ])
def procces_request():
    if request.method == 'POST':
        my_name: str = request.form['name']
        return f'Hello this is post method {my_name}'
    elif request.method == 'GET':
        user_name: str = request.args.get('name')
        return f'Hello this is get method {user_name}' 
    
    else:
        return f'I dont know '


if __name__ == '__main__':
    app.run(debug=True)