# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from uuid import uuid4

from django.core.urlresolvers import reverse

from django.db import models

from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

# Create your models here.

@python_2_unicode_compatible
class ProfileViews(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)
    
    """Referes to the wallet owned by the user
    that is paying for the service"""
    source_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='outbound_profile_views',
    )

    """Referes to the wallet owned by the user
    that is offering for the service"""
    target_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='inbound_profile_views',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return str(self.id)+" - "+self.source_user.name+" --> "+ str(self.target_user.name)
