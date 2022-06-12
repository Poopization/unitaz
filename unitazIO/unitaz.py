from .pooping_exceptions import UnitazIsFull


class Unitaz:
    pooped_times = 0

    @classmethod
    def iteratively_pooped(cls) -> None:
        if cls.pooped_times == 10:
            raise UnitazIsFull('Пришло время смыть за собой!')

        cls.pooped_times += 1
