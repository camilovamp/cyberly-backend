from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoginView
from .views import ProfileCategoryViewSet, ProfileLanguageViewSet, ProfileViewSet

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'profile-categories', ProfileCategoryViewSet)
router.register(r'profile-languages', ProfileLanguageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
]
