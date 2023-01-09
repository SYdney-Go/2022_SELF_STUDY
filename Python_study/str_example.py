class Simple:
    def __init__(self, a, b, c):
        self.A = a
        self.B = b
        self.C = c
    
    def __str__(self):
        return self.__init__

a = 1
b = 2
c = 3
s = Simple(a, b, c)

print(s.__str__())