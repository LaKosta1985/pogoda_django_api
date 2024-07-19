
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from app.views import index



urlpatterns = [
    path('',index,name='index'),
]


