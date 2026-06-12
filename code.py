from flask import Flask, request
import requests

app = Flask(__name__)

def get_target_url(user_input):
    return user_input

@app.route("/fetch")
def fetch():

    url = request.args.get("url")

    target_url = get_target_url(url)

    response = requests.get(target_url)

    return response.text

if __name__ == "__main__":
    app.run(debug=True)
