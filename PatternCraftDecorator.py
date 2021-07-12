class Marine:
    def __init__(self, damage, armor):
        self.damage = damage
        self.armor = armor


class Marine_weapon_upgrade(Marine):
    def __init__(self, marine):
        self.damage = marine.damage + 1
        self.armor = marine.armor


class Marine_armor_upgrade(Marine):
    def __init__(self, marine):
        self.armor = marine.armor + 1
        self.damage = marine.damage
