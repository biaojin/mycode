from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage':"I am bold font from the context"}
    return render(request, 'rango/index.html', context_dict)

def about(request):
        return HttpResponse("Rango says about here<br/><a href='/rango/'>Index</a>")
# Create your views here.
