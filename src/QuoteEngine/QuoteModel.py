class QuoteModel():
    """ Quote Model is the data object tha takes 2 arguments

        Arguments:
        str - body
        str - author
    """
    def __init__(self, body: str, author: str):
        self.body = body
        self.author = author

    def __repr__(self):
        return f'"{self.body}" - {self.author}'

    def __str__(self):
        return f'QuoteModel({self.body}, {self.author})'
