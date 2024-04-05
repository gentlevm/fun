from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def get_meme():
    url = "https://meme-api.com/gimme/memes"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        meme_large = data["preview"][-2]
        subreddit = data["subreddit"]
        return meme_large, subreddit
    except Exception as e:
        # Log the error or handle it gracefully
        print("Error fetching meme:", e)
        return None, None

@app.route("/")
def index():
    meme_pic, subreddit = get_meme()
    if meme_pic is None:
        return "Failed to fetch meme. Please try again later."
    return render_template("meme.html", meme_pic=meme_pic, subreddit=subreddit)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
