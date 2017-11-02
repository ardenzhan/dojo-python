from animal import Animal

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self
    
    def displayHealth(self):
        super(Dragon, self).displayHealth()
        print "I am a Dragon"
        return self

dragon1 = Dragon("Draggy")
dragon1.displayHealth()
dragon1.fly()
dragon1.displayHealth()
dragon1.walk()
dragon1.displayHealth()