from django.contrib import admin
from django.urls import path
from registro import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.registrar_evento, name='registrar_evento'),
    path('registro_exitoso/', views.registro_exitoso, name='registro_exitoso'),
]
