from typing import List

from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .IngestorInterface import IngestorInterface
from .PDFIngestor import PDFIngestor
from .TextIngestor import TXTIngestor
from ..QuoteEngine.QuoteModel import QuoteModel


class Ingestor(IngestorInterface):

    importers = [PDFIngestor, DocxIngestor, CSVIngestor, TXTIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for importer in cls.importers:
            if importer.parse(path):
                return importer.parse(path)
