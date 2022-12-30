from modul.Exception import *
from modul.Parsing import Parsing


class Presenter:
    parsing = Parsing()

    def start(self):
        my_list = [
            ['Петров','02.03.1988','3343', 'Иван', 'Иванович', 'f'],
            ['Петров', '02.03.1988', '3343', 'Иван', 'Иванович', 'm'],
        ]
        for i in my_list:
            try:
                self.parsing.get_parsing(i)
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