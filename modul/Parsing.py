from modul.Exception import *
import time


class Parsing:
    user_data = {
        'Surname': '',
        'Name': '',
        'Patronymic': '',
        'Gender': '',
        'Date': '',
        'Telefon': '',
    }

    def clear_user_data(self):
        self.user_data = {
        'Surname': '',
        'Name': '',
        'Patronymic': '',
        'Gender': '',
        'Date': '',
        'Telefon': '',
        }


    def get_parsing(self, array):
        if len(array)!= 6:
            raise ExceptionWrongNumberData('Incorrect amount of data entered')

        for el in array:
            if len(el) == 1:
                self.parsing_gender(el)
            elif '.' in el:
                self.parsing_data(el)
            elif len(el) > 1 and el.isalpha():
                self.parsing_fio(el)
            elif len(el) > 1 and el.isdigit():
                self.parsing_phone(el)

        for value in self.user_data.values():
            if value == '': raise ExceptionNotAllData("The following data is entered incorrectly:")

        return self.user_data

    def parsing_gender(self, simbol):
        if simbol == 'f':
            self.user_data['Gender'] = 'f'
        elif simbol == 'm':
            self.user_data['Gender'] = 'm'
        else:
            raise ExceptionGender("The gender should be entered 'f' or 'm'")

    def parsing_data(self, el):
        try:
            time.strptime(el, '%m.%d.%Y')
            self.user_data['Date'] = el
        except ValueError:
            raise ExceptionDate("The gender should be entered 'f' or 'm'")

    def parsing_fio(self, el):
        if self.user_data['Surname'] == '':
            self.user_data['Surname'] = el.title()
        elif self.user_data['Name'] == '':
            self.user_data['Name'] = el.title()
        else:
            self.user_data['Patronymic'] = el.title()

    def parsing_phone(self, el):
        self.user_data['Telefon'] = el

