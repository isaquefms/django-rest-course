from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from school.views import CourseViewSet, EnrollmentViewSet, StudentViewSet

router = routers.DefaultRouter()
router.register('courses', CourseViewSet, basename='Courses')
router.register('students', StudentViewSet, basename='Students')
router.register('enrollments', EnrollmentViewSet, basename='Enrollments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
