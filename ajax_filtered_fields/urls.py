from django.conf.urls import patterns

from ajax_filtered_fields import settings
from ajax_filtered_fields.views import json_index

if settings.AUTH_DECORATOR:
    json_index = settings.AUTH_DECORATOR(json_index)

urlpatterns = patterns('',
    (r'^json_index/$', json_index),
)
