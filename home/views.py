from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def handler404(request, exception):
    """ A view to handle 404 errors """
    return render(request, '404.html', status=404)
