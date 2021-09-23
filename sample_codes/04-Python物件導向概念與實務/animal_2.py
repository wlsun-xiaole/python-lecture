class Animal():
    species = 'animal'
    def __init__(self, species):
        self.species = species    
    
    def intro(self):
        print('I am an', self.species)

