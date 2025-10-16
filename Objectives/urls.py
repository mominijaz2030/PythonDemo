from django.contrib import admin
from django.urls import path, include
from todolistapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('task/', include('todolistapp.urls')),
    path('account/', include('usersapp.urls')),
    path('contact', views.contact,name='contact'),
    path('about-us', views.about,name='about'),
]
