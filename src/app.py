import os

import random
import requests
from flask import Flask, render_template, request

from .CustomException import MemeException
# @TODO Import your Ingestor and MemeEngine classes
from .QuoteEngine import Ingestor
from .MemeGenerator import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():

    """ Load all resources
        Setup returns a tuple consisting of quotes and images
        
        1. Join the base directory with subdirectory - quote_path
        2. Get a lit of file names only in the directory  - os.listdir
        3. Create complete path for images with join - use List comprehension
        4. Parse the quoted files - Call Ingestor.parse on each file
        5. Get Path for images from tuple returned from os.walk
           os.walk- returns tuple so grab only the images from list
        6. return quotes and images
    """
    quote_path = os.path.join('../src', '_data/DogQuotes/')
    quote_files = os.listdir(quote_path)

    # TODO: Use the Ingestor class to parse all files in the
    file_names = [os.path.join(quote_path, names) for names in quote_files]
    # quote_files variable
    quotes = [Ingestor.parse(qf) for qf in file_names]

    images_path = os.path.join('../src', '_data/photos/dog/')

    # TODO: Uhse the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = [ img for root, dir, img in os.walk(images_path)][0]

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

    try:
        image_data = requests.get(path)
        tmp = f'/tmp/{random.randint(1, 100000000)}.png'
        with open(tmp, 'wb') as img:
            img.write(image_data.content)

        meme.make_meme(tmp, request.form['body'], request.form['author'])

        os.remove(tmp)

    except MemeException as me:
        print(f'Meme Generator Exception Occurred {me.message}')

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
