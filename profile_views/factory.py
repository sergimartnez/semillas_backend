# -*- coding: utf-8 -*-

import factory
import faker
import datetime

from django.conf import settings

from .models import ProfileViews
from semillas_backend.users.models import User

faker = faker.Factory.create()

class ProfileViewsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProfileViews

    source_user = factory.Iterator(User.objects.all())
    target_user = factory.Iterator(User.objects.all())