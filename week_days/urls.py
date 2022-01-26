from django.urls import path
from . import views


urlpatterns = [
    path('<int:week_day>/', views.plan_for_week_day_by_number),
    path('<str:week_day>/', views.plan_for_week_day, name='week_days'),
]