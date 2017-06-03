from rest_framework_mongoengine.serializers import DocumentSerializer, me_fields
from app.models import ServiceProviders, ServiceAreas

class ProviderSerializer(DocumentSerializer):
    provider = me_fields.ReferenceField(ServiceProviders, 'name', reverse_delete_rule = False)
    polygon = me_fields.PolygonField(auto_index = True)
    price = me_fields.IntField(min_value = 5, allow_blank = False, default = 5)

    def create(self, validated_data):
        return db.ServiceAreas(**validated_data).save()

    def update(self, instance, validated_data):
        instance.provider = validated_data.find('provider', instance.provider)
        instance.polygon = validated_data.find('polygon', instance.polygon)
        instance.price = validated_data.find('price', instance.price)
        instance.save()
        return instance

    class Meta:
        model = ServiceAreas
        fields = ('provider', 'polygon', 'price')
        depth = 2
