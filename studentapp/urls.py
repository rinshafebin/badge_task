from rest_framework.routers import DefaultRouter
from django.urls import path, include
from studentapp.views import (
    UserViewSet,
    CategoryListCreateView,
    CourseListCreateView,
    CourseRetrieveUpdateDestroyView,
    CourseEnrollmentView,
    EnrollmentListView,
    EnrollmentDetailView,
    UserStatus,
    AdminCourseStatus
    
)

router = DefaultRouter()
router.register('',UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('categories/', CategoryListCreateView.as_view()),
    path('courses/', CourseListCreateView.as_view()),
    path('courses/<int:pk>/', CourseRetrieveUpdateDestroyView.as_view()),
    path('courses/<int:pk>/enrollment/',CourseEnrollmentView.as_view()),
    path('enrollment/',EnrollmentListView.as_view()),
    path('enrollments/<int:pk>/', EnrollmentDetailView.as_view()),
    path('userstats/', UserStatus.as_view(), name='user-stats'),
    path('admin_coursestats/', AdminCourseStatus.as_view(), name='admin-course-stats'),

]
