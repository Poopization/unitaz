from unitazIO import Poop

Poop.boom(2)


'''
Output:

              YOU ARE HEADLESS!
         SO MUCH!
                      BOOM!
              YOU ARE HEADLESS!
         SO MUCH!
                 BOOM!
       YOU ARE HEADLESS!
                          SO MUCH!
                             YOU ARE HEADLESS!
                         YOU ARE HEADLESS!
Traceback (most recent call last):
  File "tests.py", line 3, in <module>
    Poop.boom(2)
  File "pooper.py", line 21, in boom
    cls.iteratively_pooped()
  File "unitaz.py", line 10, in iteratively_pooped
    raise UnitazIsFull('Пришло время смыть за собой!')
unitazIO.pooping_exceptions.UnitazIsFull: Пришло время смыть за собой!
'''
