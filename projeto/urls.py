from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:argumento>', views.outraspaginas, name='pagina'),
    path('admin/', admin.site.urls),
]
