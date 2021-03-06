from utils.viewsets import ModelFilterViewSet

from .user_serializers import UserSerializer
from django.contrib.auth.models import User

from .permission import IsSiteAdmin

from .user_filters import UserFilter


class UserViewSet(ModelFilterViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = (IsSiteAdmin,)
    filter_class = UserFilter
    search_fields = ('username', 'first_name', 'last_name')
    ordering_fields = ('username', 'email')
