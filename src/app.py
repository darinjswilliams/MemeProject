import os
import random

import requests
from flask import Flask, render_template, request

from MemeGenerator import MemeEngine
from QuoteEngine import Ingestor
from Utils import create_tmp_dirs

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():

    """ Load all resources
        Setup returns a tuple consisting of quotes and images
        1. Create static directory if it doesn't exist'
        2. Join the base directory with subdirectory - quote_path
        3. Get a lit of file names only in the directory  - os.listdir
        4. Create complete path for images with join - use List comprehension
        5. Parse the quoted files - Call Ingestor parse on each file
        6. Get Path for images from tuple returned from os walk
        7. return quotes and images
    """
    create_tmp_dirs()
    quote_path = os.path.join('./', '_data/DogQuotes/')
    quote_files = os.listdir(quote_path)

    file_names = [os.path.join(quote_path, names) for names in quote_files]
    # quote_files variable
    quotes = [Ingestor.parse(qf) for qf in file_names]

    images_path = os.path.join('./', '_data/photos/dog/')

    # images within the images images_path directory
    imgs = [img for root, dir, img in os.walk(images_path)][0]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme
        Use the random python standard library class to:
        1. select a random image from imgs array
        2. select a random quote from the quotes array
    """
    img = random.choice(imgs)
    img_path = os.path.join('./', f'_data/photos/dog/{img}')
    random_quote = random.choice(random.choice(quotes))
    path = meme.make_meme(img_path, text=random_quote.body,
                          author=random_quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme
        Use Flask to get information from Form than use requests
        to call the url to retrieve th image
        1. Use requests to save the image from the image_url
           form param to a temp local file.
        2. Use the meme object to generate a meme using this temp
           file and the body and author form paramaters.
        3. Remove the temporary saved image.
    """

    path = request.form['image_url']

    try:
        image_data = requests.get(path)
        tmp = f'/tmp/{random.randint(1, 100000000)}.png'
        with open(tmp, 'wb') as img:
            img.write(image_data.content)

        path = meme.make_meme(tmp, request.form['body'],
                              request.form['author'])

        os.remove(tmp)

    except Exception:
        return render_template('meme_error.html')

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
