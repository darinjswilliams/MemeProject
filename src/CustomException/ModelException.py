class ModelException(Exception):


    def __init__(self, message):
        self.message = message


    def __repr__(self):
        return f'ModelException({self.message})'