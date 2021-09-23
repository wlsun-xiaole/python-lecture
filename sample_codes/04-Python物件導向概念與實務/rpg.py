class Character():
    Name = ""
    HealthPoint = 100
    MagicPoint = 10
    ATK = 0
    DEF = 0
    def __init__(self, name):
        self.Name = name
    def attack(self):
        atk_res = 0
        return atk_point
    def defence(self, atk_point):
        def_res = atk_point
        return def_res
    def updateHP(self, def_res):
        self.HealthPoint -= def_res
    def updateMP(self, atk_point):
        self.MagicPoint -= atk_point
    def info(self):
        print('[',self.Name,'] HP=', self.HealthPoint, 'MP=', self.MagicPoint)
class Knight(Character):
    Legends = ""
    def use_sword(self, atk_raw):
        return atk_raw + 10

class Wizard(Character):
    Attributes = []
    def use_magic(self, atk_raw):
        return atk_raw + 5

class Rogue(Character):
    Items = {}
    def use_dart(self, atk_raw):
        return atk_raw + 7
