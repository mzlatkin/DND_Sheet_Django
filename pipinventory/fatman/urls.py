from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from fatman import views

urlpatterns = format_suffix_patterns([
    url(r'^$', api_root),
    url(r'^character_detail/get_details_by_character/(?P<character>[0-9])/$', character_detail_detail, name='get_details_by_character'),
    url(r'^char_class_association/get_char_class_by_character/(?P<character>[0-9])/$', char_class_association_detail, name='get_char_class_by_character'),
    url(r'^skill_association/get_skill_association_by_character/(?P<character>[0-9])/$', skill_association_detail, name='get_skill_association_by_character'),
    url(r'^attribute_association/get_attribute_association_by_character/(?P<character>[0-9])/$', attribute_association_detail, name='get_attribute_association_by_character'),
    url(r'^feat_association/get_feat_association_by_character/(?P<character>[0-9])/$', feat_association_detail, name='get_feat_association_by_character'),
    url(r'^item_association/get_item_association_by_character/(?P<character>[0-9])/$', item_association_detail, name='get_item_association_by_character'),
    url(r'^armor_association/get_armor_association_by_character/(?P<character>[0-9])/$', armor_association_detail, name='get_armor_association_by_character'),
    url(r'^weapon_association/get_weapon_association_by_character/(?P<character>[0-9])/$', weapon_association_detail, name='get_weapon_association_by_character'),
    url(r'^spell_association/get_spell_association_by_character/(?P<character>[0-9])/$', spell_association_detail, name='get_spell_association_by_character'),
])