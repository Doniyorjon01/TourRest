from django.urls import path

from apps.views import (CityCreateAPIView, CityListAPIView, CityDeleteAPIView, CityUpdateAPIView,
    # AttractionCreateAPIView, AttractionListAPIView, AttractionUpdateAPIView,AttractionDeleteAPIView,
                        CityAttractionsListView, CityAttractionCreateView,
                        CityAttractionUpdateView, CityAttractionDeleteView, AboutCreateAPIView, AboutListAPIView,
                        AboutUpdateAPIView, AboutDeleteAPIView, TransportCreateAPIView, TransportListAPIView,
                        TransportUpdateAPIView, TransportDeleteAPIView, SendMessageCreateAPIView,
                        SendMessageListAPIView, CityImageCreateAPIView, CityImageListAPIView, CityImageUpdateAPIView)




urlpatterns = [
    path('city/create', CityCreateAPIView.as_view()),
    path('city/list', CityListAPIView.as_view()),
    path('city/delete/<int:pk>', CityDeleteAPIView.as_view()),
    path('city/update/<int:pk>', CityUpdateAPIView.as_view()),

    # path('attraction/create', AttractionCreateAPIView.as_view()),
    # path('attraction/list', AttractionListAPIView.as_view()),
    # path('attraction/update/<int:pk>', AttractionUpdateAPIView.as_view()),
    # path('attraction/delete/<int:pk>', AttractionDeleteAPIView.as_view()),

    path('cities/<int:city_id>/attractions/', CityAttractionsListView.as_view()),
    path('cities/<int:city_id>/attractions/create/', CityAttractionCreateView.as_view()),
    path('cities/<int:city_id>/attractions/<int:pk>/update/', CityAttractionUpdateView.as_view()),
    path('cities/<int:city_id>/attractions/<int:pk>/delete/', CityAttractionDeleteView.as_view()),


    path('about/create', AboutCreateAPIView.as_view()),
    path('about/list', AboutListAPIView.as_view()),
    path('about/update/<int:pk>', AboutUpdateAPIView.as_view()),
    path('about/delete/<int:pk>', AboutDeleteAPIView.as_view()),

    path('transport/create', TransportCreateAPIView.as_view()),
    path('transport/list', TransportListAPIView.as_view()),
    path('transport/update/<int:pk>', TransportUpdateAPIView.as_view()),
    path('transport/delete/<int:pk>', TransportDeleteAPIView.as_view()),

    path('send-message/create', SendMessageCreateAPIView.as_view()),
    path('send-message/list', SendMessageListAPIView.as_view()),

    path('city/<int:cityid>/images/', CityImageCreateAPIView.as_view()),
    path('city/<int:cityid>/images/', CityImageListAPIView.as_view()),
    path('city/<int:cityid>/images/<int:imageid>/', CityImageUpdateAPIView.as_view()),
    path('cityimage/delete/<int:cityid>', CityDeleteAPIView.as_view()),
]
