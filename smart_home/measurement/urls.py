from django.urls import path
from .views import SensorViewAll, SensorUpdate, MeasurementView, SensorView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorViewAll.as_view()),
    path('sensors/update/<pk>/', SensorUpdate.as_view()),
    path('measurements/', MeasurementView.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),

]
