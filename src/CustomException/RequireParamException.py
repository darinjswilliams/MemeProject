class RequireParamException(Exception):
    """Custom Exceptions raised for parameters that is required

      Attributes:
           message - Explains the exceptions
      """

    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return f'RequireParmException({self.message})'