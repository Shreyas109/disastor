from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Replace with your actual Twitter API key
TWITTER_BEARER_TOKEN = "cc0270d9e7mshefad09068ad93ebp1bd3f3jsnd62ab3030d61"

def get_tweets():
    url = "https://api.twitter.com/2/tweets/search/recent"
    headers = {"Authorization": f"Bearer {TWITTER_BEARER_TOKEN}"}
    params = {"query": "earthquake OR flood OR wildfire -is:retweet", "max_results": 10}
    
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        tweets = response.json().get("data", [])
        return [{"text": t["text"], "id": t["id"]} for t in tweets]
    else:
        return [{"error": "Failed to fetch tweets"}]

@app.route("/tweets", methods=["GET"])
def fetch_tweets():
    return jsonify(get_tweets())

if __name__ == "__main__":
    app.run(debug=True)
