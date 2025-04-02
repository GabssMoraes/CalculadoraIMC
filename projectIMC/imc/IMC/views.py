from django.shortcuts import render
import requests

# Create your views here.
def imc(request):
    if request.method == "POST":
        peso = request.POST["peso"]
        altura = request.POST["altura"]

        calculoIMC = ((float (peso)) / (float(altura) ** 2))

        try:
            if calculoIMC < 18.5:
                resultado = "Abaixo do peso"
            elif 18.5 <= calculoIMC < 24.9:
                resultado = "Peso Normal"
            elif 25 <= calculoIMC < 29.9:
                resultado = "Sobrepeso"
            else:
                resultado = "Obesidade"

            return render(request, 'IMC/imc.html',{
                'resultado' : resultado,
                'peso' : peso,
                'altura' : altura,
            })
        except ValueError:
            return render(request,'IMC/imc.html',{
                'error': 'Valores invalidos!'
            })
        
    return render(request, 'IMC/imc.html')