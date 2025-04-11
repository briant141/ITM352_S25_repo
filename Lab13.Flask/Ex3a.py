from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def meme():
    url = "https://meme-api.com/gimme/wholesomememes"
    response = requests.get(url).json()
    
    meme_url = response.get("url")
    subreddit = response.get("subreddit")
    
    return render_template("meme.html", meme_url=meme_url, subreddit=subreddit)

if __name__ == "__main__":
    app.run(debug=True)
