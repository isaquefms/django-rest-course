from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from school.models import Enrollment, Student, Course
from school.serializer import EnrollmentSerializer, EnrollmentStudentsSerializer, StudentSerializer, CourseSerializer, StudentsEnrollmentCoursesSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """Manipulação do recurso aluno.
    """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


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


class EnrollmentStudentsViewSet(generics.ListAPIView):
    """Manipulação do recurso matrícula.
    """

    def get_queryset(self):
        queryset = Enrollment.objects.filter(student_id=self.kwargs['pk'])
        return queryset
    
    serializer_class = EnrollmentStudentsSerializer


class StudentsEnrollmentCoursesViewSet(generics.ListAPIView):
    """Manipulação do recurso matrícula.
    """

    def get_queryset(self):
        return Enrollment.objects.filter(course_id=self.kwargs['pk'])
    
    serializer_class = StudentsEnrollmentCoursesSerializer
