import random
class Character():
    Name = ""
    HealthPoint = 100
    MagicPoint = 10
    ATK = 0
    DEF = 0
    def __init__(self, name):
        self.Name = name
    def attack(self):
        atk_res = random.randrange(self.ATK)
        return atk_point
    def defense(self, atk_point):
        def_res = max(0, atk_point - random.randrange(self.DEF))
        return def_res
    def updateHP(self, def_res):
        self.HealthPoint -= def_res
    def updateMP(self, atk_point):
        self.MagicPoint -= atk_point
    def showStatus(self):
        print("[",self.Name,"] HP:",self.HealthPoint, "MP", self.MagicPoint)

class Knight(Character):
    Legends = ""
    def __init__(self, name):
        super().__init__(name)
        self.HealthPoint = 100
        self.MagicPoint = 50
        self.ATK = 25
        self.DEF = 10
    def attack(self):
        if self.MagicPoint > 0:
            atk_res = random.randrange(self.ATK+10)
            self.updateMP(atk_res)
        else:
            atk_res = random.randrange(self.ATK)
        return atk_res

class Wizard(Character):
    Attributes = []
    def __init__(self, name):
        super().__init__(name)
        self.HealthPoint = 50
        self.MagicPoint = 200
        self.ATK = 5
        self.DEF = 5
    def attack(self):
        if self.MagicPoint > 0:
            atk_res = random.randrange(self.ATK+30)
            self.updateMP(atk_res)
        else:
            atk_res = random.randrange(self.ATK)
        return atk_res

class Rogue(Character):
    Items = {}
    def __init__(self, name):
        super().__init__(name)
        self.HealthPoint = 70
        self.MagicPoint = 100
        self.ATK = 15
        self.DEF = 30
    def attack(self):
        if self.MagicPoint > 0:
            atk_res = random.randrange(self.ATK+15)
            self.updateMP(atk_res)
        else:
            atk_res = random.randrange(self.ATK)
        return atk_res
