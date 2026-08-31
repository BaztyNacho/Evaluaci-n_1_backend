from django.db import models


class Teacher(models.Model):
    """Representa a un docente que puede impartir una o más asignaturas (Course)."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    """Representa a un estudiante que puede inscribirse en varias asignaturas."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Course(models.Model):
    """Representa una asignatura, dictada por un único Teacher (FK teacher_id)."""
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='courses'
    )

    def __str__(self):
        return self.name


class StudentCourse(models.Model):
    """
    Tabla intermedia de inscripciones (student_id, course_id).
    Representa la relación muchos-a-muchos entre Student y Course.
    """
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='enrollments'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='enrollments'
    )

    class Meta:
        # Evita que un mismo estudiante se inscriba dos veces en la misma asignatura
        # (simula la clave primaria compuesta student_id + course_id del ER)
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student} → {self.course}"