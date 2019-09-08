
from django.conf.urls import url
from django.contrib import admin
from photoapp import views
app_name = 'photoapp'

urlpatterns = [
    url('',views.index,name='index'),
    url('<int:photo_id>/', views.detail,name='detail'),
]
