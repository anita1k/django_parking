from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from parkings.views import *

from parkings import views

# urlpatterns = [
#     # path('', views.home, name='home'),
#     path('admin/', admin.site.urls),
#     path('', views.PlaceView.as_view(), name='place_list'),
# ]

urlpatterns = [
    # path('', include('frontend.urls')),
    path('', include('parkings.urls'))
]

