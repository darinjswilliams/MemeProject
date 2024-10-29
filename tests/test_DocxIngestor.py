from src.QuoteEngine import DocxIngestor as ingest
from src.CustomException.ParseImportException import ParseImportException
import os
import pytest

class Test_DocxIngestor:

    def setup_method(self, method):
        """ setup any state tied to the execution of the given method in a
            class.  setup_method is invoked for every test method of a class.
        """
        print(f"setup method {method.__name__}")
        self.base_dir = '../src/_data'
        self.pdf_dir = 'SimpleLines'
        self.invalid_doc_file_name = 'SimpleLines.tff'
        self.valid_doc_file_name = 'SimpleLines.docx'

    def test_parse_invalid_file_return_parse_exception(self):
        """
            Test on parsing file with invalid extension
            raises ParseImportException
        """
        file_name = os.path.join(self.base_dir, self.pdf_dir, self.invalid_doc_file_name)
        with pytest.raises(ParseImportException) as parse_exception:
            ingest.parse(file_name)
        assert parse_exception.type == ParseImportException


    def test_parse_valid_docx_file_return_file_size(self):
        """
            Test on parsing file with valid extension
            and validate file size
         """
        file_name = os.path.join(self.base_dir, self.pdf_dir, self.valid_doc_file_name)
        expected_file_size = ingest.parse(file_name)
        assert len(expected_file_size) > 0


