from modul.Exception import *
from modul.Parsing import Parsing


class Presenter:
    parsing = Parsing()

    def start(self):
        try:
            self.parsing.get_parsing(['Петров','02.03.1988','3343', 'Иван', 'Иванович', 'f'])
        except ExceptionGender:
            print(ExceptionGender.description)

        except ExceptionDate:
            print(ExceptionDate.description)

        except ExceptionWrongNumberData:
            print(ExceptionWrongNumberData.description)

        except ExceptionNotAllData:
            print(ExceptionNotAllData.description)
            for key, value in self.parsing.user_data.items():
                if value == '':
                    print(key)




        print(self.parsing.user_data)