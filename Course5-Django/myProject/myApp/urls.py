from .views import IndexView
from django.urls import path, re_path 
from . import views # importa o arquivo views onde está a função a ser mapeada

app_name = 'myApp'

urlpatterns = [ 
    path('home/', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'), 
    path('display_date/', views.display_date, name='display_date'),
    path('getuser/<name>/<id>',views.pathview,name='pathview'),
    path('movies/<str:movie>',views.info_movies, name='info_movies'),
    path('menu_item/10',views.display_menu_item, name='display_menu_item'),
    re_path(r'^menu_item/([0-2]{2})/$', views.display_menu_item,),
    path('myview/', views.myview, name='myview'),
    path('form/', views.form_view),    
    path('menu_cards/', views.menu_by_id), 
    path('index/', IndexView.as_view(), name='index'),
] 
# a string vazia é a rota(router) e o segundo argumento é a visualização que tem: 
# o relative path e o nome da fun

