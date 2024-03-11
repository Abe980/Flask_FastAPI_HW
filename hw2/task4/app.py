# Создать страницу, на которой будет форма для ввода текста и
# кнопка "Отправить"
# При нажатии кнопки будет произведен подсчет количества слов
# в тексте и переход на страницу с результатом.


from flask import Flask, render_template, request, make_response


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/counter/', methods=['GET', 'POST'])
def counter():
    return f'{len(request.form["my_text"].split(" "))} words'




if __name__ == '__main__':
    app.run(debug=True)