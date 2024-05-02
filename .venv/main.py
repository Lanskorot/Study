import datetime
from flask import Flask

count = 0
app =  Flask(__name__)

@app.route('/')
def index():
    return f'Тест запущен в {datetime.datetime.now()} '

@app.route('/endpoint /hello/world')
def hello():
    return 'Hello, world!'


@app.route('/endpoint /counter')
def plas():
    global count
    count += 1
    return f'вссего вызовов: {str(count)}'


if __name__ == '__main__':
    app.run(debug=True)

