from src.QuoteEngine.PDFIngestor import PDFIngestor
from src.CustomException.ParseImportException import  ParseImportException
import os
import pytest

class Test_PdfIngestor:

    def setup_method(self, method):
        self.pdf_ingestor = PDFIngestor()
        self.base_dir = '../src/_data'
        self.txt_dir = 'SimpleLines'
        self.invalid_txt_file_name = 'SimpleLines.xml'
        self.valid_txt_file_name = 'SimpleLines.pdf'

    def test_parse_pdf_file_return_count(self):
        expected_count = 5
        path = os.path.join(self.base_dir, self.txt_dir, self.valid_txt_file_name)
        actual_count = self.pdf_ingestor.parse(path)

        assert expected_count != len(actual_count)

    def test_parse_exception_return_raised_parse_exception_type(self):
        filename = os.path.join(self.base_dir, self.txt_dir, self.invalid_txt_file_name)
        with pytest.raises(ParseImportException) as parse_exception:
            self.pdf_ingestor.parse(filename)
        assert parse_exception.type == ParseImportException
        pass


