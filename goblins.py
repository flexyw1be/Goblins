import random
from prettytable import PrettyTable
from termcolor import colored

NAMES = [
    'Рогнар', 'Гайрил', 'Харвельд',
    'Бонк', 'Бинк', 'Дигидим'
]


class Goblin:
    def __init__(self):
        self.name = random.choice(NAMES)
        self.hp = random.randint(10, 20) * 10
        self.dmg = random.randint(7, 12)
        self.crit_chance = random.randrange(5, 30 + 1, 5)
        self.crit_mult = 2

    def __repr__(self):
        return f'<Goblin({self.name}, {self.hp}, {self.dmg}, {self.crit_mult})>'

    def __str__(self):
        return f'Имя гоблина: {self.name}.\n' \
               f'ОЗ: {self.hp}, урон: {self.dmg}' \
               f'Шанс крита: {self.crit_chance}'

    def attack_dmg(self):
        dice = random.randint(1, 6)
        dmg = self.dmg + dice
        crit_chance = random.randint(1, 100)
        crit = False
        if crit_chance <= self.crit_chance:
            print(colored('Крит!', 'red'))
            crit = True
            dmg *= self.crit_mult
        return dmg, crit

    def is_awake(self):
        return self.hp > 0

    def get_dmg(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

    def dodge(self):
        crit_chance = random.randint(1, 100)
        return crit_chance <= self.crit_chance

    def get_base_dmg(self):
        return self.dmg


class BattleOfGoblins2000:
    def __init__(self):
        self.g1 = Goblin()
        self.g2 = Goblin()

        self.turn = 0

    def run(self):
        self.turn = 0
        print(self.print_table())
        print()
        while self.g1.is_awake() and self.g2.is_awake():
            self.turn += 1
            print(f'Раунд: {self.turn}')
            coin = random.randint(1, 2)
            if coin == 1:
                self.attack(self.g1, self.g2)
                self.attack(self.g2, self.g1)
            else:
                self.attack(self.g2, self.g1)
                self.attack(self.g1, self.g2)
            print()
        if self.g1.is_awake():
            print(f'{self.g1.name} сторожит')
            print(f'{self.g2.name} уснул')
        else:
            print(f'{self.g2.name} сторожит')
            print(f'{self.g1.name} уснул')

    def attack(self, attacker, defender):
        if not attacker.is_awake():
            return
        dmg, crit = attacker.attack_dmg()
        if defender.dodge():
            dmg = defender.get_base_dmg()
            attacker.get_dmg(dmg)
            print(colored(f'{defender.name} уклонился и контр-ударил {attacker.name}', 'red'), \
                  colored(f' с силой {dmg}', 'red'), sep='')
            print(f'У {attacker.name} осталось {attacker.hp} ОЗ')
        else:
            defender.get_dmg(dmg)
            print(f'{attacker.name} ударил {defender.name}' \
                  f' с силой {dmg}')
            print(f'У {defender.name} осталось {defender.hp} ОЗ')

    def print_table(self):
        mytable = PrettyTable()
        mytable.field_names = ["Имя", "Урон", "ОЗ", "Шанс крита", "Множитель урона"]
        mytable.add_rows([
            [self.g1.name, self.g1.dmg, self.g1.hp, self.g1.crit_chance, self.g1.crit_mult],
            [self.g2.name, self.g2.dmg, self.g2.hp, self.g2.crit_chance, self.g2.crit_mult]
        ])
        return mytable


if __name__ == '__main__':
    game = BattleOfGoblins2000()
    game.run()

