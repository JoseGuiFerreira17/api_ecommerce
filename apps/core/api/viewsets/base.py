from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.permissions import DjangoObjectPermissions, IsAuthenticated
from rest_framework.viewsets import GenericViewSet


class BaseGenericViewSet(GenericViewSet):
    permission_classes = [DjangoObjectPermissions, IsAuthenticated]
    parser_classes = [JSONParser]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    model = None
    serializer_class = None

    def get_queryset(self):
        if self.model:
            return self.model.objects.get_queryset()
        return super().get_queryset()

    def get_serializer_class(self):
        if self.action in self.action_serializer_classes:
            return self.action_serializer_classes[self.action]
        return self.serializer_class


class ListModelViewSet(BaseGenericViewSet, ListModelMixin):
    pass


class BaseReadOnlyModelViewSet(BaseGenericViewSet, RetrieveModelMixin, ListModelMixin):
    pass


class BaseModelViewSet(
    BaseGenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin
):
    pass
