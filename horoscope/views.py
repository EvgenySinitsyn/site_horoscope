from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
zodiac_dict = {
    "aries": ["Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля)", (3, 21), (4, 20)],
    "taurus": ["Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая)", (4, 21), (5, 21)],
    "gemini": ["Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня)", (5, 22), (6, 21)],
    "cancer": ["Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля)", (6, 22), (7, 22)],
    "leo": ["Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа)", (7, 23), (8, 21)],
    "virgo": ["Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября)", (8, 22), (9, 23)],
    "libra": ["Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)", (9, 24), (10, 23)],
    "scorpio": ["Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября)", (10, 24), (11, 22)],
    "sagittarius": ["Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря)", (11, 23), (12, 22)],
    "capricorn": ["Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января)", (12, 23), (1, 20)],
    "aquarius": ["Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля)", (1, 21),
                 (2, 19)],
    "pisces": ["Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)", (2, 20), (3, 20)],
}

signs_of_types = {
    "fire": ["aries", "leo", "sagittarius"],
    "earth": ["taurus", "virgo", "capricorn"],
    "air": ["gemini", "libra", "aquarius"],
    "water": ["cancer", "scorpio", "pisces"]
}


def get_yyyy_converters(request, sign_zodiac):
    return HttpResponse(f"Вы передали число из 4х цифр - {sign_zodiac}")


def get_my_float_converters(request, sign_zodiac):
    return HttpResponse(f"Вы передали вещественное число - {sign_zodiac}")


def get_my_date_converter(request, sign_zodiac):
    return HttpResponse(f"вы ввели дату - {sign_zodiac}")



def get_info_about_sign_zodiac(request, sign_zodiac: str):
    if sign_zodiac in zodiac_dict:
        zodiacs = list(zodiac_dict)
        description = zodiac_dict.get(sign_zodiac)[0]
    else:
        description = None
    data = {
        'description': description,
        'sign': sign_zodiac,
        'zodiacs': zodiacs,
        'sign_name': description.split()[0],
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > 12:
        return HttpResponseNotFound(f"Знака зодиака с номером {sign_zodiac} не существует")
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse("horoscope_name", args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)


def index(request):
    zodiacs = list(zodiac_dict)
    context = {
        'zodiacs': zodiacs
    }
    return render(request, "horoscope/index.html", context=context)


def types_of_signs(request):
    zodiacs = list(zodiac_dict)
    types = list(signs_of_types.keys())
    context = {
        "types": types,
        "zodiacs": zodiacs
    }
    return render(request, "horoscope/types_of_signs.html", context=context)


def get_signs_of_type(request, type_of_sign: str):
    signs_of_type = signs_of_types[type_of_sign]
    types_rus = {'fire': 'огня', 'water': 'воды', 'air': 'воздуха', 'earth': 'земли'}
    type = types_rus[type_of_sign]
    zodiacs = list(zodiac_dict)
    context = {
        "signs_of_type": signs_of_type,
        "type": type,
        "zodiacs": zodiacs
    }
    return render(request, "horoscope/get_types_of_signs.html", context=context)


def get_sign_from_date(request, month, day):
    if month in (1, 3, 5, 7, 8, 10, 12) and day in range(1, 32) or month in (4, 6, 9, 11) and day in range(1,
                                                                                                           31) or month == 2 and day in range(
            1, 30):
        for sign in zodiac_dict:
            month_beg, day_beg, month_end, day_end = zodiac_dict[sign][1][0], zodiac_dict[sign][1][1], \
                                                     zodiac_dict[sign][2][0], zodiac_dict[sign][2][1]
            if month == month_beg and day >= day_beg or month == month_end and day <= day_end:
                redirect_path = reverse("horoscope_name", args=(sign,))
                return HttpResponseRedirect(redirect_path)
    else:
        return HttpResponse("Такой даты не существует")
