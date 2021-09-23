class Animal():
    species = 'animal'
    def __init__(self, species):
        self.species = species    
    
    def intro(self):
        print('I am an', self.species)

class Lion(Animal):
    def __init__(self):
        super().__init__('Lion')
    def intro(self):
        print('I am a', self.species)
    def roar(self):
        print('吼~')
