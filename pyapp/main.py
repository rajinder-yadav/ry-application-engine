from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Server is running on port 8080'

@app.route('/data')
def get_data():
    return jsonify({
        "modelname": "pik 2.0 purchase flow",
        "modelversion": "2019-11-01 16:43:25.021586",
        "recommendations": [
            {
                "component ID": "50869",
                "fifa ID": "9136080258413413392",
                "name": "MOVIETIME",
                "weight": 0.02578764595091343
            },
            {
                "component ID": "55113",
                "fifa ID": "9146894752513896209",
                "name": "HISTORY TELEVISION",
                "weight": 0.025303268805146217
            },
            {
                "component ID": "50760",
                "fifa ID": "9147136763813749660",
                "name": "A&E",
                "weight": 0.025085553526878357
            },
            {
                "component ID": "50852",
                "fifa ID": "9147136763813749747",
                "name": "HGTV",
                "weight": 0.02168024703860283
            },
            {
                "component ID": "50885",
                "fifa ID": "9147205044813838373",
                "name": "NATIONAL GEOGRAPHIC CHANNEL",
                "weight": 0.021538956090807915
            },
            {
                "component ID": "65591",
                "fifa ID": "9147137180013749872",
                "name": "AMC",
                "weight": 0.021384000778198242
            },
            {
                "component ID": "50929",
                "fifa ID": "9147136763813749727",
                "name": "FOOD NETWORK CANADA",
                "weight": 0.02079412341117859
            },
            {
                "component ID": "50806",
                "fifa ID": "9147137180013749924",
                "name": "DISCOVERY CHANNEL",
                "weight": 0.0207687821239233
            },
            {
                "component ID": "50791",
                "fifa ID": "9147325096213850877",
                "name": "CNN",
                "weight": 0.019928721711039543
            },
            {
                "component ID": "50932",
                "fifa ID": "9147136974613749834",
                "name": "TLC",
                "weight": 0.019688116386532784
            }
        ]
    })

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
