from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import RegistrationForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Project, Task
from .forms import ProjectForm, TaskForm


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('profile'))
    else:
        form = RegistrationForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')  # Redirect to the user's profile page after login
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def homepage(request):
    return render(request, 'homepage.html')

@login_required
def profile(request):
    return render(request, 'profile.html')
    # user_projects = Project.objects.filter(owner=request.user)
    # return render(request, 'profile.html', {'user_projects': user_projects})

# def project_list(request):
#     projects = Project.objects.filter(owner=request.user)
#     return render(request, 'project_list.html', {'projects': projects})

@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect('project_list')  # Redirect to the project list after creation
    else:
        form = ProjectForm()
    return render(request, 'create_project.html', {'form': form})

@login_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

def task_list(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    tasks = Task.objects.filter(project=project)
    return render(request, 'tasks/task_list.html', {'project': project, 'tasks': tasks})

# View to add a new task
def add_task(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('task_list', project_id=project_id)
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'project': project, 'form': form})

# View to update an existing task
def update_task(request, project_id, task_id):
    project = get_object_or_404(Project, pk=project_id)
    task = get_object_or_404(Task, pk=task_id, project=project)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            project.update_percentage_completed()
            return redirect('task_list', project_id=project_id)
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/update_task.html', {'project': project, 'task': task, 'form': form})

# View to delete a task
def delete_task(request, project_id, task_id):
    project = get_object_or_404(Project, pk=project_id)
    task = get_object_or_404(Task, pk=task_id, project=project)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list', project_id=project_id)
    return render(request, 'tasks/delete_task.html', {'project': project, 'task': task})


def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    tasks = project.task_set.all()  # Retrieve all tasks related to the project
    return render(request, 'project_detail.html', {'project': project, 'tasks': tasks})
