# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the ServiceListView
    url(
        regex=r'^user/(?P<user_uuid>[^/]+)/$',
        view=views.ProfileViewHistoryList.as_view(),
        name='list'
    ),
]
