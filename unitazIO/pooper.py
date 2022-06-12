import time
import random

from .unitaz import Unitaz
from .pooping_exceptions import TooMuchTimeForPooping


class Poop(Unitaz):
    def __init__(self, poop_times: int, flush_after_pooping: bool = False) -> None:
        self.poop_times = poop_times
        self.flush_after_pooping = flush_after_pooping


    def boom(self, timer: int) -> None:
        if timer not in range(1, 1001):
            raise TooMuchTimeForPooping('Вы не можете какать меньше 1 или дольше 1000 секунд.')

        words_dict = ['БУУМ!', 'ТЫ ПРОСТО В УДАРЕ!', '#ТАКМНОГО!']
        
        for _ in range(self.poop_times):
            self.iteratively_pooped()
            time.sleep(timer)
            print(f'{" " * random.randint(5, 30)} {random.choice(words_dict)}')

        if self.flush_after_pooping:
            print('\nЯ все смыл, и на всякий случай вызвал сантехника.')
