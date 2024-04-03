class ExceededRateLimitError(Exception):
    def __str__(self):
        return "No more tokens to use"
