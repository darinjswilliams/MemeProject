from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


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
            raise Exception(
                f'ParseException{cls.__repr__} '
                f'cannot parse {cls.allowed_extensions}')

        quote_model_list = []
        try:
            with open(path, 'r') as data_file:
                for row in data_file.readlines():
                    row = row.strip('\n\r\f')
                    if len(row) > 0 and row != '':
                        parse = row.split('-')
                        new_quote_model = QuoteModel(parse[0], parse[1])
                        quote_model_list.append(new_quote_model)
        except Exception as nde:
            print(f'NoDirectoryException can not open file: {nde}')

        return quote_model_list

    def __ref__(self):
        return f'TXTImporter(allowed extensions {self.allowed_extensions})'
