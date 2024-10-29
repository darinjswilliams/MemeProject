
from MemeGenerator import MemeEngine
from QuoteEngine import QuoteModel, Ingestor
from CustomException import RequireParamException, NoDirectoryException

import argparse
import os
import random

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
        # images = "./src/_data/photos/dog/"
        images = os.path.join('../src/_data', 'photos', 'dog')

        if not os.path.exists(images):
            raise NoDirectoryException(f'Directory {images} does not exists ')

        imgs = []

        try:
            for root, dirs, files in os.walk(images):
                imgs = [os.path.join(root, name) for name in files]
        except NoDirectoryException as nde:
            print('NoDirectoryException:(directory is not valid', nde)

        img = random.choice(imgs)
    else:
        img = path

    # pdb.set_trace(header='meme file -when body is none')
    if body is None:
        quote_files = ['../src/_data/DogQuotes/DogQuotesTXT.txt',
                       '../src/_data/DogQuotes/DogQuotesDOCX.docx',
                       '../src/_data/DogQuotes/DogQuotesPDF.pdf',
                       '../src/_data/DogQuotes/DogQuotesCSV.csv']

        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise RequireParamException(f'Author Required if Body is Present')

        try:
            quote = QuoteModel(body, author)
        except Exception(f'{body, author}') as me:
            print(me.message)

    meme = MemeEngine(f'./tmp/{img.split("/")[-1]}')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    # @TODO Use ArgumentParser to parse the following CLI arguments
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    parser = argparse.ArgumentParser(description='Provide file path, body and author.')
    parser.add_argument('--path', type=str, help='Path to image')
    parser.add_argument('--body', type=str, help='Body text')
    parser.add_argument('--author', type=str, help='Author')

    args = parser.parse_args()
    # doctest.testmod()

    # pdb.set_trace(header="Meme Generator Calling Meme")
    print(f'{generate_meme(args.path, args.body, args.author)}')
