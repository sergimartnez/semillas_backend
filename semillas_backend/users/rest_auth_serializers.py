from rest_framework import serializers
from drf_extra_fields.geo_fields import PointField
from rest_auth.models import TokenModel
from .serializers import FullUserSerializer



class TokenSerializer(serializers.ModelSerializer):
    """
    Serializer for Token model.
    """

    user = FullUserSerializer()

    class Meta:
        model = TokenModel
        fields = ('key', 'user')
