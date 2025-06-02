from rest_framework import serializers
from studentapp.models import Student,Course,Enrollment,Assessment,Grade

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields ='__all__'
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        
class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = '__all__'
        

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'
             
