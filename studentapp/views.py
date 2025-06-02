from rest_framework.viewsets import ModelViewSet
from studentapp.models import Student,Course,Enrollment,Assessment,Grade
from studentapp.serializers import StudentSerializer,CourseSerializer,EnrollmentSerializer,AssessmentSerializer,GradeSerializer

# Create your views here.
class StudentView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class CourseView(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
class EnrollmentView(ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class AssessmentView(ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer

class GradeView(ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    