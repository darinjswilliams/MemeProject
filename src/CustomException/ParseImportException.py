

class ParseImportException(Exception):
    """Exceptions raised for parsing files calls parent class with message

    Attributes:
         message - Explains the exceptions
    """
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'ParseImportException({self.message})'
