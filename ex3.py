import average 
class triangle:
    def __init__(self, a, b, c):
        self.a = min(a, b ,c)
        self.b = average.average(a, b, c)
        self.c = max(a, b, c)
    def correct(self):
        return self.c < self.a+self.b
    def Perimeter(self):
        return self.a + self.b + self.c
    def Surface(self):
        s = self.Perimeter()/2
        return (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5

t = triangle(3, 4 ,5)
print(t.correct())
print(t.Perimeter())
print(t.Surface())