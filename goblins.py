import random
from termcolor import colored
from prettytable import PrettyTable

NAMES = [
    'Рогнар', 'Гайрил', 'Харвельд',
    'Бонк', 'Бинк', 'Дигидим'
]


class Goblin:
    def __init__(self):
        self.name = random.choice(NAMES)
        self.hp = random.randint(10, 20) * 10
        self.dmg = random.randint(7, 12)
        self.critical_damage = random.randint(10, 20) / 10

    def __repr__(self):
        return f'<Goblin({self.name}, {self.hp}, {self.dmg})>'

    def __str__(self):
        return f'Имя гоблина: {self.name}.\n' \
               f'ОЗ: {self.hp}, урон: {self.dmg}'

    def attack_dmg(self):
        dice = random.randint(1, 6)
        chance_critical_damage = random.randint(0, 4)  # шанс 1/5
        if chance_critical_damage == 1:
            print(colored(f'{self.name} может нанести удар в {self.critical_damage} ' \
                          f'раза сильнее, произошла крит. атака', 'red'))
            return int((self.dmg + dice) * self.critical_damage)
        else:
            return self.dmg + dice

    def is_awake(self):
        return self.hp > 0

    def get_dmg(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0


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
        self.result()

    def attack(self, attacker, defender):
        if not attacker.is_awake():
            return
        chance_to_deflect = random.randint(0, 9)
        if chance_to_deflect != 0:
            dmg = attacker.attack_dmg()
            defender.get_dmg(dmg)
            print(f'{attacker.name} ударил {defender.name}' \
                  f' с силой {dmg}')
            print(f'У {defender.name} осталось {defender.hp} ОЗ')
        else:
            attacker.get_dmg(defender.dmg)
            print(colored(f'{defender.name} отразил удар {attacker.name}', "red"),
                  colored(f' и ударил его с силой {defender.dmg}', "red"), sep='')
            print(f'У {attacker.name} осталось {attacker.hp} ОЗ')

    def result(self):
        if self.g1.is_awake():
            print(f'{self.g2.name} Уснул')
        else:
            print(f'{self.g1.name} Уснул')

    def print_table(self):
        mytable = PrettyTable()
        mytable.field_names = ["Имя", "Урон", "ОЗ", "Множитель урона"]
        mytable.add_rows([
            [self.g1.name, self.g1.dmg, self.g1.hp, self.g1.critical_damage],
            [self.g2.name, self.g2.dmg, self.g2.hp, self.g2.critical_damage]
        ])
        return mytable


if __name__ == '__main__':
    BattleOfGoblins2000().run()
