from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import GeneralWord, UserWord
from .serializers import (
    GeneralWordSerializer,
    UserWordSerializer,
    SimpleGeneralWordSerializer
)
from .permissions import IsOwnerOrReadOnly
from pagination import PagePageListPagination

class GeneralWordViewSet(
        GenericViewSet,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,):

    serializer_class = GeneralWordSerializer
    queryset = GeneralWord.objects.all()
    model = GeneralWord
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ("title", "title_ar",)
    pagination_class = PagePageListPagination

    def list(self, request, *args, **kwargs):
        self.serializer_class = SimpleGeneralWordSerializer
        return super(GeneralWordViewSet, self).list(request,
                                                    *args,
                                                    **kwargs)


class UserWordViewSet(
        GenericViewSet,
        mixins.CreateModelMixin,
        mixins.DestroyModelMixin,
        mixins.RetrieveModelMixin,):

    serializer_class = UserWordSerializer
    queryset = UserWord.objects.all()
    model = UserWord
    permission_classes = (IsOwnerOrReadOnly,)
