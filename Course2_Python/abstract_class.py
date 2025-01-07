'''
Veículo é uma classe abstrata pq a ideia de veículo é abstrata. Você não cria um veículo e, sim, um carro, um barco ou 
um trem.
São implementadas de duas formas:
    1. os métodos devem ser implementados nas classes filhas(porque as abstratas não tem implement própria)
from abc import ABC, abstractmethod 
class VeiculoClass(ABC):
    @abstractmethod
    def tornOnEngine(self):
        pass
    
    2.  super() function 
'''


