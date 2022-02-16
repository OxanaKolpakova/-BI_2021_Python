class Fruit(object):

    def __init__(self, color, taste, mellowness):
        self.color = color
        self.taste = taste
        self.mellowness = mellowness

    def test(self):
        if 5 < self.mellowness <= 10:
            return("Ready to be eaten")
        if self.mellowness > 10:
            return("I'm rotten")
        else:
            return("Wait")

    def after_a_while(self):
        self.mellowness += 1

if __name__ == "__main__":
    apple = Fruit("red", "sweet", 10)
    print(apple.color)
    print(apple.test())
    print(apple.after_a_while())
    print(apple.mellowness)
    print(apple.test())
