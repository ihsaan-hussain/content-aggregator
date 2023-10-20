from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/world')
def world():
    # world news page

    headlines = []

    url = "https://www.bbc.co.uk/news/world"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "lxml")
    
    h3 = soup.find_all("h3")

    for x in h3:
        headlines.append(x.text)

    return render_template('world.html', headlines=headlines)