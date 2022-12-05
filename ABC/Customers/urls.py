from django.urls import path, include
from . import views
urlpatterns = [
    path('page/add', views.new_customer),
    path('db/insert', views.insert_customer_in_db),
]