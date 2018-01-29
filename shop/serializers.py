from rest_framework import serializers
from rest_framework_mongoengine import serializers as mongoserializers

from shop.models import Shop


class ShopSerializer(mongoserializers.DocumentSerializer):
    class Meta:
        model = Shop
        fields = '__all__'