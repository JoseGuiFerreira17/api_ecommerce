from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.viewsets import GenericViewSet


class BaseGenericViewSet(GenericViewSet):
    has_file_field = False
    parser_classes = [JSONParser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    model = None
    serializer_class = None  # Default
    action_serializer_classes = {
        # 'list': None,
        # 'retrieve': None,
        # 'create': None,
        # 'update': None,
        # 'partial_update': None,
        # 'destroy': None,
    }
    filterset_class = None

    def get_queryset(self):
        if self.model:
            return self.model.objects.get_queryset()
        return super().get_queryset()

    def get_serializer_class(self):
        if self.action in self.action_serializer_classes:
            return self.action_serializer_classes[self.action]
        return self.serializer_class

    def get_parsers(self):
        if self.has_file_field:
            self.parser_classes = [MultiPartParser, *self.parser_classes]
        return super().get_parsers()

    @property
    def search_fields(self):
        return self.filterset_class._meta.search_fields if self.filterset_class else []


class ListModelViewSet(BaseGenericViewSet, ListModelMixin):
    pass


class BaseReadOnlyModelViewSet(BaseGenericViewSet, RetrieveModelMixin, ListModelMixin):
    pass


class BaseModelViewSet(
    BaseGenericViewSet,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
):
    pass
