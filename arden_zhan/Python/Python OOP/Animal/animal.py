'''Animal'''

class Animal(object):
    def __init__(self, name = "Animal", health = 100):
        self.name = name
        self.health = health
    
    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print "{}'s health: {}".format(self.name, self.health)
        return self

# animal1 = Animal("Poopy Animal", 100)
# animal1.walk().walk().walk()
# animal1.run().run()
# animal1.displayHealth()
# #animal1.pet().fly()