from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Bienvenido a este Proyecto")