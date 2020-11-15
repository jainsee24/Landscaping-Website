from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import *
def index(request):
	return render(request,'blog/index.html')
def handler404(request,exception):
    return render(request,'blog/index.html')


def handler500(request):
    return render(request,'blog/index.html')