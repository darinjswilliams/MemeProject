from src.Ingesters.TextIngestor import TXTIngestor as txt_ingestor
from src.CustomException.ParseImportException import ParseImportException
import os
import pytest

class Test_TextIngestor:

    def setup_method(self, method):
        print(f'setup_method: {method.__name__}')
        self.base_dir = '../src/_data'
        self.txt_dir = 'SimpleLines'
        self.invalid_txt_file_name = 'SimpleLines.xml'
        self.valid_txt_file_name = 'SimpleLines.txt'
        self.txt_ingestor = txt_ingestor


    def test_parse_verify_return_list_count(self):
        expected_count = 5
        path = os.path.join(self.base_dir, self.txt_dir, self.valid_txt_file_name)
        actual_count = self.txt_ingestor.parse(path)
        assert expected_count == len(actual_count)


    def test_exception_raise_return_parse_exception(self):
        """ Test to validate that a Parse Exception is raised
            when file has invalid extension

        if a valid file is pass the test will fail because it is expecting
        a Parse Import Exception. No Parse Exception is raised
        This confirms that the test is working

        If a invalid file is passed test will fail and raised a Parse Import Exception

        """
        filename = os.path.join(self.base_dir, self.txt_dir, self.invalid_txt_file_name)
        with pytest.raises(ParseImportException) as parse_exception:
            self.txt_ingestor.parse(filename)
        assert parse_exception.type == ParseImportException







