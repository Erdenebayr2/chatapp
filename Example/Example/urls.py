from django.urls import path,include
from examapp import views

urlpatterns = [
    path('chats',include('examapp.urls')),
    path('', views.userlog, name='userlog'),
    path('accounts.google.com/', views.google_login, name='google')
]
