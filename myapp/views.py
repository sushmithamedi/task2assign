from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    # dict={'name':'congratulations you are signed in'}
    return render(request,'login.html')

def signin(request):
    return HttpResponse("congratulation you are signed in")