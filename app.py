from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    url = "https://news.google.com/home?hl=en-GB&gl=GB&ceid=GB:en"

    get_url = requests.get(url)
    get_text = get_url.text

    soup = BeautifulSoup(get_text, "html.parser")

    return render_template('home.html',  tags=tags, soup=soup)