from src.QuoteEngine.Ingestor import Ingestor
from src.QuoteEngine.TextIngestor import TXTIngestor
from src.QuoteEngine.PDFIngestor import PDFIngestor
from src.QuoteEngine.CSVIngestor import CSVIngestor
from src.QuoteEngine.DocxIngestor import DocxIngestor

import os
import pytest



class Test_Ingestor:

    def setup_method(self, method):
        print(f'setup method {method.__name__}')
        self.ingestor = Ingestor()
        self.allowed_importers = [PDFIngestor, DocxIngestor, CSVIngestor, TXTIngestor]
        self.base_dir = '../src/_data'
        self.parent_dir = 'SimpleLines'
        self.invalid_txt_file_name = 'SimpleLines.xml'


    @pytest.mark.parametrize('file_input', ['SimpleLines.txt','SimpleLines.docx','SimpleLines.csv'])
    def test_ingestor_parse_with_valid_files_types(self, file_input):
        """Parameterize Test will validate Strategy Object Pattern is working properly.
           the test will call in the parse function.  Prior to getting called with correct
           ingestor, a call is made to can_ingest to validate extenstion

           Arguments: File with  extension
           Output: Return valid count of data in parse file
           Valid Extension are PDF, Txt, Docx and CSV
        """
        file_path = os.path.join(self.base_dir, self.parent_dir, file_input)
        expect_path_cnt = 5
        actual_path = self.ingestor.parse(file_path)

        assert len(actual_path) == expect_path_cnt


    def test_ingestor_parse_with_invalid_files_types_return_none(self):
        """Test will validate Strategy Object Pattern is working properly.

            Arguments: File with invalid extension
            Output: None - which means the object file can not be ingest
            Valid Extension are PDF, Txt, Docx and CSV
        """
        file_path = os.path.join(self.base_dir, self.parent_dir, self.invalid_txt_file_name)
        expect_parse = None
        actual_path = self.ingestor.parse(file_path)
        assert   actual_path == expect_parse
