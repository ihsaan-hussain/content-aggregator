from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    url = "https://www.youtube.com/feed/trending"

    get_url = requests.get(url)
    get_text = get_url.text

    soup = BeautifulSoup(get_text, "html.parser")
    tags = soup.find_all("ytd-app")

    return render_template('home.html', tags=tags)