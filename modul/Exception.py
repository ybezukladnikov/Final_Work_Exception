class MyEexception(Exception):
    """General exception class"""

    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f"Error: {self.message}"


class ExceptionGender(MyEexception):
    """Exception. Сhecking gender """
    description = "The gender should be entered 'f' or 'm'"
    pass