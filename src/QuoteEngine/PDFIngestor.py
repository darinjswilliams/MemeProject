import os
import random
import subprocess
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
# from ..CustomException import ParseImportException


class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse a PDF file with a valid pdf extension

        Arguments: a list containing - path to pdf file, tmp directory
        Exception: ParseImportException
        Libraries: Subprocess call  to pdftotext to
                   read pdf file using file written to tmp
        """
        if not cls.can_ingest(path):
            raise Exception(
                f'ParseException {cls.__repr__} '
                f'cannot parse {cls.allowed_extensions}')

        tmp = f'./tmp/{random.randint(0, 100000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])

        if call != 0:
            raise Exception('ParseException pdftotext failed to parse', path)

        file_ref = open(tmp, 'r')
        quote_model_list = []

        for line in file_ref.readlines():
            line = line.strip('\n\r\f').strip()
            if len(line) > 0 and line != '' and line != '"':
                parse = line.split('-')
                new_quote_model = QuoteModel(parse[0], parse[1])
                quote_model_list.append(new_quote_model)

        file_ref.close()
        os.remove(tmp)
        return quote_model_list

    def __repr__(self):
        return f'PDFImporter(allowed extension {self.allowed_extensions})'
