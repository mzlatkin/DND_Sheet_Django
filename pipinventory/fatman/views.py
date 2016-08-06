from django.contrib.auth.models import User
from rest_framework import viewsets
from fatman.serializers import UserSerializer,CharacterSerializer,CharacterDetailSerializer
from fatman.models import Character,CharacterDetail
from rest_framework import permissions

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    model = User
    queryset = User.objects.all()

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all().select_related('account')
    model = Character
    serializer_class = CharacterSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CharacterDetailViewSet(viewsets.ModelViewSet):
    queryset = CharacterDetail.objects.all().select_related('character')
    model = CharacterDetail
    serializer_class = CharacterDetailSerializer
    permission_classes = (permissions.IsAuthenticated,)