import random
import os
from operator import index

import random
import requests
from flask import Flask, render_template, abort, request

# @TODO Import your Ingestor and MemeEngine classes
from  .Ingesters.Ingestor import Ingestor as ingestor
from  .MemeGenerator.MemeEngine import MemeEngine as meme_engine

app = Flask(__name__)

meme = meme_engine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # TODO: Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = [ingestor.parse(qf) for qf in quote_files]

    images_path = "./_data/photos/dog/"

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = os.walk(images_path)

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme
        Use Flask to get information from Form than use requests
        to call the url to retrieve the image
        1. Use requests to save the image from the image_url
           form param to a temp local file.
        2. Use the meme object to generate a meme using this temp
           file and the body and author form paramaters.
        3. Remove the temporary saved image.
    """
    path = request.form['image_url']
    image_data = requests.get(path)
    tmp = f'/tmp/{random.randint(1, 100000000)}.png'
    with open(tmp, 'wb') as img:
        img.write(image_data.content)

    meme_obj = meme.make_meme(tmp, request.form['body'], request.form['author'])

    print(meme_obj)

    os.remove(tmp)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
