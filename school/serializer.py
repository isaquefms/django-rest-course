from rest_framework import serializers


from school.models import Enrollment, Student, Course


class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'
    

class EnrollmentStudentsSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.description')
    period = serializers.SerializerMethodField()

    class Meta:
        model = Enrollment
        fields = ['course', 'period']

    def get_period(self, obj):
        return obj.get_period_display()


class StudentsEnrollmentCoursesSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source='student.first_name')

    class Meta:
        model = Enrollment
        fields = ['student']
