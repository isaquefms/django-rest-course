from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from school.views import CourseViewSet, EnrollmentStudentsViewSet, EnrollmentViewSet, StudentViewSet, StudentsEnrollmentCoursesViewSet

router = routers.DefaultRouter()
router.register('courses', CourseViewSet, basename='Courses')
router.register('students', StudentViewSet, basename='Students')
router.register('enrollments', EnrollmentViewSet, basename='Enrollments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('students/<int:pk>/enrollments/', EnrollmentStudentsViewSet.as_view(), name='enrollment-students'),
    path('courses/<int:pk>/enrollments/', StudentsEnrollmentCoursesViewSet.as_view(), name='students-enrollment-courses'),
]
