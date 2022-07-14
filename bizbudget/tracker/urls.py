from django.urls import path
from . import views

urlpatterns = [
    path('tracker/', views.home, name="home"),
    path('tracker/admin/', views.admin, name="admin"),
    path('tracker/it/', views.it, name="it"),
    path('tracker/production/', views.production, name="production"),
    path('tracker/sales/', views.sales, name="sales"),

]