from django.urls import path
from workdayManagement import views

app_name = 'workdayManagement'
# #URLPatterns for function based views
urlpatterns = [
    path('', views.WorkList.as_view(), name='work_list'),
    path('new/', views.WorkCreate.as_view(), name='work_new'),
    path('<int:pk>/update', views.WorkUpdate.as_view(), name='work_update'),
]
