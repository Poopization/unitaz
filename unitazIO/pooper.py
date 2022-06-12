import time
import random

from .unitaz import Unitaz
from .pooping_exceptions import TooMuchTimeForPooping


class Poop(Unitaz):
    @staticmethod
    def spaces() -> str:
        return ' ' * random.randint(5, 30)

    @classmethod
    def boom(cls, timer: int) -> None:
        if timer not in range(1, 101):
            raise TooMuchTimeForPooping('You can\'t poop lower than 1 second and more than 100.')

        words_dict = ['BOOM!', 'YOU ARE HEADLESS!', 'SO MUCH!']
        
        while True:
            cls.iteratively_pooped()
            time.sleep(5)
            print(f'{cls.spaces()} {random.choice(words_dict)}')
