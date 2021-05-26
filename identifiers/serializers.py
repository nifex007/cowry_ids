from rest_framework import serializers
from identifiers.models import Identifier
from uuid import UUID


class IdentifiersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Identifier
        fields = '__all__'

    def to_representation(self, instance):
        identifiers = {}
        for identifier in instance:
            date_time_string = identifier.created_at.strftime("%Y-%m-%d %H:%M:%S.%f")
            uuid_ = UUID(str(identifier.id)).hex
            identifiers[date_time_string] = uuid_
        return identifiers


