class ShortURL404(Exception):
    """
    Exception class for errors where the short_url
    either does not exist on the database or is not a
    valid hash
    """

    def __init__(self, message):
        super().__init__(message)
