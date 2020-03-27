class Error(Exception):
    #Base class for exceptions in this module.
    pass

class HelpError(Error):
    message = """
    Help me
    """
    def __init__(self, message):
        self.message = message
