from django.http import HttpResponse, HttpResponseNotFound

def handler404(request,exception):
    return HttpResponseNotFound('<h1>404: Page not found!</h1>')

