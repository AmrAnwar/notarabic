
from django.contrib.gis.geoip2 import GeoIP2
from django.http import HttpResponse, Http404, HttpResponseRedirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action


from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import GeneralWord, UserWord, WordTimeStamp
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

    def retrieve(self, request, *args, **kwargs):
        self.create_word_timestamp(request)
        return super().retrieve(request, *args, **kwargs)


    def list(self, request, *args, **kwargs):
        self.serializer_class = SimpleGeneralWordSerializer
        return super(GeneralWordViewSet, self).list(request,
                                                    *args,
                                                    **kwargs)
    def create_word_timestamp(self, request):
        g = GeoIP2()
        try:
            requested_location = g.country_name(request.META['REMOTE_ADDR'])
        except:
            requested_location="Unknown"
        WordTimeStamp.objects.create(word=self.get_object(), location=requested_location).save()


class UserWordViewSet(
        GenericViewSet,
        mixins.CreateModelMixin,
        mixins.DestroyModelMixin,
        mixins.RetrieveModelMixin,):

    serializer_class = UserWordSerializer
    queryset = UserWord.objects.all()
    model = UserWord
    permission_classes = (IsOwnerOrReadOnly,)

    @action(detail=True, methods=['get'], url_path='up')
    def up_vote(self, request, pk=None):
        current_word = self.get_object()
        if not current_word.up_vote.filter(id = request.user.id):
            if current_word.down_vote.filter(id=request.user.id):
                current_word.down_vote.remove(request.user)
            current_word.up_vote.add(request.user)
        return Response(self.get_serializer(current_word).data,status = status.HTTP_200_OK)



    @action(detail=True, methods=['get'], url_path='down')
    def down_vote(self, request, pk=None):
        current_word = self.get_object()
        if not current_word.down_vote.filter(id = request.user.id):
            if current_word.up_vote.filter(id=request.user.id):
                current_word.up_vote.remove(request.user)
            current_word.down_vote.add(request.user)
        return Response(self.get_serializer(current_word).data, status=status.HTTP_200_OK)

