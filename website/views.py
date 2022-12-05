from django.shortcuts import render, redirect
from website.forms import FuncionarioForm


# Create your views here.


def home(request):
    return render(request, "home.html")


def form(request):
    return render(request, "form.html")


def create(request):
    form = FuncionarioForm(request.POST or None)

    if form.is_valid():
        print("Funcionou")
        form.save()
        return redirect("home")
    return render(request, "form.html")
