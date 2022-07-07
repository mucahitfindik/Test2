import datetime as dt


class InvalidRequestParameter(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message


class InvalidCurrency(InvalidRequestParameter):
    def __init__(self, message):
        super().__init__(message)


def check_required_parameters(data):
    if "amount" not in data:
        raise InvalidRequestParameter("No amount provided!")
    elif not isinstance(data["amount"], int):
        raise InvalidRequestParameter("Amount should be number!")
    elif "toCurrency" not in data or data["toCurrency"] == "" or data["toCurrency"] == []:
        raise InvalidRequestParameter("No toCurrency provided!")
    elif not (isinstance(data["toCurrency"], list) or isinstance(data["toCurrency"], str)):
        raise InvalidRequestParameter("toCurrency should be array or string!")
    elif "fromCurrency" not in data or data["fromCurrency"] == "":
        raise InvalidRequestParameter("No fromCurrency provided!")
    elif not isinstance(data["fromCurrency"], str):
        raise InvalidRequestParameter("fromCurrency should be string!")
    elif "date" not in data or data["date"] == "":
        raise InvalidRequestParameter("No date provided!")
    elif not isinstance(data["date"], str):
        raise InvalidRequestParameter("date should be string!")
    try:
        dt.date.fromisoformat(data["date"])
    except ValueError:
        raise InvalidRequestParameter("Incorrect date format, should be YYYY-MM-DD")


def check_currency_supported(from_currency, to_currency, currency_list):
    if from_currency not in currency_list:
        raise InvalidCurrency("Currency list doesn't include " + from_currency + ".")

    for currency in to_currency:
        if currency not in currency_list:
            raise InvalidCurrency("Currency list doesn't include " + currency + ".")
