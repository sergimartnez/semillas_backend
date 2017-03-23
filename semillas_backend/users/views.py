# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import generics
from rest_framework import permissions
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

from profile_views.models import ProfileViews

from .models import User
from .serializers import UserSerializer
from .permissions import IsOwnerOrReadOnly



class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['name', ]

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)

# used --> View user's profile --> create entry in profile_views table
class UserDetail(generics.RetrieveUpdateAPIView):
    """ access: curl http://0.0.0.0:8000/api/v1/user/2/
    """
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    def get_queryset(self):
        if 'uuid' in self.kwargs:
            pk = self.kwargs['uuid']
            target_user = User.objects.get(uuid=pk)
            ProfileViews.objects.create(
                source_user=self.request.user,
                target_user=target_user,
            )
            return target_user
        
        return Response("The user was not found!", status=status.HTTP_404_NOT_FOUND)



class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
