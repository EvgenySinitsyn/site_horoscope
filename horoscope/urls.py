from django.urls import path, register_converter, converters
from . import views, converters

register_converter(converters.MyDateConverter, 'my_date')
register_converter(converters.FoundDigitYearConverter, 'yyyy')
register_converter(converters.MyFloatConverter, 'my_float')



urlpatterns = [
    path('', views.index, name="horoscope_index"),
    path('<my_date:sign_zodiac>', views.get_my_date_converter),
    path('types/', views.types_of_signs),
    path('<int:month>/<int:day>', views.get_sign_from_date),
    path('types/<str:type_of_sign>', views.get_signs_of_type, name="type_name"),
    path('<yyyy:sign_zodiac>', views.get_yyyy_converters),
    path('<int:sign_zodiac>', views.get_info_about_sign_zodiac_by_number),
    path('<my_float:sign_zodiac>', views.get_my_float_converters),
    path('<str:sign_zodiac>', views.get_info_about_sign_zodiac, name='horoscope_name'),

]