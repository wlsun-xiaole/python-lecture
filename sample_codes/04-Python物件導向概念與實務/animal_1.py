class Animal():
    species = 'animal'
    def __init__(self, name):
        self.species = name
        self.weight = 80
        self.height = 100
    def intro(self):
        print('I am an', self.species)


class Dog(Animal):
    def __init__(self):
        super().__init__("Dog")
        self.food  = 'meat'
    def intro(self):
        print('I am a', self.species)

    def roar(self):
        print('ghkkg')

a = Dog()
a.roar()

