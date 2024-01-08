from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),     # /food/
    path('<int:item_id>/', views.detail),    # /food/1
    path('item/', views.item, name='item')
]

