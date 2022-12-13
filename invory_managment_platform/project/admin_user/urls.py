from django.urls import path,include
from admin_user import views

app_name = 'admin_user'

urlpatterns = [
    path('user_login/', views.user_login, name='user_login'),
    path("register/", views.register, name="register"),
    path("index/", views.index, name="index"),
    path("indexs/", views.indexs, name="indexs"),
    path("indext/", views.indext, name="indext"),
    path("signin/", views.signin, name="signin"),
]
