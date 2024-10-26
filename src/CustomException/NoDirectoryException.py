class NoDirectoryException(Exception):

    def __init__(self, message):
        self.message = message


    def __repr__(self):
        return f'NoDirectoryException({self.message})'
