import { Unitaz } from './unitaz';

export class Poop extends Unitaz {
    private poopingTimes: number;
    private flushAfterPooping: boolean = false;

    constructor(poopingTimes: number, flushAfterPooping?: boolean) {
        super();

        this.poopingTimes = poopingTimes;
        
        if (flushAfterPooping) {
            this.flushAfterPooping = true;
        }
    }

    private randomNumber(from: number, to: number): number {
        const min = Math.ceil(from);
        const max = Math.floor(to);
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    private spaces(): string {
        return ' '.repeat(this.randomNumber(5, 30));
    }

    public boom(timer: number): any {
        if (timer <= 0 || timer >= 101) {
            throw new Error('Вы не можете какать меньше 1 или дольше 1000 секунд.');
        }

        const wordsDict = ['БУУМ!', 'ТЫ ПРОСТО В УДАРЕ!', '#ТАКМНОГО!'];

        const wrapper = () => {
            this.iterativelyPooped();

            if (this.poopedTimes === this.poopingTimes) {
                return;
            }

            const randomIndex = Math.floor(Math.random() * wordsDict.length);
            const word = wordsDict[randomIndex];
            console.log(this.spaces() + word);
        };
        
        setInterval(wrapper, timer * 1000);
        
        // За каким-то хуем это выполняется раньше интервала...
        if (this.flushAfterPooping) {
            console.log('\nЯ все смыл, и на всякий случай вызвал сантехника.');
        }
    }
}
