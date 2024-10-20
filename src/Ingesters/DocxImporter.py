from typing import List
import pandas as pd
import src.CustomException.ParseImportException

from .IngestorInterface import IngestorInterface
from src.QuoteEngine.QuoteModel import QuoteModel
from ..CustomException.ParseImportException import ParseImportException


class DocxImporter(IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise ParseImportException(f'{cls.__repr__} cannot parse {cls.allowed_extensions}')

        quote_model_list = []
        df = pd.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote_model = QuoteModel(row['body'], row['author'])
            quote_model_list.append(new_quote_model)

        return quote_model_list


    def __repr__(self):
        return f'Docx Importer (allowed extension  {self.allowed_extensions} )'