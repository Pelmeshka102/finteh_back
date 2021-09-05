from flask import Flask, json

data = {
    "forecast": [
        {"y": 31850910313.0, "year": 2010},
        {"y": 35935356067.74, "year": 2011},
        {"y": 33150930793.99, "year": 2012},
        {"y": 30576682754.19, "year": 2013},
        {"y": 34117735931.87, "year": 2014},
        {"y": 34801533070.6, "year": 2015},
        {"y": 39323606617.18, "year": 2016},
        {"y": 41108607816.91, "year": 2017},
        {"y": 54378039681.2, "year": 2018},
        {"y": 58543527525.81, "year": 2019},
        {"y": 68182687573.07, "year": 2020},
        {"y": 58263280752.01, "year": 2021}
    ],
    "result": [
        {"y": 58543739759.0, "year": 2019},
        {"y": 58543739759.0, "year": 2020},
        {"y": 58543739759.0, "year": 2021},
    ],
}

api = Flask(__name__)


@api.route('/data', methods=['GET'])
def get_data():
    return json.dumps(data)


if __name__ == '__main__':
    api.run(host='0.0.0.0', port=5000, debug=True, threaded=True)







