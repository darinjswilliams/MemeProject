from typing import List

from .IngestorInterface import IngestorInterface
from ..CustomException.ParseImportException import ParseImportException
from ..QuoteEngine.QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """   Parse a Text file with a valid text extension

              Arguments: Path to text file
              Exception: ParseImportException if can not parse file
              Libraries: open file, readline and split on character delimiter

              return List[QuoteModel]
        """
        if not cls.can_ingest(path):
            raise ParseImportException(f'{cls.__repr__} cannot parse {cls.allowed_extensions}')

        quote_model_list = []
        with open(path, 'r') as data_file:
            for index, row in data_file.readline().split('-'):
                new_quote_model = QuoteModel(row['body'], row['author'])
                quote_model_list.append(new_quote_model)

        return quote_model_list

    def __ref__(self):
        return f'TXTImporter(allowed extensions {self.allowed_extensions})'