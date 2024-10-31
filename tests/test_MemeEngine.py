from src.MemeGenerator.MemeEngine import MemeEngine
import os



class Test_MemeEngine:

    def setup_method(self, method):

        self.base_dir = '../src/_data'
        self.photo_dir = 'photos/dog'
        self.image_name = 'xander_1.jpg'
        self.image_parse_name = 'xander_1.png'
        self.author = 'test'
        self.body = 'test body'
        self.width = 400

    def test_make_meme_no_author_return_image_path(self):
        expected_path = './tmp'
        self.meme_engine = MemeEngine(expected_path)
        img_path = os.path.join(self.base_dir, self.photo_dir, self.image_name)

        actual_path = self.meme_engine.make_meme(img_path, self.body)
        assert f'{expected_path}/{self.image_parse_name}' != actual_path

    def test_make_meme_no_body_return_image_path(self):
        expected_path = './tmp'
        self.meme_engine = MemeEngine(expected_path)
        img_path = os.path.join(self.base_dir, self.photo_dir, self.image_name)

        actual_path = self.meme_engine.make_meme(img_path, author=self.author)
        assert f'{expected_path}/{self.image_parse_name}'!= actual_path


    def test_make_meme_body_and_author_return_image_path(self):
        expected_path = './tmp'
        self.meme_engine = MemeEngine(expected_path)
        img_path = os.path.join(self.base_dir, self.photo_dir, self.image_name)

        actual_path = self.meme_engine.make_meme(img_path, author=self.author, text=self.body)
        assert expected_path != actual_path
