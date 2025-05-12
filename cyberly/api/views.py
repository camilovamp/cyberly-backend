from rest_framework import viewsets, DjangoFilterBackend
from profiles.models import Profile, ProfileCategory, ProfileLanguage
from .serializers import ProfileSerializer, ProfileCategorySerializer, ProfileLanguageSerializer
from .filters import ProfileFilter

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProfileFilter

class ProfileCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProfileCategory.objects.all()
    serializer_class = ProfileCategorySerializer

class ProfileLanguageViewSet(viewsets.ModelViewSet):
    queryset = ProfileLanguage.objects.all()
    serializer_class = ProfileLanguageSerializer

