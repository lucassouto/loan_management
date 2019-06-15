from django.urls import path
from .views import HelloProject


list_actions = {'get': 'list'}

app_name = 'api'
urlpatterns = [
    path('hello_project/', HelloProject.as_view(list_actions), name='hello_project')
]
