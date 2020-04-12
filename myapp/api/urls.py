from django.urls import path
from rest_framework.authtoken import views
from myapp.api.views import (Book_List, Book_Detail, CreateuserView, LoginView)
urlpatterns = [
    path('list/', Book_List, name="api_list"),
    path('books/<pk>', Book_Detail, name="api_detail_view"),
    path('register/', CreateuserView.as_view(), name="User-register"),
    path('login/', LoginView.as_view(), name="login")
]
