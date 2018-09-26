import animal

class Penguin(animal.Animal):
    def __init__(self):
        super().__init__()
        print('I am a penguin')
        self.energy = 100

    def move(self):
        self.energy -= 5
        print('I am sliding!')

class Eagle(animal.Animal):
    def __init__(self):
        super().__init__()
        print('I am an eagle!')
        self.energy = 20
    def move(self):
        if self.energy > 0:
            self.energy -= 20
            print('I am flying to the sea!')
        else: 
            print('I am too tired to fly...')
    def say_hi(self):
        print('shrieeeeeek!')
