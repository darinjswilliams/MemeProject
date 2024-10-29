from typing import List

import docx

# from src.CustomException import ParseImportException
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface

class DocxIngestor(IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """ Parse a Doc file

            Arguments: Path to docx file with a valid docx extension
            Exception: ParseImportException if can not parse
            Libraries: docx to read document path file

            return List[QuoteModel]
        """
        if not cls.can_ingest(path):
            raise (Exception(
                    f'ParseException {cls.__repr__} cannot parse {cls.allowed_extensions}'))

        quote_model_list = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != '':
                parse = para.text.split(' - ')
                new_cat = QuoteModel(parse[0], parse[1])
                quote_model_list.append(new_cat)

        return quote_model_list

    def __repr__(self):
        return f'Docx Importer (allowed extension  {self.allowed_extensions} )'
