from flask import Flask, request
import requests

ALLOWED_DOMAINS = [
    "example.com"
]

app = Flask(__name__)

def get_target_url(user_input):
    return user_input

def validate_url(url):
    print("Validating:", url)
    return url

@app.route("/fetch")
def fetch():

    url = request.args.get("url")

    target_url = get_target_url(url)

    validated_url = validate_url(target_url)

    if validated_url is None:
        return "Rejected"

    response = requests.get(validated_url)

    return response.text

if __name__ == "__main__":
    app.run(debug=True)
