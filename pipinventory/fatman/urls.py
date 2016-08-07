from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from fatman import views

urlpatterns = format_suffix_patterns([
    url(r'^$', api_root),
    url(r'^character_detail/get_details_by_character/(?P<character>[0-9])/$', character_detail_detail, name='get_details_by_character'),
    url(r'^char_class_association/get_char_class_by_character/(?P<character>[0-9])/$', char_class_association_detail, name='get_char_class_by_character'),
    url(r'^skill_association/get_skill_association_by_character/(?P<character>[0-9])/$', skill_association_detail, name='get_skill_association_by_character'),
])