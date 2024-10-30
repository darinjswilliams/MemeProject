import collections
import os

from src.QuoteEngine import Ingestor as ingest
from src.app import setup as app_setup


def test_setup_return_image_count():

    """This is a general test for independently testing code in setup() without it being
       calling the actual setup method in app.py
    """
    quote_path = os.path.join('../src', '_data/DogQuotes/')
    assert quote_path == '../src/_data/DogQuotes/'

    file_list = os.listdir(quote_path)
    assert len(file_list) == 4

    # TODO: Use the Ingestor class to parse all files in the
    # quote_files variable
    file_names = [ os.path.join(quote_path, names) for names in file_list]
    quotes = [ingest.parse(qf) for qf in file_names]
    assert len(quotes) == 4

    images_path = "./_data/photos/dog/"
    images_path = os.path.join('../src', '_data/photos/dog/')
    # assert images_path != './_data/photos/dog/'

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    img = [ img for root, dir, img in os.walk(images_path)][0]
    expected_cnt = 4
    actual_cnt = collections.Counter(img)
    assert expected_cnt == len(actual_cnt)

def test_app_setup_return_quotes_count():
    """This test calls the setup() method in app.py returning the count of quotes
       the count of quotes
    """
    actual_quotes, actual_images = app_setup()
    expected_quotes = 4
    assert len(actual_quotes) == expected_quotes



def test_app_setup_return_image_count():
    """This test calls the setup() method in app.py returning the count of images
       the count of quotes
    """
    actual_quotes, actual_images = app_setup()
    expected_images = 4
    actual_image_cnt = collections.Counter(actual_images)
    assert len(actual_image_cnt) == expected_images

