from django.urls import path
from .views import *

urlpatterns = [
   path('', RegisterCreateView.as_view(), name="register"),
   path('login/', LoginCreateView.as_view(), name="login"),
   path('accounts/profile/', ProfileListView.as_view(), name="Profile"),
   path('accounts/update/<int:pk>/', ProfileUpdateView.as_view(), name="update"),
   path('logout', exit, name="logout"),

]
