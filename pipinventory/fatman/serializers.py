from django.contrib.auth.models import User
from rest_framework import serializers
from fatman.models import Character, CharacterDetail

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'password', 'first_name', 'last_name', 'email',)
        write_only_fields = ('password',)
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'].strip(),
            last_name=validated_data['last_name'].strip()
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    account = serializers.SlugRelatedField(slug_field='pk',required=True,queryset=User.objects.all().select_related())

    class Meta:
        model = Character
        fields = ('pk', 'account', 'name', 'created', 'updated','is_active')

class CharacterDetailSerializer(serializers.HyperlinkedModelSerializer):
    character = serializers.SlugRelatedField(slug_field='pk',required=True,queryset=Character.objects.all().select_related())

    class Meta:
        model = CharacterDetail
        fields = ('pk', 'character', 'gender', 'level', 'deity','alignment','base_attack_bonus')