from django.shortcuts import render


tasks = ["zesrac sie w gacie", "zeszczac"]

# Create your views here.

def index(request):
    return render(request, "tasks\index.html", {
        "tasks": tasks
    })