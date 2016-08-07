from fatman.serializers import UserSerializer, CharacterSerializer, CharacterDetailSerializer,CharClassSerializer,SizeSerializer,CharClassAssociationSerializer,RaceSerializer,SkillSerializer,SkillTypeSerializer,SkillAssociationSerializer,AttributeSerializer,AttributeAssociationSerializer,FeatSerializer,FeatAssociationSerializer,ItemSerializer,ItemAssociationSerializer,ArmorSerializer,ArmorAssociationSerializer,WeaponSerializer,WeaponTypeSerializer,WeaponAssociationSerializer,SpellSerializer,SpellAssociationSerializer
from fatman.models import Character, CharacterDetail,CharClass,Size,CharClassAssociation,Race,Skill,SkillType,SkillAssociation,Attribute,AttributeAssociation,Feat,FeatAssociation,Item,ItemAssociation,Armor,ArmorAssociation,Weapon,WeaponType,WeaponAssociation,Spell,SpellAssociation
from rest_framework.decorators import detail_route, list_route
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import filters

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    model = User
    queryset = User.objects.all()

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all().select_related('account')
    model = Character
    serializer_class = CharacterSerializer
    permission_classes = ()
    paginator=None
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('account', 'name', 'created', 'updated','is_active',)


class CharacterDetailViewSet(viewsets.ModelViewSet):
    queryset = CharacterDetail.objects.all().select_related('character','size','race')
    model = CharacterDetail
    serializer_class = CharacterDetailSerializer
    permission_classes = ()
    paginator=None
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('character', 'gender', 'deity','alignment','base_attack_bonus','size','race',)

    @list_route(methods=['get'])
    def get_details_by_character(self, request, format=None):
        character = self.request.query_params.get('character', None)
        ret = None
        try:
            ret = CharacterDetail.objects.filter(character=character)
            ret = CharacterDetailSerializer(ret, many=True)
        except Exception as e:
            return Response({},status=status.HTTP_400_BAD_REQUEST)

        return Response(ret.data)


class CharClassViewSet(viewsets.ModelViewSet):
    queryset = CharClass.objects.all()
    model = CharClass
    serializer_class = CharClassSerializer
    permission_classes = ()
    paginator=None
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name',)


class SizeViewSet(viewsets.ModelViewSet):
    queryset = Size.objects.all()
    model = Size
    serializer_class = SizeSerializer
    permission_classes = ()
    paginator=None
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('size',)


class CharClassAssociationViewSet(viewsets.ModelViewSet):
    queryset = CharClassAssociation.objects.all().select_related('char_class','character')
    model = CharClassAssociation
    serializer_class = CharClassAssociationSerializer
    permission_classes = ()
    paginator=None
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('character','char_class','level',)


class RaceViewSet(viewsets.ModelViewSet):
    queryset = Race.objects.all()
    model = Race
    serializer_class = RaceSerializer
    permission_classes = ()
    paginator=None
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name',)


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all().select_related('attribute', 'skill_type')
    model = Skill
    serializer_class = SkillSerializer
    permission_classes = ()
    paginator=None
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'disscription','attribute', 'skill_type',)


class SkillTypeViewSet(viewsets.ModelViewSet):
    queryset = SkillType.objects.all()
    model = SkillType
    serializer_class = SkillTypeSerializer
    permission_classes = ()
    paginator=None
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name',)


class SkillAssociationViewSet(viewsets.ModelViewSet):
    queryset = SkillAssociation.objects.all().select_related('character', 'skill')
    model = SkillAssociation
    serializer_class = SkillAssociationSerializer
    permission_classes = ()
    paginator=None
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('character', 'skill','rank', 'effect',)


class AttributeViewSet(viewsets.ModelViewSet):
    queryset = Attribute.objects.all()
    model = Attribute
    serializer_class = AttributeSerializer
    permission_classes = ()
    paginator=None
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'disscription',)


class AttributeAssociationViewSet(viewsets.ModelViewSet):
    queryset = AttributeAssociation.objects.all().select_related('character', 'attribute')
    model = AttributeAssociation
    serializer_class = AttributeAssociationSerializer
    permission_classes = ()
    paginator=None
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('character', 'attribute', 'rank', 'effect',)


class FeatViewSet(viewsets.ModelViewSet):
    queryset = Feat.objects.all()
    model = Feat
    serializer_class = FeatSerializer
    permission_classes = ()
    paginator=None
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'disscription', 'benefit',)


class FeatAssociationViewSet(viewsets.ModelViewSet):
    queryset = FeatAssociation.objects.all().select_related('character', 'feat')
    model = FeatAssociation
    serializer_class = FeatAssociationSerializer
    permission_classes = ()
    paginator=None
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('character', 'feat', 'rank',)


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    model = Item
    serializer_class = ItemSerializer
    permission_classes = ()
    paginator=None
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'weight', 'cost',)


class ItemAssociationViewSet(viewsets.ModelViewSet):
    queryset = ItemAssociation.objects.all().select_related('character', 'item')
    model = ItemAssociation
    serializer_class = ItemAssociationSerializer
    permission_classes = ()
    paginator=None
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('character', 'item', 'amount',)


class ArmorViewSet(viewsets.ModelViewSet):
    queryset = Armor.objects.all().select_related('item')
    model = Armor
    serializer_class = ArmorSerializer
    permission_classes = ()
    paginator=None
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('item', 'ac_bonus', 'max_dex', 'check_penalty', 'spell_fail', 'speed',)


class ArmorAssociationViewSet(viewsets.ModelViewSet):
    queryset = ArmorAssociation.objects.all().select_related('armor', 'character')
    model = ArmorAssociation
    serializer_class = ArmorAssociationSerializer
    permission_classes = ()
    paginator=None
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('armor','character', 'amount', 'equipped',)


class WeaponViewSet(viewsets.ModelViewSet):
    queryset = Weapon.objects.all().select_related('item')
    model = Weapon
    serializer_class = WeaponSerializer
    permission_classes = ()
    paginator=None
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('item', 'weapon_type', 'damage', 'crit', 'range_radius',)


class WeaponTypeViewSet(viewsets.ModelViewSet):
    queryset = WeaponType.objects.all()
    model = WeaponType
    serializer_class = WeaponTypeSerializer
    permission_classes = ()
    paginator=None
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name',)


class WeaponAssociationViewSet(viewsets.ModelViewSet):
    queryset = WeaponAssociation.objects.all().select_related('weapon', 'character')
    model = WeaponAssociation
    serializer_class = WeaponAssociationSerializer
    permission_classes = ()
    paginator=None
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('weapon','character', 'amount', 'equipped',)


class SpellViewSet(viewsets.ModelViewSet):
    queryset = Spell.objects.all()
    model = Spell
    serializer_class = SpellSerializer
    permission_classes = ()
    paginator=None
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'disscription',)


class SpellAssociationViewSet(viewsets.ModelViewSet):
    queryset = SpellAssociation.objects.all().select_related('character', 'spell')
    model = SpellAssociation
    serializer_class = SpellAssociationSerializer
    permission_classes = ()
    paginator=None
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('character', 'spell','prepared')