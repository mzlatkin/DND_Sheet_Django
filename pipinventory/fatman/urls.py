from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from fatman import views

urlpatterns = format_suffix_patterns([
    url(r'^$', api_root),
    url(r'^character_detail/get_details_by_character/(?P<character>[0-9])/$', get_details_by_character, name='get_details_by_character'),
])