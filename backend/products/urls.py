from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.product_alt_view),
    path('', views.product_list_create_view),
    path('<int:pk>/delete/', views.product_alt_view),
    path('<int:pk>/update', views.product_alt_view),
]