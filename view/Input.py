'''Фамилия не должна состоять из одной буквы. Фамилия, Имя, Отчество могут быть введены на разном порядке, но слева
Направа порядок должен соблюдаться.'''

class Input:
    def input_data(self):
        return input("Фамилия Имя Отчество датарождения номертелефона пол"+ '\n').split(' ')