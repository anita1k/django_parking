from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from parkings.views import *

from parkings import views

urlpatterns = [
    path('', include('parkings.urls'))
]

