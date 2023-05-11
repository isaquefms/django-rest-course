from django.contrib import admin

from school.models import Enrollment, Student, Course


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'document', 'document_number', 'born_date')
    list_display_links = ('id', 'first_name')
    search_fields = ('first_name',)
    list_per_page = 20


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'description', 'level')
    list_display_links = ('id', 'code')
    search_fields = ('code', 'name')
    list_per_page = 20


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'enrollment_date', 'period')
    list_display_links = ('id', 'student')
    search_fields = ('student__first_name', 'course__name')
    list_per_page = 20


# Importação dos modelos no Admin
admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
