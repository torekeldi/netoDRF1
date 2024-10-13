from django.urls import path

from measurement.views import SensorView, SingleSensorView, MeasurementView

urlpatterns = [
    path('v1/sensors/', SensorView.as_view()),
    path('v1/sensor/<pk>/', SingleSensorView.as_view()),
    path('v1/measurement/', MeasurementView.as_view()),
]
