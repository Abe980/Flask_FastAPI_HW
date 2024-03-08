from flask import Flask, render_template


app = Flask(__name__)


@app.route('/main/')
@app.route('/')
def main():
    return render_template('base.html')


@app.route('/clothes/')
def get_clothes():
    return render_template('clothes.html')


@app.route('/clothes/jacket/')
def get_jacket():
    return render_template('jacket.html')


@app.route('/shoes/')
def get_shoes():
    return render_template('shoes.html')


if __name__ == '__main__':
    app.run()