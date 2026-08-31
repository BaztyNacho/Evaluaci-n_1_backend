from django.contrib import admin
from django.urls import path, include
from academic import views as academic_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Endpoints de la API REST (DRF), consumidos vía fetch() desde el HTML
    path('api/', include('academic.urls')),

    # Vistas HTML (páginas visibles para el usuario)
    path('', academic_views.home, name='home'),
    path('teachers/', academic_views.teachers_page, name='teachers_page'),
    path('courses/', academic_views.courses_page, name='courses_page'),
    path('students/', academic_views.students_page, name='students_page'),
    path('student-courses/', academic_views.student_courses_page, name='student_courses_page'),
]