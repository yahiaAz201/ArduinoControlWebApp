from flask_cors import CORS, cross_origin
import json
import serial
from flask import Flask

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={
    r"/*": {
        "origins": "*"
    }
})


@app.route('/')
def hello():
    file = open("value.txt", "r")
    val = file.read()
    file.close
    test_list = val.splitlines()
    while("" in test_list):
        test_list.remove("")

    num = test_list[len(test_list)-1]

    x = '{{"potValue":"{}"}}'.format(num)
    y = json.loads(x)

    return y


if __name__ == '__main__':
    app.run("127.0.0.1", "5000", debug=True)
