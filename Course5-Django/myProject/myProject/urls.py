"""
O mecanismo  de URL do Django é equivalente ao controlador na arquitetura MVC.
O módulo urls.py na pasta do pacote do projeto Django atua como o controller.
Ele define os padrões de URL. Cada padrão de URL é mapeado com uma função de 
visualização a ser invocada quando o URL de solicitação do cliente corresponde a ele.
_________________________________
Esse arquivo mapeia os urls de apps, se houverem.
"""

from django.contrib import admin 
from django.urls import  path, include


urlpatterns = [   
    path('admin/', admin.site.urls, name='admin'), 
    
    # All path from myApp was included to project level - se eu quiser localhost/about, tenho que colocar o path individualmente
    path('myApp/', include('myApp.urls', namespace='myApp')),
    
]

handler404 = 'myProject.views.handler404'


