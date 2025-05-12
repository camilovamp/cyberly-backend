from rest_framework import viewsets
from profiles.models import Profile, ProfileCategory, ProfileLanguage
from .serializers import ProfileSerializer, ProfileCategorySerializer, ProfileLanguageSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProfileCategory.objects.all()
    serializer_class = ProfileCategorySerializer

class ProfileLanguageViewSet(viewsets.ModelViewSet):
    queryset = ProfileLanguage.objects.all()
    serializer_class = ProfileLanguageSerializer

