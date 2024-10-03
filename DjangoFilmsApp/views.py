from django.shortcuts import render
from .models import Films  # Asegúrate de importar el modelo Films
from django.http import HttpResponse

def films_list(request):
    # Obtén todas las películas activas
    
    films = Films.objects.filter(active=True)
    films = Films.objects.all()  # Obtiene todos los registros de la tabla `films`
    print(films)

    if films.exists():
       return render(request, 'films_list.html', {'films': films})
    else:
        return HttpResponse("HOLA ALEXANDER")