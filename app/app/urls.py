from django.urls import path, include
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Modulka/', include('Modulka.urls', namespace='Modulka')),
]
