from django.shortcuts import render
from .models import Quote


# Create your views here.
def quotes_list(request):
    quotes = Quote.objects.all().order_by('created_at')
    return render(request, 'quotes/quotes_list.html', {'quotes': quotes})
