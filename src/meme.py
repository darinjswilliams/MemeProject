import os
import random
import argparse

import pdb

from  CustomException.NoDirectoryException import NoDirectoryException
from  .Ingesters.Ingestor import Ingestor
from  .QuoteEngine.QuoteModel import QuoteModel

from .MemeGenerator.MemeEngine import MemeEngine
from .CustomException.ModelException import ModelException

# @TODO Import your Ingestor and MemeEngine classes

def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote and save image to
        temporary directory.

    >>> generate_meme('./src/_data/photos/dog/', 'test', 'test')
    >>> os.path.exists(path)
    >>> False
    """
    img = None
    quote = None

    if path is None:
        images = "./src/_data/photos/dog/"

        if not os.path.exists(images):
            raise NoDirectoryException(f'Directory {images} does not exists ')

        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')

        try:
            quote = QuoteModel(body, author)
        except ModelException(f'{body, author}') as me:
            print(me.message)

    meme = MemeEngine(f'./tmp/{img}')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    # @TODO Use ArgumentParser to parse the following CLI arguments
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    import doctest
    parser = argparse.ArgumentParser(description='Provide file path, body and author.')
    parser.add_argument('--path', type=str, help='Path to image')
    parser.add_argument('--body', type=str, help='Body text')
    parser.add_argument('--author', type=str, help='Author')

    args = parser.parse_args()
    doctest.testmod()

    # pdb.set_trace(header="Meme Generator Calling Meme")
    print(f'{generate_meme(args.path, args.body, args.author)}')
