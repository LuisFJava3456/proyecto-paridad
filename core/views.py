from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def verificar_paridad(request):
    if request.method == 'POST':
        numero = int(request.POST.get('numero'))
        resultado = 'par' if numero % 2 == 0 else 'impar'
        return JsonResponse({'resultado': resultado})