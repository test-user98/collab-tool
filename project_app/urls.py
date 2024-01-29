from django.urls import path
from . import views
from project_manager import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('projects/', views.project_list, name='project_list'),
    path('create_project/', views.create_project, name='create_project'),
    path('projects/<int:project_id>/tasks/', views.task_list, name='task_list'),
    path('projects/<int:project_id>/tasks/add/', views.add_task, name='add_task'),
    path('projects/<int:project_id>/tasks/<int:task_id>/update/', views.update_task, name='update_task'),
    path('projects/<int:project_id>/tasks/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('logout/', auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('', views.homepage, name='homepage'),


]
