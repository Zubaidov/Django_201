from django.urls import path
from .import views

app_name = "mainapp"

urlpatterns = [
    path("", views.HomePageView.as_view(), name='index'),
    path("<int:pk>/", views.PostDetailView.as_view(), name='detail'),
]
