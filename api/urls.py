from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet
from . import views


router = DefaultRouter()
router.register('students', StudentViewSet)


urlpatterns = [
    path('', include(router.urls)),

    path('students/', views.student_list, name='students'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:id>/', views.edit_student, name='edit_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
]
