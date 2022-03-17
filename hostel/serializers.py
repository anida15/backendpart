from rest_framework import serializers

from .models import Hostel


class HostelSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)

    class Meta:
        model = Hostel
        fields = ('id', 'name', 'description', 'price', 'image')