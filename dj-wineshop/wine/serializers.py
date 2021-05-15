from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

from .models import *

class WineSerializer(serializers.ModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model = Wine
        fields = ("id", "name", "quantity", "image", "tags")
