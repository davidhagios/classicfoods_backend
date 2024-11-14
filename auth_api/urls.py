from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('get_user', views.get_user, name='get_user'),
    path('create-task', views.createTask, name='create-task'),
    path('tasks', views.tasks, name='tasks'),
    path('delete-task/<str:pk>', views.deleteTask, name='deleteTask'),
    path('complete-task/<str:pk>', views.completeTask, name='completeTask'),

]