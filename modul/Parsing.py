class Parsing:

    user_data = {}

    def get_parsing(self, array):
        for el in array:
            if len(el) == 1: self.parsing_gender(el)



    def parsing_gender(self, simbol):
        if simbol == 'f': self.user_data['Gender'] = 'f'
        elif simbol == 'm': self.user_data['Gender'] = 'm'
        else: raise Exception




