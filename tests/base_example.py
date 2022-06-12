from unitazIO import Poop

poop = Poop(poop_times=5)
poop.boom(timer=1)

'''
Вывод:

              БУУМ!
         БУУМ!
            ТЫ ПРОТО В УДАРЕ!
                  ТЫ ПРОСТО В УДАРЕ!
               БУУМ!

Я все смыл, и на всякий случай вызвал сантехника.
'''

poop = Poop(poop_times=15)
poop.boom(timer=1)

'''
Вывод:

                           ТЫ ПРОТО В УДАРЕ!
                   ТЫ ПРОТО В УДАРЕ!
                              ТЫ ПРОТО В УДАРЕ!
                  ТЫ ПРОТО В УДАРЕ!
                 ТЫ ПРОТО В УДАРЕ!
Traceback (most recent call last):
  File "tests.py", line 19, in <module>
    poop.boom(timer=1)
  File "pooper.py", line 24, in boom
    self.iteratively_pooped()
  File "unitaz.py", line 10, in iteratively_pooped
    raise UnitazIsFull('Пришло время смыть за собой! Вы покакали уже 10 раз подряд!')
unitazIO.pooping_exceptions.UnitazIsFull: Пришло время смыть за собой! Вы покакали уже 10 раз подряд!
'''
