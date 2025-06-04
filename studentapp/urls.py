from rest_framework.routers import DefaultRouter
from django.urls import path, include
from studentapp.views import UserViewSet,CategoryListCreateView

router = DefaultRouter()
router.register('',UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('categories/', CategoryListCreateView.as_view()),

]
