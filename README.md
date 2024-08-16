# Data-Site-
The site is to provide a template for me to build site using python , specifically using Django. A library that contain lot of odule that help programmer to building their own website. 

## Create and activate Environement 

Setting in Windows: 

``` 
py -m venv myworld
myworld\Scripts\activate.bat
```
Setting MAC OS: 

```
python -m venv myworld
source myworld/bin/activate
```

# Install Django 
```
py -m pip install Django

```

# Create Project 
When starting projected, you have to type those commend: 
```
django-admin startproject {project name}

```
 After that, you will have to run the server and run your project 
```
py manage.py runserver

```

## Create an app 

What is an app ? So an app will allow you to list or register in Data base which it really useful when you want to handle well on borht backend and frontend. 

```
py manage.py startapp { app name} 

```

## Views.py :

Django views are Python functions that takes http requests and returns http response, like HTML documents.

Views.py original file looks like: 

```
from django.shortcuts import render

# Create your views here.
```
However, since you want to recieve and reponse to the request, we have to add something new: 

```
from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello world!")

```

## Urls.py 

fine the path of your inheritate app , e.x: website_builder/front_task/web_application/urls.py 

```

from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
]

```
After executing the file, the urls for the web should look like this:
" http://127.0.0.1:8000/members/ " . And print out like this: 
{ Hello } 

## Create a templates folder 

Create a templates folder in your apps and add a new html file in it.

Change the views.py method and add a few things on it. 

```
from django.http import HttpResponse
from django.template import loader

def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

```
Once finish editing the app, we want to save the app name so we go to settings.py and add the app name: 

Install_Apps=[
  'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps name'

]

then run this command: 
```
py manage.py migrate

```

## Creat SQL 

Check the create SQl file 
[Contribution guidelines for this project](create_sql)

### Show the sql data on the website 

Create a html in template call access which allow you to go thoorugh your sql base. You can find this file on the folder call templates provided. 
