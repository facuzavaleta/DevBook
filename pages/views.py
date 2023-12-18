from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def landing_view(request):
    data = {'message': '¡Hola desde el servidor!'}

    if request.GET.get('ajax_request'):
        # Esta es una solicitud AJAX
        return JsonResponse(data)
    else:
        # Esta no es una solicitud AJAX
        return render(request, 'pages/landing.html')
    
def about_view(request):
    return render(request, 'pages/about.html')