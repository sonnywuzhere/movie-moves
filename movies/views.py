from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'movies': ['Anne of Green Gables', 'Princess Switch', 'Hidden Figures', 'High School Musical', 'Fly Me To The Moon']
    }
    return render(request, "movies/index.html", context)

def about(request):
    return render(request, "movies/about.html", {})
