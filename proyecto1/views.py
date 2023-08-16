from django.http import HttpResponse 


def print_bienvenida(request):
    return HttpResponse ("Bienvenido a mi primer blog")