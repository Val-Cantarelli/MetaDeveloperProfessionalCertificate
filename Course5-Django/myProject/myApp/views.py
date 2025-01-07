
from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from datetime import datetime
from django.urls import reverse
from myApp.forms import  LogForm
from django.contrib.auth.decorators import login_required 
from django.template import loader
from .models import Menu
from django.views.generic.base import TemplateView
    

def say_hello(request):
    return HttpResponse("Hello!")

def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def display_menu_item(request):
    text = """<h1 style="color: #F4CE14;"> This is little lemon again</h1>"""
    return HttpResponse(text)

def pathview(request,name,id):
    return HttpResponse("Name: {} UserID: {}".format(name,id))

#@login_required  Esse overide exige que somente usr logados possam acessar a informacao
def info_movies(request, movie):
    items = {
        'A_Viagem_de_Chihiro':'"A Viagem de Chihiro" é uma animação japonesa +\
        dirigida por Hayao Miyazaki. A história segue uma jovem chamada Chihiro,+\
        que, ao se mudar com seus pais para uma nova cidade, acaba entrando em um+\
        mundo mágico habitado por espíritos e criaturas fantásticas.'
    }
    description = items[movie]
    return HttpResponse(f"<h2>{movie} </h2>" + description)
    

def myview(request): 
    # Quando alguém quiser acessar: my/myview/, vai ser redirecionado para newApp/login/
    return HttpResponsePermanentRedirect(reverse('newApp:login'))


def form_view(request):

    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'home.html',context)


    about_content = {'about':"Based in Chicado, blablabla!"}
    return render(request,'about.html',about_content)

def menu_by_id(request):
    newmenu = Menu.objects.all()
    newmenu_dict={'menu': newmenu}
    return render(request,'menu_cards.html', newmenu_dict)
    
    
def home(request): 
    return render(request, "home.html", {}) 

def about(request): 
    return render(request, "about.html", {}) 

def menu(request): 
    return render(request, "menu.html", {}) 

 

class IndexView (TemplateView): 
    template_name = 'index.html' 