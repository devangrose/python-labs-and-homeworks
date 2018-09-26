class Animal:
    def __init__(self):
        print('I am coming to life!')
        self.energy = 50

    def eat(self, amount):
        self.energy = self.energy + amount

    def move(self):
        self.energy -= 10
        print('I am running!')

    def get_status (self):
        print('My energy level is: {}'.format(self.energy))
        if self.energy > 100:
            print('I\'m feeling stuffed!')
        elif self.energy > 50:
            print('I\'m happily full')
        elif self.energy > 0:
            print('I\'m getting hungry')
        else: 
            print('I\'m starving!')
    def say_hi (self):
        print('Meep')
