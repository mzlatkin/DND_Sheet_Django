from django.conf.urls import url, include
from rest_framework import routers
from fatman import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'character', views.CharacterViewSet)
router.register(r'character_detail', views.CharacterDetailViewSet)
router.register(r'char_class', views.CharClassViewSet)
router.register(r'size', views.SizeViewSet)
router.register(r'char_class_association', views.CharClassAssociationViewSet)
router.register(r'race', views.RaceViewSet)
router.register(r'skill', views.SkillViewSet)
router.register(r'skillType', views.SkillTypeViewSet)
router.register(r'skill_association', views.SkillAssociationViewSet)
router.register(r'attribute', views.AttributeViewSet)
router.register(r'attribute_association', views.AttributeAssociationViewSet)
router.register(r'feat', views.FeatViewSet)
router.register(r'feat_association', views.FeatAssociationViewSet)
router.register(r'item', views.ItemViewSet)
router.register(r'item_association', views.ItemAssociationViewSet)
router.register(r'armor', views.ArmorViewSet)
router.register(r'armor_association', views.ArmorAssociationViewSet)
router.register(r'weapon', views.WeaponViewSet)
router.register(r'weaponType', views.WeaponTypeViewSet)
router.register(r'weapon_association', views.WeaponAssociationViewSet)
router.register(r'spells', views.SpellsViewSet)
router.register(r'spells_association', views.SpellsAssociationViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
