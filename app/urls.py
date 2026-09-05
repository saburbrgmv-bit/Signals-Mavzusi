from django.urls import path
from .views import *

urlpatterns = [
  path('home/', PostListView.as_view(), name="home"),
  path('create/', PostCreateView.as_view(), name="create"),
  path('update/<int:pk>/', PostUpdateView.as_view(), name="update"),
  path('delete/<int:pk>/', PostDeleteView.as_view(), name="delete"),

]