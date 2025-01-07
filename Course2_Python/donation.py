# Primeiro modo
from abc import ABC, abstractmethod 
class Employee(ABC):
    '''
    @abstractmethod É um ¨decorator¨: são funções que modificam outras funções ou métodos. 
    Eles são usados para modificar o comportamento de uma função ou método de forma declarativa, 
    adicionando funcionalidades adicionais a eles. Aqui é usado para sinalizar que o método deve ser 
    implementado por todas as subclasses concretas'''
    
    def donate(self):
        pass
    
class Donation(Employee):
    def donate(self):
        return input("How much would you like to donate: ")


# Not finished, just an example how to implement       