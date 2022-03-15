from flask import Flask
import os
# from flask_ngrok import run_with_ngrok

app = Flask(__name__)
# run_with_ngrok(app)


@app.route('/')
def index():
    return 'АзМеНтЕс ВаЙн'


if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(port=port)
