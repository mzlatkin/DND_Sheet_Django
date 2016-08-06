from django.db import models

class Character(models.Model):
    account = models.ForeignKey('auth.User', related_name='account')
    name = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active =  models.BooleanField(default=True)
    
    class Meta:
        ordering = ('name',)

class CharacterDetail(models.Model):
    character = models.ForeignKey(Character, related_name='character_detail')
    #size = models.ForeignKey(Size, related_name='character_detail')
    gender = models.TextField(default='')
    deity = models.TextField(default='')
    alignment = models.TextField(default='')
    base_attack_bonus = models.IntegerField(default=0)    
    
    class Meta:
        ordering = ('character',)

class CharClass(models.Model):
    name = models.TextField(default='')

    class Meta:
        ordering = ('name',)

class Size(models.Model):
    size = models.TextField(default='')

    class Meta:
        ordering = ('name',)

class CharClassAssociation(models.Model):
    character = models.ForeignKey(Character, related_name='char_class_association')
    char_class = models.ForeignKey(CharClass, related_name='char_class_association')
    level = models.IntegerField(default=0)
    
    class Meta:
        ordering = ('level',)

class Race(models.Model):
    name = models.TextField(default='')

    class Meta:
        ordering = ('name',)

class Skill(models.Model):
    name = models.TextField(default='')
    disscription = models.TextField(default='')

    class Meta:
        ordering = ('name',)

class SkillType(models.Model):
    name = models.TextField(default='')

    class Meta:
        ordering = ('name',)

class SkillAssociation(models.Model):
    character = models.ForeignKey(Character, related_name='skill_association')
    skill = models.ForeignKey(Skill, related_name='skill_association')
    attribute = models.ForeignKey(Attribute, related_name='skill_association')
    skill_type = models.ForeignKey(SkillType, related_name='skill_association')
    rank = models.IntegerField(default=0)
    effect = models.IntegerField(default=0)
    
    class Meta:
        ordering = ('skill',)

class Attribute(models.Model):
    name = models.TextField(default='')
    disscription = models.TextField(default='')

    class Meta:
        ordering = ('name',)

class AttributeAssociation(models.Model):
    character = models.ForeignKey(Character, related_name='attribute_association')
    attribute = models.ForeignKey(Attribute, related_name='attribute_association')
    rank = models.IntegerField(default=0)
    effect = models.IntegerField(default=0)
    
    class Meta:
        ordering = ('attribute',)

class Feat(models.Model):
    name = models.TextField(default='')
    disscription = models.TextField(default='')
    benefit = models.TextField(default='')

    class Meta:
        ordering = ('name',)

class FeatAssociation(models.Model):
    character = models.ForeignKey(Character, related_name='feat_association')
    feat = models.ForeignKey(Feat, related_name='feat_association')
    rank = models.IntegerField(default=0)
    
    class Meta:
        ordering = ('feat',)

class Item(models.Model):
    name = models.TextField(default='')
    weight = models.TextField(default='')
    cost = models.TextField(default='')
    
    class Meta:
        ordering = ('name',)

class ItemAssociation(models.Model):
    character = models.ForeignKey(Character, related_name='item_association')
    item = models.ForeignKey(Item, related_name='item_association')
    amount = models.IntegerField(default=0)
    
    class Meta:
        ordering = ('item',)

class Armor(models.Model):
    item = models.ForeignKey(Item, related_name='armor')
    ac_bonus = models.IntegerField(default=0)
    max_dex = models.IntegerField(default=0)
    check_penalty = models.IntegerField(default=0)
    spell_fail = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    
    class Meta:
        ordering = ('name',)

class ArmorAssociation(models.Model):
    armor = models.ForeignKey(Armor, related_name='armor_association')
    item = models.ForeignKey(Item, related_name='armor_association')
    amount = models.IntegerField(default=0)
    equiped = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('item',)

class Weapon(models.Model):
    item = models.ForeignKey(Item, related_name='weapon')
    weapon_type = models.ForeignKey(WeaponType, related_name='weapon')
    damage = models.TextField(default='')
    crit = models.TextField(default='')
    range_radius = models.TextField(default='')
    speed = models.IntegerField(default=0)
    
    class Meta:
        ordering = ('name',)

class WeaponType(models.Model):
    weapon_type = models.TextField(default='')

    class Meta:
        ordering = ('weapon_type',)

class WeaponAssociation(models.Model):
    weapon = models.ForeignKey(Weapon, related_name='weapon_association')
    item = models.ForeignKey(Item, related_name='weapon_association')
    amount = models.IntegerField(default=0)
    equiped = models.BooleanField(default=False)

    class Meta:
        ordering = ('item',)

class Spells(models.Model):
    name = models.TextField(default='')
    disscription = models.TextField(default='')

    class Meta:
        ordering = ('name',)

class SpellsAssociation(models.Model):
    character = models.ForeignKey(Character, related_name='spells_association')
    spells = models.ForeignKey(Spells, related_name='spells_association')
    Prepared = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('spells',)