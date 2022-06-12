export class Unitaz {
    private poopedTimes: number = 0;

    protected iterativelyPooped(): any {
        if (this.poopedTimes === 10) {
            throw new Error('Пришло время смыть за собой! Вы покакали уже 10 раз подряд!');
        }

        this.poopedTimes += 1;
    }
}
