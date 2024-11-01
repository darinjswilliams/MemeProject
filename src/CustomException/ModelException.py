class ModelException(Exception):
    """Custom Model Exception class to handle model exceptions

        if the creation of a QuoteModel throws an exception
        A Custom Model Exception is raised
    """

    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return f'ModelException({self.message})'
