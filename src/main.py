
from MemeGenerator import MemeEngine
from QuoteEngine import QuoteModel, Ingestor
from CustomException import (RequireParamException, NoDirectoryException)
from Utils import create_tmp_dirs

import argparse
import os
import random


def generate_meme(path=None, body=None, author=None):
    """
        Generate a meme given an path and a quote and save image to
        temporary directory.

        The utility method create_tmp_dirs() creates a temporary directory for
        tmp and static. Note those folder are not stored in git repository.
        For future reference place all utility methods in helper file
    """
    img = None
    quote = None
    create_tmp_dirs()

    if path is None:
        images = "_data/photos/dog/"

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

    if body is None:
        quote_files = ['_data/DogQuotes/DogQuotesTXT.txt',
                       '_data/DogQuotes/DogQuotesDOCX.docx',
                       '_data/DogQuotes/DogQuotesPDF.pdf',
                       '_data/DogQuotes/DogQuotesCSV.csv']

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

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    # os.makedirs('./tmp', exist_ok=True)

    parser = argparse.ArgumentParser(
        description='Provide file path, body and author.')
    parser.add_argument('--path', type=str, help='Path to image')
    parser.add_argument('--body', type=str, help='Body text')
    parser.add_argument('--author', type=str, help='Author')

    args = parser.parse_args()
    # doctest.testmod()

    # pdb.set_trace(header="Meme Generator Calling Meme")
    print(f'{generate_meme(args.path, args.body, args.author)}')
