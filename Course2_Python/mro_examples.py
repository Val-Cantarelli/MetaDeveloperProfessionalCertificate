'''# Quando eu chamo a instancia de C - se não houver nada dentro dela - ela procura em B e depois em A 
# nessa ordem porque foi posta assim class C(B,A) se fosse class C(A,B) ele procuraria em  A e depois em B

# Example 1
class A:
   def a(self):
       return "Function inside A"

class B:
    def a(self):
        return "Function inside B"

class C(B,A):
    pass

# Driver code
c = C()
print(c.a())
'''



'''class A:
    def c(self):
        return "Function inside A"

class B(A):
    def c(self):
        return "Function inside B"

class C(A,B):
    pass

class D(C):
    pass

d = D()
print(d.c)'''