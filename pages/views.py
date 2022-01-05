from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic import TemplateView

# Create your views here.

def homePageView(request):

    return render(request,'home.html',{})

class ClassView(TemplateView):

    template_name='home.html'  


def aboutView(request):
    return render(request,'about.html',{})      