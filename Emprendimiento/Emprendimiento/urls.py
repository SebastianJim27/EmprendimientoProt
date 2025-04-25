from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('foro.urls')),
    path('registro/', include('registro.urls')),
    path('chat/', include('chatforo.urls')),
    path('usuario/', include('infousuario.urls')),
    path('debates/', include('debates.urls')),
]
