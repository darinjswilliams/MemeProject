class MemeException(Exception):
    """"Custom Exception class to handle meme exceptions
        returns the exception message

        The class also use the __rpr__ method for debug purpose
    """
    def __init__(self, message):
        self.message = message

    def __rpr__(self):
        return f'MemeException({self.message})'
