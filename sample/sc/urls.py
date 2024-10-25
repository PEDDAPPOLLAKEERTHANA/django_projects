from django.urls import path
from sc import views

urlpatterns = [
    path('anantapur/towerclock', views.f, name='home'),
    path('anantapur/tower', views.func2),
    path('anantapur/tow/<str:name>', views.fun),
    path('wish1', views.f),
    path('wish/<str:b>', views.func4),
    path('index', views.index, name="index"),
    path('items', views.items, name='items'),
    path('about', views.about, name='about'),
    path('nitem', views.nitem, name='nitem'),
    path('table', views.table, name='table'),
    path('form', views.farenhit, name='form'),
    path('form2', views.f3, name='form2'), 
    
]
