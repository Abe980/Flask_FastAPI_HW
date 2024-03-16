from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import db, User
from flask_wtf.csrf import CSRFProtect
from form import LoginForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)
db.init_app(app)


@app.cli.command('init_db')
def init_db():
    db.create_all()
    print('Ok')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        last_name = form.last_name.data
        email = form.email.data
        password = hash(form.password.data)
        user = User(name=name, last_name=last_name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
    return render_template('index.html', form=form)


# @app.route('save_db', methods=['GET', 'POST'])
# def save_db():
#     pass


if __name__ == '__main__':
    app.run(debug=True)