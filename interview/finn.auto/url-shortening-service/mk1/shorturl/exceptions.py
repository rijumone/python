class ShortURL404(Exception):

    def __init__(self, message):
        super().__init__(message)
