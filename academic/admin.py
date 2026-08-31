from django.contrib import admin
from .models import Teacher, Course, Student, StudentCourse


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    # Columnas visibles en el listado del admin
    list_display = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # Muestra el nombre del profesor asignado en vez del objeto crudo
    list_display = ('id', 'name', 'teacher')
    search_fields = ('name',)
    list_filter = ('teacher',)


@admin.register(StudentCourse)
class StudentCourseAdmin(admin.ModelAdmin):
    # Representa la tabla de inscripciones: qué estudiante está en qué curso
    list_display = ('id', 'student', 'course')
    list_filter = ('course', 'student')