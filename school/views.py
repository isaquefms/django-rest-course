from rest_framework import viewsets
from django.http import JsonResponse


from school.models import Student, Course
from school.serializer import StudentSerializer, CourseSerializer


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
