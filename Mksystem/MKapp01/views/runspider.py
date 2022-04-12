from django.shortcuts import *
from MKapp01.views import run


def runspider(request):

    return render(request, 'runspider.html')