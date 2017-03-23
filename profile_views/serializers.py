from rest_framework import serializers
from .models import ProfileViews

class ProfileViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileViews
        fields = ('source_user', 'target_user', 'created_at')