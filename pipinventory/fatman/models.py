from django.db import models


class Character(models.Model):
    account = models.ForeignKey('auth.User', related_name='account')
    name = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active =  models.BooleanField(default=True)
    
    class Meta:
        ordering = ('character_name',)

class CharacterDetail(models.Model):
    character = models.ForeignKey(Character, related_name='character_detail')
    gender = models.TextField(default='')
    level = models.IntegerField(default=0)
    deity = models.TextField(default='')
    alignment = models.TextField(default='')
    base_attack_bonus = models.IntegerField(default=0)    
    
    class Meta:
        ordering = ('character',)