from django.contrib import admin
from django.urls import path, include

# from .. import custumer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('custumer.urls')), # adicionando (include) as urls de api
]
