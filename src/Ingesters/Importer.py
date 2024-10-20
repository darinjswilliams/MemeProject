from src.Ingesters.CSVImporter import CSVImporter
from src.Ingesters.DocxImporter import DocxImporter
from src.Ingesters.IngestorInterface import IngestorInterface
from src.Ingesters.PDFImporter import PDFImporter
from src.Ingesters.TXTImporter import TXTImporter
from src.QuoteEngine.QuoteModel import QuoteModel


class Importer(IngestorInterface):

    importers = [DocxImporter, PDFImporter, CSVImporter, TXTImporter]


    @classmethod
    def parse(cls, path) -> list[QuoteModel]:
        for importer in cls.importers:
            if importer.parse(path):
                return importer.parse(path)