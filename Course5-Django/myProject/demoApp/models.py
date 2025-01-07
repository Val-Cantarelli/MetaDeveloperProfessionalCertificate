from django.db import models 
class Customer(models.Model): 
    name = models.CharField(max_length=255) 
    
    def __str__(self) -> str:
        return self.name

class Vehicle(models.Model): 
    name = models.CharField(max_length=255) 
    customer = models.ForeignKey( 
        Customer, 
        on_delete=models.CASCADE, 
        related_name='Vehicle' 
    ) 
    # Vai retornar o nome, ao invés do objeto
    def __str__(self) -> str:
        return self.name