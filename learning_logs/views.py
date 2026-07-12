from django.shortcuts import render

def index(request):
    """A página inicial do Learning Log."""

    return render(request, 'index.html')
