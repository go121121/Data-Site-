from django.urls import path 
from . import views 

urlpatterns=[ path('web_application/',views.webapplication, name='application'),
             path('web_application/details/<int:id>',views.details, name='details'),
             path('',views.main,name='main page'), 
             path('testing/', views.testing, name='testing page')
             ]
