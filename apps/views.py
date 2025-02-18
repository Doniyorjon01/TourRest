from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView

from apps.models import City, Attraction, About, Transport, ContactMessage, CityImage
from apps.serializers import CityModelSerializer, AttractionModelSerializer, AboutModelSerializer, \
    TransportModelSerializer, ContactMessageModelSerializer, CityImageModelSerializer


@extend_schema(
    tags=['city'])
class CityCreateAPIView(CreateAPIView):
    serializer_class = CityModelSerializer
    queryset = City.objects.all()

@extend_schema(tags=['city'])
class CityListAPIView(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CityModelSerializer

@extend_schema(
    tags=['city'])
class CityUpdateAPIView(UpdateAPIView):
    queryset = City.objects.all()
    serializer_class = CityModelSerializer
    lookup_field = 'pk'

@extend_schema(
    tags=['city'])
class CityDeleteAPIView(DestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CityModelSerializer
    lookup_field = 'pk'

# @extend_schema(
#     tags=['attraction'])
# class AttractionCreateAPIView(CreateAPIView):
#     queryset = Attraction.objects.all()
#     serializer_class = AttractionModelSerializer
#
# @extend_schema(
#     tags=['attraction'])
# class AttractionListAPIView(ListAPIView):
#     queryset = Attraction.objects.all()
#     serializer_class = AttractionModelSerializer
#
# @extend_schema(
#     tags=['attraction'])
# class AttractionUpdateAPIView(UpdateAPIView):
#     queryset = Attraction.objects.all()
#     serializer_class = AttractionModelSerializer
#     lookup_field = 'pk'
#
# @extend_schema(
#     tags=['attraction'])
# class AttractionDeleteAPIView(DestroyAPIView):
#     queryset = Attraction.objects.all()
#     serializer_class = AttractionModelSerializer
#     lookup_field = 'pk'

#   ---------------------- City-Attraction -------------------------

@extend_schema(
    tags=['city-attraction'])
class CityAttractionsListView(ListAPIView):
    serializer_class = AttractionModelSerializer

    def get_queryset(self):
        city_id = self.kwargs['city_id']
        return Attraction.objects.filter(city_id=city_id)

@extend_schema(
    tags=['city-attraction'])
class CityAttractionCreateView(CreateAPIView):
    serializer_class = AttractionModelSerializer

    def perform_create(self, serializer):
        city_id = self.kwargs['city_id']
        city = City.objects.get(id=city_id)
        serializer.save(city=city)

@extend_schema(
    tags=['city-attraction'])
class CityAttractionUpdateView(UpdateAPIView):
    queryset = Attraction.objects.all()
    serializer_class = AttractionModelSerializer

@extend_schema(
    tags=['city-attraction'])
class CityAttractionDeleteView(DestroyAPIView):
    queryset = Attraction.objects.all()
    serializer_class = AttractionModelSerializer

#  -------------- About -------------------------

@extend_schema(
    tags=['about-us'])
class AboutCreateAPIView(CreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutModelSerializer

@extend_schema(
    tags=['about-us'])
class AboutListAPIView(ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutModelSerializer

@extend_schema(
    tags=['about-us'])
class AboutUpdateAPIView(UpdateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutModelSerializer
    lookup_field = 'pk'

@extend_schema(
    tags=['about-us'])
class AboutDeleteAPIView(DestroyAPIView):
    queryset = About.objects.all()
    serializer_class = AboutModelSerializer
    lookup_field = 'pk'

# -------------  Transport  -----------------------

@extend_schema(
    tags=['transport'])
class TransportCreateAPIView(CreateAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportModelSerializer

@extend_schema(
    tags=['transport'])
class TransportListAPIView(ListAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportModelSerializer

@extend_schema(
    tags=['transport'])
class TransportUpdateAPIView(UpdateAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportModelSerializer
    lookup_field = 'pk'

@extend_schema(
    tags=['transport'])
class TransportDeleteAPIView(DestroyAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportModelSerializer
    lookup_field = 'pk'

#  -------------- Send Message  --------------

@extend_schema(
    tags=['send-message'])
class SendMessageCreateAPIView(CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageModelSerializer

@extend_schema(
    tags=['send-message'])
class SendMessageListAPIView(ListAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageModelSerializer

#    -----------  City Image  ------------

class CityImageCreateAPIView(CreateAPIView):
    queryset = CityImage.objects.all()
    serializer_class = CityImageModelSerializer

    def perform_create(self, serializer):
        city_id = self.kwargs['cityid']
        city = City.objects.get(id=city_id)
        serializer.save(city=city)

class CityImageListAPIView(ListAPIView):
    queryset = CityImage.objects.all()
    serializer_class = CityImageModelSerializer

    def get_queryset(self):
        city_id = self.kwargs['cityid']
        return CityImage.objects.filter(city_id=city_id)

class CityImageUpdateAPIView(UpdateAPIView):
    queryset = CityImage.objects.all()
    serializer_class = CityImageModelSerializer

    def get_object(self):
        city_id = self.kwargs['cityid']
        image_id = self.kwargs['imageid']
        return CityImage.objects.get(id=image_id, city_id=city_id)

@extend_schema(
    tags=['cityimage'])
class CityImageDeleteAPIView(DestroyAPIView):
    queryset = CityImage.objects.all()
    serializer_class = CityImageModelSerializer
    lookup_field = 'pk'


