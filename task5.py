import random
from typing import List, Optional
from datetime import datetime
from abc import ABC, abstractmethod



class Human(ABC):

    def __init__(self, name: str, sex: str, year_of_birth: int):
        current_year = datetime.now().year
        if year_of_birth > current_year:
            raise ValueError(f'Incorrect year_of_birth: {year_of_birth}! It should be no more than {current_year}!')
        if sex not in ['M', 'F']:
            raise TypeError('Incorrect sex! It should be "M" for men and "F" for women!')

        self._name = name
        self._sex = sex
        self._age = current_year - year_of_birth


class Worker(Human):

    @abstractmethod
    def do_job(self):
        pass


class Client(Human):

    def __init__(self, name: str, sex: str, year_of_birth: int,
                 hair_length: int, nail_length: int, nail_color: Optional[int] = None):

        super().__init__(name=name, sex=sex, year_of_birth=year_of_birth)

        if hair_length < 0:
            raise ValueError('Incorrect hair_length! It should be non-negative number')
        if nail_length < 0:
            raise ValueError('Incorrect nail_length! It should be non-negative number')

        self.hair_length = hair_length
        self.nail_length = nail_length
        self.nail_color = nail_color


class Manicurist(Worker):

    def __init__(self, name: str, sex: str, year_of_birth: int,
                 available_colors: List[str] = ['red', 'purple', 'green']):
        super().__init__(name=name, sex=sex, year_of_birth=year_of_birth)

        self.available_colors = available_colors

    def do_job(self, client):
        if client.nail_length == 0:
            raise ValueError("This client hasn't nails!")
        else:
            client.nail_length -= 1
            if client.nail_length == 0:
                client.nail_color = None
            else:
                client.nail_color = random.choice(self.available_colors)


class Hairdresser(Worker):

    def __init__(self, name: str, sex: str, year_of_birth: int):
        super().__init__(name=name, sex=sex, year_of_birth=year_of_birth)

    def do_job(self, client):
        if client.hair_length == 0:
            raise NameError('Hair are too short!')
        else:
            client.hair_length -= 1


class Barber(Hairdresser):

    def __init__(self, name: str, sex: str, year_of_birth: int):
        super().__init__(name, sex, year_of_birth)

    def do_job(self, client):
        if client._sex == 'F':
            raise ValueError('I only work with men!')
        super().do_job(client=client)


neo = Client(
  name="Neo", sex="M", year_of_birth=1964,
  hair_length=10, nail_length=2
)
trinity = Client(
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