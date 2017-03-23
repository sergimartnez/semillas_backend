# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import generics
from rest_framework import permissions

from semillas_backend.users.models import User

from django.contrib.gis.db.models.functions import Distance

from .models import ProfileViews

from .serializers import ProfileViewsSerializer


class ProfileViewHistoryList(generics.ListAPIView):
    serializer_class = ProfileViewsSerializer
    permission_classes = (permissions.AllowAny,)
    def get_queryset(self):
        if 'user_uuid' in self.kwargs:
            pk = self.kwargs['user_uuid']
            u=User.objects.get(uuid=pk)
            if u:
                return ProfileViews.objects.filter(source_user=u.id)
        else:
            return ProfileViews.objects.all()