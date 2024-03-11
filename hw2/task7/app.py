# Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.

from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/res/', methods=['GET', 'POST'])
def counter():
    num = int(request.form['num'])
    return f'Число: {num}, его квадрат: {num*num}'


if __name__ == '__main__':
    app.run(debug=True)