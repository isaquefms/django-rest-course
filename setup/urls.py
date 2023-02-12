from django.contrib import admin
from django.urls import path
from school.views import get_students

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', get_students, name='get_students')
]
