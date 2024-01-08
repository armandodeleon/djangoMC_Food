from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    path('', views.index, name='index'),     # /food/
    path('<int:item_id>/', views.detail, name='detalle'),    # /food/1, path's name is "detalle"
    path('item/', views.item, name='item')
]

