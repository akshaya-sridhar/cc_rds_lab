from django.shortcuts import render, redirect
from .forms import CovidForm
from .models import *

# Create your views here.
def indexform(request):
    form = CovidForm()
    if request.method == 'POST':
        form = CovidForm(request.POST)
        if form.is_valid():
            form.save()
            # form = CovidForm()
            redirect('/covid_dash')
    context = {'form': form}
    return render(request, 'index.html', context)

def results(request):
    obj = covid_19.objects.all()
    
    return render(request, 'results.html', {'obj':obj})