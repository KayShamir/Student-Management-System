from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # 'index' as the main page
    path('add_student/', views.add_student, name='add_student'),  # Separate URL for adding a student
]
