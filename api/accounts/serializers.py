from rest_framework import serializers
from api.users.models import User
from api.users.mixins import UserAvatarLinkSerializerMixin


class ProfileSerializer(
    UserAvatarLinkSerializerMixin,
    serializers.ModelSerializer,
):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "is_email_verified",
            "username",
            "name",
            "phone_number",
            "avatar",
            "date_joined",
            "is_superuser",
            "is_staff",
            "links",
        )
        read_only_fields = (
            "date_joined",
            "last_login",
            "email",
            "is_active",
            "is_staff",
            "is_superuser",
            "phone_number",
            "total_xp",
            "rank",
        )
        extra_kwargs = {"avatar": {"write_only": True}}
