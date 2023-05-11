from rest_framework import viewsets

from school.models import Enrollment, Student, Course
from school.serializer import EnrollmentSerializer, StudentSerializer, CourseSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """Manipulação do recurso aluno.
    """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """Manipulação do recurso curso.
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):
    """Manipulação do recurso matrícula.
    """

    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
