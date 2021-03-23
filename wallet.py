class wallet:
    def __init__(self, dollars, cents):
        self.dollars = dollars + cents // 100
        self.cents = cents % 100
    def __add__(self, other):  
        x = self.dollars + other.dollars
        y = self.cents + other.cents
        return wallet(x, y)
    def __mul__(self, n):
        x = self.dollars * n
        y = self.cents * n
        return wallet(x, y)
    def __truediv__(self, n):
        x = (self.dollars * 100 + self.cents) // n
        return wallet(0, x)
    def __str__(self):
        return f'{self.dollars} dollars and {self.cents} cents'
w1 = wallet(10, 53)
w2 = 4
print(w1*w2)
print(w1 / w2)