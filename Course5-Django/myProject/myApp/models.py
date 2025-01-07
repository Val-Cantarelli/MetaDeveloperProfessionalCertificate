from django.db import models


class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.menu_category_name
    
class Menu(models.Model):
    name = models.CharField(max_length=200) 
    price = models.IntegerField(null=True)
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT,default=None, related_name="category_name")
    def __str__(self) -> str:
        return self.name
       
class Logger(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    time_log = models.TimeField()
    def __str__(self) -> str:
        return self.first_name
    
class Reservation(models.Model):
    name = models.CharField(max_length=100,blank=True)
    last_name = models.CharField(max_length=100,blank=True)
    booking_time = models.DateTimeField(auto_now=True)
    
    # Eu quero que lá no admin, no lugar de "Reservation object (2)" apareça o nome da pessoa
    def __str__(self):
        return self.name