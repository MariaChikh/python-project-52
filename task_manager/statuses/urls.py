from django.urls import path
from task_manager.statuses import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='statuses_index'),
    path('create/', views.StatusCreateView.as_view(), name='status_create'),
    #path('<int:pk>/edit/', views.UserUpdateView.as_view(), name='user_update'),
    #path('<int:pk>/delete/', views.UserDeleteView.as_view(), name='user_delete'),
    
]