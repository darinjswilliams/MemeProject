class NoDirectoryException(Exception):
    """Custom Exception class to handle no directory exceptions

       If a directory does not exists or a file does not exists.
       A Custom Exception is raised
    """
    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return f'NoDirectoryException({self.message})'
