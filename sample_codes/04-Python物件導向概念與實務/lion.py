from animal_2 import Animal

class Lion(Animal):
    def __init__(self):
        super().__init__('Lion')
    def intro(self):
        print('I am a', self.species)
    def roar(self):
        print('吼~')
