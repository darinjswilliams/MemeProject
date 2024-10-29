from src.QuoteEngine import CSVIngestor as ingest
from src.CustomException.ParseImportException import ParseImportException
import os
import pytest

class Test_CSVIngestor:

    def setup_method(self, method):
        """ setup any state tied to the execution of the given method in a
            class.  setup_method is invoked for every test method of a class.
        """
        print(f"setup method {method.__name__}")
        self.base_dir = '../src/_data'
        self.csv_dir = 'SimpleLines'
        self.invalid_csv_file_name = 'SimpleLines.xml'
        self.valid_csv_file_name = 'SimpleLines.csv'

    def test_to_see_if_directory_exists_return_true(self):
        dir_name = '../src/_data/SimpleLines/'
        """ Check if the directory exists returns true"""
        assert  os.path.dirname(dir_name) == '../src/_data/SimpleLines'


    def test_exception_raise_return_parse_exception(self):
        """ Test to validate that a Parse Exception is raised
            when file has invalid extension
        """
        filename = os.path.join(self.base_dir, self.csv_dir, self.invalid_csv_file_name)
        with pytest.raises(ParseImportException) as parse_exception:
            ingest.parse(filename)
        assert parse_exception.type == ParseImportException


    def test_valid_parse_return_file_size(self, tmp_path):
        """
          Test to validate that a CSVIngestor is able to parse the file
          returns the length of the file
        """
        file_name =  os.path.join(self.base_dir, self.csv_dir, self.valid_csv_file_name)
        expected_list = ingest.parse(file_name)
        assert len(expected_list) > 0








