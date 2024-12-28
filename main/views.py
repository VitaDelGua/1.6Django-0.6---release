import datetime

from django.shortcuts import render

from main.forms import CalculateForm
from main.models import CalculateHistory


def index_page(request):
    context = {
        "author": "Admin",
        "count_pages": 3
    }
    return render(request, "index.html", context)


def time_page(request):
    context = dict()
    context['date'] = datetime.datetime.now()
    return render(request, 'time.html', context)


def calculate_page(request):
    context = dict()
    if request.method == "POST":
        calc_form = CalculateForm(request.POST)
        if calc_form.is_valid():
            a = calc_form.cleaned_data["a"]
            b = calc_form.cleaned_data["b"]
            c = a + b
            context["a"] = a
            context["b"] = b
            context["c"] = c
            item = CalculateHistory(a=a, b=b, result=c, created_at=datetime.datetime.now())
            item.save()
    else:
        calc_form = CalculateForm()
    context["calc_form"] = calc_form
    context["history"] = CalculateHistory.objects.all()
    return render(request, "calculate.html", context)