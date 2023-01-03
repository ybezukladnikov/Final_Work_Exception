from modul.Exception import *
from view.Input import *
from modul.Parsing import Parsing
from modul.WriteFile import *


class Presenter:
    parsing = Parsing()
    read_write = ReadWriteFile()
    input_d = Input()


    def start(self):

        while True:

            try:
                data = self.input_d.input_data()
                self.parsing.get_parsing(data)
                break
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

        self.read_write.write_file(self.parsing.user_data)
        self.parsing.clear_user_data()

