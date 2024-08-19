from django.http import HttpResponse 
from django.template import loader 
from .models import data_application


# Create your views here.

def webapplication(request): 
    data_processing=data_application.objects.all().values()
    template=loader.get_template('access.html')
    context= { 
             'data_processing':data_processing
             }
    return HttpResponse(template.render(context,request))   

def details(request,id): 
    mymember=data_application.objects.get(id=id)
    template=loader.get_template('details.html')
    context={ 
             'mymember': mymember
             }
    return HttpResponse(template.render(context,request ))

def main(request): 
    template=loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request): 
    template=loader.get_template('template.html')
    context= { 
              'fruits':['apple','orange','bannana']
              }
    return HttpResponse(template.render(context,request))