from flask import Flask, render_template
import requests
import json
from songs import songs
from chat import chat
from tone import tone
app = Flask(__name__)

app.register_blueprint(songs)
app.register_blueprint(chat)
app.register_blueprint(tone)


@app.route('/api')
def hello_world():
    obj={"hi":1}
    return obj


if __name__=='__main__':
    app.run(debug=True)


