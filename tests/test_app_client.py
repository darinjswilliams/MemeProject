import io

import pytest
import requests
from PIL import Image

from src.app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_app_home_page_return_status_200(client):
    """ This test is verify that the home page will load
        and returns a status of 200

        A simple test just to make sure the page loads
    """
    response = client.get('/')
    assert response.status_code == 200


def test_app_meme_form_page_return_status_200(client):
    """ This test is verify that the meme page will load
        and returns a status of 200

        A simple test just to make sure the page loads
    """
    response = client.get('/create')
    assert response.status_code == 200


def test_url_from_web_return_request_form_data(requests_mock):
    """ Create a test image consisting of some bytes
        simulate testing request from web using requests_mock
     """
    image = Image.new('RGB', (100, 100), color='blue')
    image_bytes = io.BytesIO()
    image.save(image_bytes, format='PNG')
    image_bytes.seek(0)

    requests_mock.get('https://127.0.0.1:5000/form',
                                json={"image_url": f'{image}', "author": "DW", "body": "test"})

    form_data = requests.get('https://127.0.0.1:5000/form').json()
    assert form_data['author'] == "DW"

    assert form_data['body'] == "test"
    assert form_data['image_url'] is not None

    response = requests.get('https://127.0.0.1:5000/form', stream=True)
    assert response.status_code == 200

def test_app_meme_rand_return_html_template_with_title(client):
    """This test calls the meme_rand method in app.py returning
       html form

       This test is verify the code works and not route which is
       done with the flask test client
     """
    expect_title = 'Meme Generator'
    response = client.get('/')
    assert response.status_code == 200

    html_template = client.get('/')
    assert  b'<!doctype html>\n' in html_template.data
    assert expect_title in str(html_template.data)



