from modul import ExceptionGender
from modul.Parsing import Parsing


class Presenter:
    parsing = Parsing()

    def start(self):
        try:
            self.parsing.get_parsing(['4245', 'h'])
        except ExceptionGender:
            print(ExceptionGender.description)

        print(self.parsing.user_data)