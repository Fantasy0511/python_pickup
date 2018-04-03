class Bird:
    def __init__(self):
        self.hungry=True
    def eat(self):
        if self.hungry==True:
            print('我饿了')
            self.hungry=False
        else:
            print('我不饿')
bird=Bird()
bird.eat()
