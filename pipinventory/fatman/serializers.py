from django.contrib.auth.models import User
from rest_framework import serializers
from fatman.models import Character, CharacterDetail,CharClass,Size,CharClassAssociation,Race,Skill,SkillType,SkillAssociation,Attribute,AttributeAssociation,Feat,FeatAssociation,Item,ItemAssociation,Armor,ArmorAssociation,Weapon,WeaponType,WeaponAssociation,Spell,SpellAssociation

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
    size = serializers.SlugRelatedField(slug_field='pk',required=True,queryset=Size.objects.all().select_related())
    race = serializers.SlugRelatedField(slug_field='pk',required=True,queryset=Race.objects.all().select_related())

    class Meta:
        model = CharacterDetail
        fields = ('pk', 'character','race','size', 'gender', 'deity','alignment','base_attack_bonus')

class GetDetailsByCharacterSerializer(serializers.HyperlinkedModelSerializer):
    character = serializers.SlugRelatedField(slug_field='pk',required=True,queryset=Character.objects.all().select_related())
    size = serializers.SlugRelatedField(slug_field='size',required=True,queryset=Size.objects.all().select_related())
    race = serializers.SlugRelatedField(slug_field='name',required=True,queryset=Race.objects.all().select_related())

    class Meta:
        model = CharacterDetail
        fields = ('pk', 'character','race','size', 'gender', 'deity','alignment','base_attack_bonus')

class CharClassSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CharClass
        fields = ('pk', 'name')


class SizeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Size
        fields = ('pk', 'size')


class CharClassAssociationSerializer(serializers.HyperlinkedModelSerializer):
    character = serializers.SlugRelatedField(slug_field='pk',required=True,queryset=Character.objects.all().select_related())
    char_class = serializers.SlugRelatedField(slug_field='pk',required=True,queryset=CharClass.objects.all().select_related())

    class Meta:
        model = CharClassAssociation
        fields = ('pk', 'character','char_class','level')

class GetCharClassByCharacterSerializer(serializers.HyperlinkedModelSerializer):
    character = serializers.SlugRelatedField(slug_field='pk',required=True,queryset=Character.objects.all().select_related())
    char_class = serializers.SlugRelatedField(slug_field='name',required=True,queryset=CharClass.objects.all().select_related())

    class Meta:
        model = CharClassAssociation
        fields = ('pk', 'character','char_class','level')


class RaceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Race
        fields = ('pk', 'name')


class SkillSerializer(serializers.HyperlinkedModelSerializer):
    skill_type = serializers.SlugRelatedField(slug_field='pk',required=True,queryset=SkillType.objects.all().select_related())
    attribute = serializers.SlugRelatedField(slug_field='pk',required=True,queryset=Attribute.objects.all().select_related())
    
    class Meta:
        model = Skill
        fields = ('pk', 'name', 'skill_type','attribute','disscription')


class SkillTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = SkillType
        fields = ('pk', 'name')


class SkillAssociationSerializer(serializers.HyperlinkedModelSerializer):
    character = serializers.SlugRelatedField(slug_field='pk',required=True,queryset=Character.objects.all().select_related())
    skill = serializers.SlugRelatedField(slug_field='pk',required=True,queryset=Skill.objects.all().select_related())
    

    class Meta:
        model = SkillAssociation
        fields = ('pk', 'character', 'skill','rank', 'effect')

class GetSkillAssociationByCharacterSerializer(serializers.HyperlinkedModelSerializer):
    character = serializers.SlugRelatedField(slug_field='pk',required=True,queryset=Character.objects.all().select_related())
    skill = serializers.SlugRelatedField(slug_field='name',required=True,queryset=Skill.objects.all().select_related())
    attribute = serializers.SlugRelatedField(slug_field='attribute',required=True,queryset=Skill.objects.all().select_related())
    skill_type = serializers.SlugRelatedField(slug_field='skill_type',required=True,queryset=Skill.objects.all().select_related())
    

    class Meta:
        model = SkillAssociation
        fields = ('pk', 'character', 'skill','rank', 'effect','attribute','skill_type')


class AttributeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Attribute
        fields = ('pk', 'name', 'disscription')


class AttributeAssociationSerializer(serializers.HyperlinkedModelSerializer):
    character = serializers.SlugRelatedField(slug_field='pk',required=True,queryset=Character.objects.all().select_related())
    attribute = serializers.SlugRelatedField(slug_field='pk',required=True,queryset=Attribute.objects.all().select_related())

    class Meta:
        model = AttributeAssociation
        fields = ('pk', 'character', 'attribute', 'rank', 'effect')


class FeatSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Feat
        fields = ('pk', 'name', 'disscription', 'benefit')


class FeatAssociationSerializer(serializers.HyperlinkedModelSerializer):
    character = serializers.SlugRelatedField(slug_field='pk',required=True,queryset=Character.objects.all().select_related())
    feat = serializers.SlugRelatedField(slug_field='pk',required=True,queryset=Feat.objects.all().select_related())

    class Meta:
        model = FeatAssociation
        fields = ('pk', 'character', 'feat', 'rank')


class ItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Item
        fields = ('pk', 'name', 'weight', 'cost')


class ItemAssociationSerializer(serializers.HyperlinkedModelSerializer):
    character = serializers.SlugRelatedField(slug_field='pk',required=True,queryset=Character.objects.all().select_related())
    item = serializers.SlugRelatedField(slug_field='pk',required=True,queryset=Item.objects.all().select_related())

    class Meta:
        model = ItemAssociation
        fields = ('pk', 'character', 'item', 'amount')


class ArmorSerializer(serializers.HyperlinkedModelSerializer):
    item = serializers.SlugRelatedField(slug_field='pk',required=True,queryset=Item.objects.all().select_related())

    class Meta:
        model = Armor
        fields = ('pk', 'item', 'ac_bonus', 'max_dex', 'check_penalty', 'spell_fail', 'speed')


class ArmorAssociationSerializer(serializers.HyperlinkedModelSerializer):
    armor = serializers.SlugRelatedField(slug_field='pk',required=True,queryset=Armor.objects.all().select_related())
    character = serializers.SlugRelatedField(slug_field='pk',required=True,queryset=Character.objects.all().select_related())

    class Meta:
        model = ArmorAssociation
        fields = ('pk', 'armor','character', 'amount', 'equipped')


class WeaponSerializer(serializers.HyperlinkedModelSerializer):
    item = serializers.SlugRelatedField(slug_field='pk',required=True,queryset=Item.objects.all().select_related())
    weapon_type = serializers.SlugRelatedField(slug_field='pk',required=True,queryset=WeaponType.objects.all().select_related())

    class Meta:
        model = Weapon
        fields = ('pk', 'item', 'weapon_type', 'damage', 'crit', 'range_radius')


class WeaponTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = WeaponType
        fields = ('pk', 'name')


class WeaponAssociationSerializer(serializers.HyperlinkedModelSerializer):
    weapon = serializers.SlugRelatedField(slug_field='pk',required=True,queryset=Weapon.objects.all().select_related())
    character = serializers.SlugRelatedField(slug_field='pk',required=True,queryset=Character.objects.all().select_related())

    class Meta:
        model = WeaponAssociation
        fields = ('pk', 'weapon','character', 'amount', 'equipped')


class SpellSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Spell
        fields = ('pk', 'name', 'disscription')


class SpellAssociationSerializer(serializers.HyperlinkedModelSerializer):
    character = serializers.SlugRelatedField(slug_field='pk',required=True,queryset=Character.objects.all().select_related())
    spell = serializers.SlugRelatedField(slug_field='pk',required=True,queryset=Spell.objects.all().select_related())

    class Meta:
        model = SpellAssociation
        fields = ('pk', 'character', 'spell','prepared')