from django.shortcuts import render

# Create your views here.
def landing_view(request):
    return render(request, 'pages/landing.html')

def about_view(request):
    return render(request, 'pages/about.html')