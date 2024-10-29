
from src import meme as meme_setup
from src.CustomException import RequireParamException, NoDirectoryException
import pytest


def test_generate_meme_no_path_no_author_return_require_param_exception():
    body = "test"

    with pytest.raises(RequireParamException)as require_parm_exception:
        meme_setup.generate_meme(body=body)

    assert require_parm_exception.type == RequireParamException


def test_generate_meme_no_exception_raised_return_image_path():
    """This test use"""
    body = "test"
    author = "test"
    expected = meme_setup.generate_meme(body=body, author=author)
    assert expected != None


def test_generate_meme_no_path_returns_no_exception():
    """This test pass no parameters and return no exception
       returns a valid path inside tmp directory
       we only need to compare the extension of file return
    """
    actual_path = meme_setup.generate_meme()
    expected_file_ext = 'jpg'

    assert actual_path[-3:] == expected_file_ext