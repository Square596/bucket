import random

class Salon:
    def __init__(self, name: str, sex: str, year_of_birth: int):
        if year_of_birth > 2022:
            raise NameError('Incorrect year_of_birth!')
        if sex != 'M' and sex != 'F':
            raise NameError('Incorrect sex!')

        self.__name = name
        self.__sex = sex
        self.__age = 2022 - year_of_birth

    def get_name(self):
        return self.__name
    def get_sex(self):
        return self.__sex
    def get_age(self):
        return self.__age

class Human(Salon):
    def __init__(self, name: str, sex: str, year_of_birth: int, hair_length: int, nail_length: int, nail_color='colorless'):
        super().__init__(name, sex, year_of_birth)
        if hair_length <= 0:
            raise NameError('Incorrect hair_length!')
        if nail_length <=0:
            raise NameError('Incorrect nail_length!')
        self.hair_length = hair_length
        self.nail_length = nail_length
        self.nail_color = nail_color

class Manicurist(Salon):
    def __init__(self, name: str, sex: str, year_of_birth: int):
        super().__init__(name, sex, year_of_birth)

    def do_job(self, client):
        if client.nail_length == 0:
            raise NameError('Nails are too short!')
        else:
            client.nail_length -= 1
            client.nail_color = random.choice(['red', 'purple', 'green'])
            if client.nail_length == 0:
                client.nail_color = 'colorless'



class Hairdresser(Salon):
    def __init__(self, name: str, sex: str, year_of_birth: int):
        super().__init__(name, sex, year_of_birth)


    def do_job(self, client):
        if client.hair_length == 0:
            raise NameError('Hair is too short!')
        else:
            client.hair_length -= 1

class Barber(Salon):
    def __init__(self, name: str, sex: str, year_of_birth: int):
        super().__init__(name, sex, year_of_birth)

    def do_job(self, client):
        if client.get_sex() == 'F':
            raise ValueError('I only work with men!')

        if client.hair_length == 0:
            raise NameError('Hair is too short!')
        else:
            client.hair_length -= 1

neo = Human(
  name="Neo", sex="M", year_of_birth=1964,
  hair_length=10, nail_length=2
)
trinity = Human(
  name="Trinity", sex="F", year_of_birth=1967,
  hair_length=30, nail_length=5
)

manicurist = Manicurist(name="Samara", sex="F", year_of_birth=1992)
barber = Barber(name="Bob", sex="M", year_of_birth=1987)

manicurist.do_job(neo)
# Теперь у Нео ногти длины 1 и, например, фиолетовые
barber.do_job(neo)
# Теперь у Нео волосы длины 9

barber.do_job(trinity)
# А тут программа падает с исключением ValueError...