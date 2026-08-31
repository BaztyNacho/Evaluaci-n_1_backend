from django.urls import path
from . import views

# Rutas de la API REST (endpoints JSON, CRUD completo).
# Se montarán bajo el prefijo /api/ definido en academic_project/urls.py
urlpatterns = [
    # ----- Teacher -----
    path('teachers/', views.TeacherListCreateAPIView.as_view(), name='api_teachers'),
    path('teachers/<int:pk>/', views.TeacherDetailAPIView.as_view(), name='api_teacher_detail'),

    # ----- Course -----
    path('courses/', views.CourseListCreateAPIView.as_view(), name='api_courses'),
    path('courses/<int:pk>/', views.CourseDetailAPIView.as_view(), name='api_course_detail'),

    # ----- Student -----
    path('students/', views.StudentListCreateAPIView.as_view(), name='api_students'),
    path('students/<int:pk>/', views.StudentDetailAPIView.as_view(), name='api_student_detail'),

    # ----- StudentCourse (inscripciones) -----
    path('student-courses/', views.StudentCourseListCreateAPIView.as_view(), name='api_student_courses'),
    path('student-courses/<int:pk>/', views.StudentCourseDetailAPIView.as_view(), name='api_student_course_detail'),
]