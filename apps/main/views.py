from django.shortcuts import render

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import PageNumberPagination
from apps.main.models import Books
from apps.main.serializers import BookSerializers


class Pagination(PageNumberPagination):
    page_size=3
    max_page_size=10



class BookAPI(GenericViewSet,
            mixins.ListModelMixin,
            mixins.CreateModelMixin,
            mixins.RetrieveModelMixin,
            mixins.DestroyModelMixin,
            mixins.UpdateModelMixin,
              ):
    queryset=Books.objects.all()
    serializer_class=BookSerializers
    pagination_class=Pagination




