import { Poop } from './unitazTS';

const poop = new Poop(5);
poop.boom(1);

/*
Вывод:
   
                               ТЫ ПРОСТО В УДАРЕ!
                              ТЫ ПРОСТО В УДАРЕ!
       БУУМ!
                          БУУМ!
             #ТАКМНОГО!
*/

const poop2 = new Poop(15);
poop2.boom(1);

/*
                        ТЫ ПРОСТО В УДАРЕ!
                           #ТАКМНОГО!
                  БУУМ!
                      БУУМ!
                  #ТАКМНОГО!
      БУУМ!
                          #ТАКМНОГО!
                        #ТАКМНОГО!
               ТЫ ПРОСТО В УДАРЕ!
     ТЫ ПРОСТО В УДАРЕ!
                        БУУМ!
         БУУМ!
                        ТЫ ПРОСТО В УДАРЕ!
         БУУМ!
      #ТАКМНОГО!
unitaz.js:10
            throw new Error('Пришло время смыть за собой! Вы покакали уже 10 раз подряд!');
            ^

Error: Пришло время смыть за собой! Вы покакали уже 10 раз подряд!
    at Poop.iterativelyPooped (unitaz.js:10:19)
    at Timeout.wrapper [as _onTimeout] (pooper.js:28:18)
    at listOnTimeout (internal/timers.js:555:17)
    at processTimers (internal/timers.js:498:7)
npm ERR! Test failed.  See above for more details.
*/

