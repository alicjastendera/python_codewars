class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
    __repr__=__str__


def declare_winner(fighter1, fighter2, first_attacker):
    attacker = fighter1 if first_attacker == fighter1.name else fighter2
    defender = fighter2 if first_attacker != fighter2.name else fighter1

    while attacker.health > 0 and defender.health > 0:
        defender.health = defender.health - attacker.damage_per_attack
        if defender.health > 0 :
            attacker.health = attacker.health - defender.damage_per_attack

    return attacker.name if attacker.health > defender.health else defender.name


declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Lew")