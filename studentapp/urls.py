from rest_framework.routers import DefaultRouter
from django.urls import path, include
from studentapp.views import UserViewSet,CategoryListCreateView,CourseListCreateView,CourseRetrieveUpdateDestroyView,CourseEnrollmentView,EnrollmentListView

router = DefaultRouter()
router.register('',UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('categories/', CategoryListCreateView.as_view()),
    path('courses/', CourseListCreateView.as_view()),
    path('courses/<int:pk>/', CourseRetrieveUpdateDestroyView.as_view()),
    path('courses/<int:pk>/enrollment/',CourseEnrollmentView.as_view()),
    path('enrollment/',EnrollmentListView.as_view()),



]
