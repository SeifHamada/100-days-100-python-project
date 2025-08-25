import requests
from flask import Flask, render_template_string

app = Flask(__name__)


template = """
<!DOCTYPE html>
<html>
<head>
    <title>NYC Subway Status</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        h1 { color: #333; }
        .line { margin: 10px 0; padding: 10px; border-radius: 5px; background: #f4f4f4; }
    </style>
</head>
<body>
    <h1>🚇 NYC Subway Status</h1>
    {% for line, status in subway_data.items() %}
        <div class="line"><strong>{{ line }}</strong>: {{ status }}</div>
    {% endfor %}
</body>
</html>
"""


@app.route("/")
def home():

    url = "https://api.mta.info/serviceStatus/subway"

    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        subway_data = {}
        for line in data["subway"]["line"]:
            name = line["name"]
            status = line["status"]
            subway_data[name] = status

    except Exception as e:
        subway_data = {"Error": "Could not fetch data"}

    return render_template_string(template, subway_data=subway_data)


if __name__ == "__main__":
    app.run(debug=True)
