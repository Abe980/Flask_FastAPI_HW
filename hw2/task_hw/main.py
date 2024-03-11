from flask import Flask, render_template, request, make_response


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def cook():
    name = request.form['name']
    email = request.form['email']
    context = {'name': name, 'email': email}
    response = make_response(render_template('/login.html', **context))
    response.set_cookie('username', context['name'])
    response.set_cookie('email', context['email'])
    return response


@app.route('/logout/')
def logout():
    response = make_response(render_template('/index.html'))
    response.delete_cookie('username')
    response.delete_cookie('email')
    return response
    


if __name__ == '__main__':
    app.run(debug=True)