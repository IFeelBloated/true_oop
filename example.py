import true_oop
true_oop.symbols = globals()

def f(self):
    self.g()
    y = self.x + self.x
    print(y)
    
def g1(self):
    self.x = self.x + 1
    
def g2(self):
    self.x = 'hello ' + self.x + ' '
    
def add(self, rhs):
    return self.x + rhs.x
    
obj1 = true_oop.obj()
obj2 = true_oop.obj()
obj3 = true_oop.obj()

obj1.x = 0  #dynamically binds a data member to obj1
obj1.g = g1 #dynamically binds a member function to obj1

obj2.x = 'world'
obj2.g = g2

obj3.x = 1
obj3.__add__ = add #dynamically overloads operator+ for obj3

obj1.f() #UFCS, prints 2
obj2.f() #UFCS, prints 'hello world hello world'
print(obj3 + obj1) #prints 2
