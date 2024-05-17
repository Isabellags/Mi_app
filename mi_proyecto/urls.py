# mi_proyecto/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mi_app/', include('mi_app.urls')),
    path('', include('mi_app.urls')),  # Esto redirige la raíz a mi_app
]
