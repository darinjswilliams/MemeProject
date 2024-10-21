from .CSVImporter import CSVImporter
from .DocxImporter import DocxImporter
from .IngestorInterface import IngestorInterface
from .PDFImporter import PDFImporter
from .TXTImporter import TXTImporter
from ..QuoteEngine.QuoteModel import QuoteModel


class Importer(IngestorInterface):

    importers = [DocxImporter, PDFImporter, CSVImporter, TXTImporter]


    @classmethod
    def parse(cls, path) -> list[QuoteModel]:
        for importer in cls.importers:
            if importer.parse(path):
                return importer.parse(path)