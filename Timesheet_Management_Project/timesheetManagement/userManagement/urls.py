from django.urls import path
from userManagement import views

app_name='userManagement'
# #URLPatterns for function based views
urlpatterns = [
    path('', views.UserList.as_view(), name='user_list'),
    #path('<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('new/', views.user_new, name='user_new'),
    #path('new/',views.UserCreate.as_view(),name='user_new'),
    #path('<int:user_id>/update', views.user_update, name='user_update'),
    path('<int:pk>/update', views.UserUpdate.as_view(), name='user_update'),
]


