from rest_framework import generics
from django.shortcuts import render

from .models import Teacher, Course, Student, StudentCourse
from .serializers import (
    TeacherSerializer,
    CourseSerializer,
    StudentSerializer,
    StudentCourseSerializer,
)


# ---------- Endpoints DRF (API REST) - CRUD completo ----------
# Cada entidad tiene 2 vistas:
#   - ListCreate: GET (listar todos) + POST (crear uno nuevo)
#   - RetrieveUpdateDestroy: GET (ver uno) + PUT/PATCH (editar) + DELETE (eliminar)
# Son las que el navegador consulta de forma asíncrona vía fetch() desde el HTML.

# ----- Teacher -----

class TeacherListCreateAPIView(generics.ListCreateAPIView):
    """GET /api/teachers/ -> lista de profesores | POST -> crea uno nuevo."""
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """GET/PUT/PATCH/DELETE /api/teachers/<id>/ -> ver, editar o eliminar un profesor."""
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


# ----- Course -----

class CourseListCreateAPIView(generics.ListCreateAPIView):
    """GET /api/courses/ -> lista de cursos con profesor | POST -> crea uno nuevo."""
    queryset = Course.objects.select_related('teacher').all()
    serializer_class = CourseSerializer


class CourseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """GET/PUT/PATCH/DELETE /api/courses/<id>/ -> ver, editar o eliminar un curso."""
    queryset = Course.objects.select_related('teacher').all()
    serializer_class = CourseSerializer


# ----- Student -----

class StudentListCreateAPIView(generics.ListCreateAPIView):
    """GET /api/students/ -> lista de estudiantes | POST -> crea uno nuevo."""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """GET/PUT/PATCH/DELETE /api/students/<id>/ -> ver, editar o eliminar un estudiante."""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# ----- StudentCourse (inscripciones) -----

class StudentCourseListCreateAPIView(generics.ListCreateAPIView):
    """GET /api/student-courses/ -> lista de inscripciones | POST -> crea una nueva."""
    queryset = StudentCourse.objects.select_related('student', 'course').all()
    serializer_class = StudentCourseSerializer


class StudentCourseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """GET/PUT/PATCH/DELETE /api/student-courses/<id>/ -> ver, editar o eliminar una inscripción."""
    queryset = StudentCourse.objects.select_related('student', 'course').all()
    serializer_class = StudentCourseSerializer


# ---------- Vistas HTML (páginas que "enmascaran" la API) ----------
# Estas vistas solo renderizan templates; los datos reales los trae
# el JavaScript de cada plantilla vía fetch() a /api/...

def home(request):
    """Página de inicio, elimina el 404 en la ruta raíz '/'."""
    return render(request, 'academic/home.html')


def courses_page(request):
    """Renderiza la vista HTML de Cursos (los datos llegan vía fetch())."""
    return render(request, 'academic/courses.html')


def students_page(request):
    """Renderiza la vista HTML de Estudiantes (los datos llegan vía fetch())."""
    return render(request, 'academic/students.html')


def teachers_page(request):
    """Renderiza la vista HTML de Profesores (los datos llegan vía fetch())."""
    return render(request, 'academic/teachers.html')


def student_courses_page(request):
    """Renderiza la vista HTML de Inscripciones (los datos llegan vía fetch())."""
    return render(request, 'academic/student_courses.html')