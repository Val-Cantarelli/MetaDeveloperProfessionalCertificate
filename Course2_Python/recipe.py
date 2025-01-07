'''Vamos criar a classe, instanciá-las com variáveis e métodos
e também descobrir como referenciá-los em instâncias separadas  para produzir resultados diferentes.

class Recipe():
    # new - cria e devolve um objeto vazio 
    def __new__(cls) -> Self: #cls: Ele atua como um espaço reservado para passar a classe como seu primeiro argumento, que será usado para criar o novo objeto vazio.
        pass
    
    # init - inicializa os atributos do objeto criado. É semelhante ao construtor de outras linguagens. usa o novo objeto como seu primeiro argumento.
    #A palavra-chave self aqui é outra convenção. Embora não tenha uma função específica, serve como um espaço reservado para autorreferência pelo objeto da instância.
    def __init__(self) -> None:
        pass
'''
class Recipe():
   
   
   
   def __init__(self, dish, items, time) -> None:
      
      self.dish = dish
      self.items = items
      self.time = time
      
   def contents(self):
      print("The " + self.dish + " has " + "," .join(self.items) + " and takes "+\
         str(self.time) + " minutes to prepare!")

pizza = Recipe("Pizza", ["cheese", "bread", "tomato"], 45 )
pasta = Recipe("Pasta", ["penne", "souce"], 55 )
pestoFetuccini = Recipe("Pesto Fetuccini", ["fettuccini", "fresh pesto","tomatos", "basil"], 30)

print( pizza.dish, pizza.items, pizza.contents())
print(pasta.items)
print(pestoFetuccini.contents())