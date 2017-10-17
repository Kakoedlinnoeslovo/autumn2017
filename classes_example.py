class Animal(object):
    def __init__(self, name, paw_count):
        self.name = name
        self.paw_count = paw_count
    
    def describe(self):
        return 'Animal'

class WildAnimal(Animal):
    def describe(self):
        return 'Wild and ' + super(WildAnimal, self).describe()

class DomesticAnimal(Animal):
    def describe(self):
        return 'Domestic'
        
class Dog(WildAnimal, DomesticAnimal):
    def __init__(self, name, breed):
        self.name = name
        self.paw_count = 4
        self.breed = breed
        
    def describe(self):
        return super(Dog, self).describe() + ' and it is {0}'.format(self.breed)
        

dog = Dog('Rex', 'Rex')
wild = WildAnimal('Puff', 5)
print(wild.describe())
print(dog.describe())
