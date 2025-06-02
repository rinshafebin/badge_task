from django.urls import path,include
from rest_framework.routers import DefaultRouter
from studentapp.views import StudentView,CourseView,EnrollmentView,AssessmentView,GradeView

router = DefaultRouter()
router.register('students',StudentView,basename='students')
router.register('courses',CourseView,basename='course')
router.register('enrollment',EnrollmentView,basename='enrollment')
router.register('assisment',AssessmentView,basename='assessment')
router.register('grade',GradeView,basename='Grade')


urlpatterns = [
    path('router/',include(router.urls)),
]

