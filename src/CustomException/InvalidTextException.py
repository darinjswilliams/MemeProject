

class InvalidTextException(Exception):
    """Custom Exception class to handle invalid text exceptions"""
    def __init__(self, message):
        self.message = message