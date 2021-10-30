from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.demo, name='demo'),
    path('create', views.create, name="create"),
    path('retrieve', views.retrieve, name="retrieve"),
    path('edit/<int:id>',views.edit,name="edit"),
    path('update/<int:id>',views.update,name="update"),
    path('delete_product/<int:id', views.delete,name="delete"),
]
