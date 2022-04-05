from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index_view(request):
    return HttpResponse("hello,hhhh")


def mydate(request, year, month, day):
    return HttpResponse(str(year) + '/' + str(month) + '/' + str(day))


def myyear(request, year):
    return render(request, 'myyear.html')


def myyear_dict(request, year, month):
    return render(request, 'myyear_dict.html', {'month': month})