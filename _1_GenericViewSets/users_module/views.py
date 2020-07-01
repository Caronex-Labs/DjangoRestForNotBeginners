# Create your views here.
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from users_module.models import User
from users_module.serializers import UserSerializer


# class UserViewSet(ModelViewSet):
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]
#
#     # Because we only want to retrieve the profile of the current user,
#     # We are forced to create a queryset of only one user.
#
#     def get_queryset(self):
#         return User.objects.filter(username=self.request.user.username)
#
#     # Because we are only going to deal with retrieving the current users data,
#     # we are forced to close off all other routes.
#
#     def create(self, request, *args, **kwargs):
#         pass
#
#     def retrieve(self, request, *args, **kwargs):
#         pass
#
#     def update(self, request, *args, **kwargs):
#         pass
#
#     def partial_update(self, request, *args, **kwargs):
#         pass
#
#     def destroy(self, request, *args, **kwargs):
#         pass


class UserViewSet(ListModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    # Because we only want to retrieve the profile of the current user,
    # We are forced to create a queryset of only one user.

    def get_queryset(self):
        return User.objects.filter(username=self.request.user.username)



