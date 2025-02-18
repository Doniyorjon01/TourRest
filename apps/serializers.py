from rest_framework.serializers import ModelSerializer

from .models import City, Attraction, About, ContactInfo, ContactMessage, Transport, CityImage


class CityModelSerializer(ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class AttractionModelSerializer(ModelSerializer):
    class Meta:
        model = Attraction
        fields = '__all__'

class AboutModelSerializer(ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

class ContactInfoModelSerializer(ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'

class ContactMessageModelSerializer(ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'

class TransportModelSerializer(ModelSerializer):
    class Meta:
        model = Transport
        fields = '__all__'

class CityImageModelSerializer(ModelSerializer):
    class Meta:
        model = CityImage
        fields = '__all__'



