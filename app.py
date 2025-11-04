from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello from Azure with Python! V2</h1><p>Виконав Полончук Павло Олександрович/Веселий Роджер/Болбочан студента групи КН-22 <\p>"

if __name__ == '__main__':
    app.run()


