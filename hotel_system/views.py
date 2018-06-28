from django.http import HttpResponse
from django.shortcuts import render


def WelcomePage(request):
    return render(request, "welcome.html")







