from django.shortcuts import render
from .forms import ProfesorForm
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def home(request):
    form=ProfesorForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,'Registrado correctamente!')
        return HttpResponseRedirect('/')
    contexto={'form':form}
    return render(request, "home.html",contexto)