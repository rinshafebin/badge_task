from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from studentapp.serializers import RegisterSerializer,CategorySerializer,CourseSerializer,EnrollmentSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView,RetrieveUpdateAPIView
from studentapp.models import Category,Course,Enrollment
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser

class UserViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['post'], url_path='register')
    def register(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'status': 'user created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='login')
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)



class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
   


class CourseListCreateView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer   
   
 

class CourseRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminUser]

    


class CourseEnrollmentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
            Enrollment.objects.create(user=request.user, course=course)
            return Response({"detail": "Enrolled successfully"}, status=status.HTTP_201_CREATED)
        except Course.DoesNotExist:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({"error": "Already enrolled or error"}, status=status.HTTP_400_BAD_REQUEST)
        
        
class EnrollmentListView(ListAPIView):
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Enrollment.objects.filter(user=self.request.user)
    

class EnrollmentDetailView(RetrieveUpdateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]
