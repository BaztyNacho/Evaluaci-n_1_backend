from rest_framework import serializers
from .models import Teacher, Course, Student, StudentCourse


class TeacherSerializer(serializers.ModelSerializer):
    """Serializa los datos de un docente (Teacher) a formato JSON."""

    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name']


class CourseSerializer(serializers.ModelSerializer):
    """
    Serializa una asignatura (Course) incluyendo el nombre completo
    del profesor asignado, en vez de mostrar solo su ID.
    """
    teacher_name = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'name', 'teacher', 'teacher_name']

    def get_teacher_name(self, obj):
        # Concatena first_name + last_name del profesor de este curso
        return f"{obj.teacher.first_name} {obj.teacher.last_name}"


class StudentSerializer(serializers.ModelSerializer):
    """Serializa los datos de un estudiante (Student) a formato JSON."""

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name']


class StudentCourseSerializer(serializers.ModelSerializer):
    """
    Serializa una inscripción (StudentCourse), incluyendo los nombres
    legibles del estudiante y del curso, no solo sus IDs.
    """
    student_name = serializers.SerializerMethodField()
    course_name = serializers.SerializerMethodField()

    class Meta:
        model = StudentCourse
        fields = ['id', 'student', 'course', 'student_name', 'course_name']

    def get_student_name(self, obj):
        # Concatena first_name + last_name del estudiante inscrito
        return f"{obj.student.first_name} {obj.student.last_name}"

    def get_course_name(self, obj):
        # Nombre de la asignatura en la que está inscrito
        return obj.course.name