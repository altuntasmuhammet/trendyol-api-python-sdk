class TrendyolError(Exception):
    """
    Base class for Trendyol Api Error
    """
    pass


class TrendyolAPIError(TrendyolError):
    
    def __init__(self, message, response):
        self._message = message
        self._response = response
        
        super(TrendyolAPIError, self).__init__(
            "\n\n" +
            "  Message: %s\n" % self._message +
            "\n" +
            "  Status Code:  %s\n" % self._response.status_code +
            "  Response:\n    %s" % self._response.text +
            "\n"
        )