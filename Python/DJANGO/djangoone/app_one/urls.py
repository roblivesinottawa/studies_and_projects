
from django.contrib import admin
from django.urls import path
from hello.views import myview
from todo.views import todoview, addTodo, deleteTodo


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sayHello/', myview),
    path('todo/', todoview),
    path('addTodo/', addTodo),
    path('deleteTodo/<int:todo_id>', deleteTodo),
    
]
