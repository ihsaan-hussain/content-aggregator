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
    images_list = []

    url = "https://www.bbc.co.uk/news/world"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "lxml")
    h3 = soup.find_all("h3")
    images = soup.find_all("img", src="https://ichef.bbci.co.uk/news/490/cpsprodpb/E7E8/production/_131486395_gettyimages-1746151111.jpg")

    for image in images:
        images_list.append(image['src'])

    for x in h3:
        headlines.append(x.text)

    return render_template('world.html', headlines=headlines, photos=images_list)