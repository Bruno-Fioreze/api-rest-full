from django.urls import path,include
from .views import lista_de_artigos,artigo_detalhe

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('lista_de_artigos/', lista_de_artigos),
    path('artigo/<int:pk>/', artigo_detalhe),


]


