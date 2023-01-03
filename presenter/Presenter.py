from modul.Exception import *
from modul.Parsing import Parsing
from modul.WriteFile import *


class Presenter:
    parsing = Parsing()
    read_write = ReadWriteFile()


    def start(self):
        my_list = [
            ['testr','02.03.1988','3343', 'Иван', 'Иванович', 'f'],
            ['petrov', '02.03.1588', '33343', 'Иванr', 'Иванович', 'm'],
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
            self.read_write.write_file(self.parsing.user_data)
            self.parsing.clear_user_data()

