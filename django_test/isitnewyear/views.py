from django.shortcuts import render

from datetime import datetime
# Create your views here.

def index(request):
    now: datetime = datetime.now()
    return render(request, "isitnewyear\index.html", {
        "newyear": now.month == 1 and now.day == 1
    })