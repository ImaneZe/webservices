# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template.response import TemplateResponse

from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet

from shop.serializers import *
from shop.models import Shop


def index_view(request):
    context = {}
    return TemplateResponse(request, 'index.html', context)


class ShopViewSet(MongoModelViewSet):
    lookup_field = 'id'
    serializer_class = ShopSerializer

    def get_queryset(self):
        print Shop.objects.all()
        return Shop.objects.all()

