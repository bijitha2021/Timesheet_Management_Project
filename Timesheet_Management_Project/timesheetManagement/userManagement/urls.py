
from django.urls import path
from userManagement import views

app_name='userManagement'
# #URLPatterns for function based views
urlpatterns = [
    path('', views.UserList.as_view(), name='user_list'),
    path('<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('new/', views.user_new, name='user_new'),
   # path('<int:blog_id>/update', views.blog_update, name='blog_update'),
]


