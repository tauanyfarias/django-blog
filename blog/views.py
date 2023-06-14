from django.shortcuts import render

#inclui a classe httpresponde.
from django.http import HttpResponse

#define uma function view chamada index.
def index(request):
    return HttResponse('Olá Django - index')

#define uma function view chamada ola
def ola(request):
    return HttpResponse('Olá Django')


