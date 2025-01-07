class Casa:
    num_rooms = 5
    bathrooms = 2
    def cost_evaluation(self, str):# o self é uma convençao necessária ao python
        print(self.num_rooms,str)
        pass
'''Você pode chamar os atributos ou diretamente ou instanciando objetos dessa classe'''
        
      
instOne = Casa()
instTwo = Casa()
instThree = Casa()
'''Alterar o valor do atributo da classe(não bom)'''
Casa.bathrooms = 8
print(Casa.bathrooms)

'''Criar instância do atributo da classe e então sim alterar o valor'''
instThree.bathrooms = 3
print(instThree.bathrooms)

'''O valor ainda sai como 8 porque mexemos no atributo da classe e isso afetou todas as instâncias da classe'''
print(instTwo.bathrooms)

print(instOne.cost_evaluation("oi"))


''' Another exemplo
class MyClass:
    a = 5
    
    def hello(self):# preciso sinalizar 
        print("Hello, World!!!")


inst1 = MyClass()
print(MyClass.a)
print(inst1.a)# consigo chamar a propriedade fácil através da instância
print(inst1.hello())# no método é diferente
# o "none"da saída é pq não há valor de retorno na function


Exemple:

bravo = 3
# b = B() nessa posição geraria um erro no output porque não foi definido. Se colocar depois da classe, ok.
class B:
    bravo = 5
    print("Inside class B")
c = B()
b = B()
print(b.bravo)

# se atentar ao escopos de atributos/lembrar encapsulamento

'''