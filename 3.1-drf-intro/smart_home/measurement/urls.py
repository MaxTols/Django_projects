from django.urls import path
from .views import SensorView, SensorSingleView, MeasurementView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<int:pk>/', SensorSingleView.as_view()),
    path('measurements/', MeasurementView.as_view()),
]
