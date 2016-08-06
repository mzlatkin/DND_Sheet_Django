from fatman.serializers import UserSerializer, CharacterSerializer, CharacterDetailSerializer,CharClassSerializer,SizeSerializer,CharClassAssociationSerializer,RaceSerializer,SkillSerializer,SkillTypeSerializer,SkillAssociationSerializer,AttributeSerializer,AttributeAssociationSerializer,FeatSerializer,FeatAssociationSerializer,ItemSerializer,ItemAssociationSerializer,ArmorSerializer,ArmorAssociationSerializer,WeaponSerializer,WeaponTypeSerializer,WeaponAssociationSerializer,SpellSerializer,SpellAssociationSerializer
from fatman.models import Character, CharacterDetail,CharClass,Size,CharClassAssociation,Race,Skill,SkillType,SkillAssociation,Attribute,AttributeAssociation,Feat,FeatAssociation,Item,ItemAssociation,Armor,ArmorAssociation,Weapon,WeaponType,WeaponAssociation,Spell,SpellAssociation
from django.contrib.auth.models import User
from rest_framework import viewsets
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


class CharClassViewSet(viewsets.ModelViewSet):
    queryset = CharClass.objects.all()
    model = CharClass
    serializer_class = CharClassSerializer
    permission_classes = (permissions.IsAuthenticated,)


class SizeViewSet(viewsets.ModelViewSet):
    queryset = Size.objects.all()
    model = Size
    serializer_class = SizeSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CharClassAssociationViewSet(viewsets.ModelViewSet):
    queryset = CharClassAssociation.objects.all().select_related('char_class','level')
    model = CharClassAssociation
    serializer_class = CharClassAssociationSerializer
    permission_classes = (permissions.IsAuthenticated,)


class RaceViewSet(viewsets.ModelViewSet):
    queryset = Race.objects.all()
    model = Race
    serializer_class = RaceSerializer
    permission_classes = (permissions.IsAuthenticated,)


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    model = Skill
    serializer_class = SkillSerializer
    permission_classes = (permissions.IsAuthenticated,)


class SkillTypeViewSet(viewsets.ModelViewSet):
    queryset = SkillType.objects.all()
    model = SkillType
    serializer_class = SkillTypeSerializer
    permission_classes = (permissions.IsAuthenticated,)


class SkillAssociationViewSet(viewsets.ModelViewSet):
    queryset = SkillAssociation.objects.all().select_related('character', 'skill', 'attribute', 'skill_type')
    model = SkillAssociation
    serializer_class = SkillAssociationSerializer
    permission_classes = (permissions.IsAuthenticated,)


class AttributeViewSet(viewsets.ModelViewSet):
    queryset = Attribute.objects.all()
    model = Attribute
    serializer_class = AttributeSerializer
    permission_classes = (permissions.IsAuthenticated,)


class AttributeAssociationViewSet(viewsets.ModelViewSet):
    queryset = AttributeAssociation.objects.all().select_related('character', 'attribute')
    model = AttributeAssociation
    serializer_class = AttributeAssociationSerializer
    permission_classes = (permissions.IsAuthenticated,)


class FeatViewSet(viewsets.ModelViewSet):
    queryset = Feat.objects.all()
    model = Feat
    serializer_class = FeatSerializer
    permission_classes = (permissions.IsAuthenticated,)


class FeatAssociationViewSet(viewsets.ModelViewSet):
    queryset = FeatAssociation.objects.all().select_related('character', 'feat')
    model = FeatAssociation
    serializer_class = FeatAssociationSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    model = Item
    serializer_class = ItemSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ItemAssociationViewSet(viewsets.ModelViewSet):
    queryset = ItemAssociation.objects.all().select_related('character', 'item')
    model = ItemAssociation
    serializer_class = ItemAssociationSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ArmorViewSet(viewsets.ModelViewSet):
    queryset = Armor.objects.all().select_related('item')
    model = Armor
    serializer_class = ArmorSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ArmorAssociationViewSet(viewsets.ModelViewSet):
    queryset = ArmorAssociation.objects.all().select_related('armor', 'item')
    model = ArmorAssociation
    serializer_class = ArmorAssociationSerializer
    permission_classes = (permissions.IsAuthenticated,)


class WeaponViewSet(viewsets.ModelViewSet):
    queryset = Weapon.objects.all().select_related('item')
    model = Weapon
    serializer_class = WeaponSerializer
    permission_classes = (permissions.IsAuthenticated,)


class WeaponTypeViewSet(viewsets.ModelViewSet):
    queryset = WeaponType.objects.all()
    model = WeaponType
    serializer_class = WeaponTypeSerializer
    permission_classes = (permissions.IsAuthenticated,)


class WeaponAssociationViewSet(viewsets.ModelViewSet):
    queryset = WeaponAssociation.objects.all().select_related('weapon', 'item')
    model = WeaponAssociation
    serializer_class = WeaponAssociationSerializer
    permission_classes = (permissions.IsAuthenticated,)


class SpellViewSet(viewsets.ModelViewSet):
    queryset = Spell.objects.all()
    model = Spell
    serializer_class = SpellSerializer
    permission_classes = (permissions.IsAuthenticated,)


class SpellAssociationViewSet(viewsets.ModelViewSet):
    queryset = SpellAssociation.objects.all().select_related('character', 'spell')
    model = SpellAssociation
    serializer_class = SpellAssociationSerializer
    permission_classes = (permissions.IsAuthenticated,)