from typing import List

import pandas as pd

# from ..CustomException import ParseImportException
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class CSVIngestor(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """ Parse a CSV file

        Arguments: Path to CSV file with a valid csv extension
        Exception: ParseImportException
        Libraries: pandas to read csv file

        return List[QuoteModel]
        """
        if not cls.can_ingest(path):
            raise Exception(
                f'CSVIngestor can not parse {path}')

        quote_model_list = []
        df = pd.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote_model = QuoteModel(row['body'], row['author'])
            quote_model_list.append(new_quote_model)

        return quote_model_list

    def __repr__(self):
        return f'CSV Importer'
