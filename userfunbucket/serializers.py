from bucketadmin.models import Status
from rest_framework import serializers

class StatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'
        depth = 2