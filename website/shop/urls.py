from django.urls import path
from .views import main_home, main_kup
from .views import main_shop
from .views import main_kup

urlpatterns = [
    path('',main_home,name='main'),
    path('mag',main_shop,name='shop'),
    path('kup',main_kup,name='kup'),
]