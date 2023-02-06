from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListCreateView.as_view()),
    path('<int:pk>/', views.ProductRetrieveUpdateDestroyView.as_view())
]