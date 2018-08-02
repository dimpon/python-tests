class A:
    def __private(self):
        print("Это метод класса A")

    def public(self):
        self.__private()



class B(A):
    def dosomefun(self):
        self.public()

    def public(self):
        print("Это метод класса B")
         

def getA(a):
    a.public()



a = A()
a.public()
a._A__private()

print("====")

b = B()
b.dosomefun()
b.public()
b._A__private()

print("====")

getA(a)
getA(b)

