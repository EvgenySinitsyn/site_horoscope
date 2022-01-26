from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
week_days = {
    "monday": "Это понедельник",
    "tuesday": "Это вторник",
    "wednesday": "Это среда",
    "thursday": "Это четверг",
    "friday": "Это пятница",
    "saturday": "Это суббота",
    "sunday": "Это воскресенье",
}

def plan_for_week_day(request, week_day: str):
    return render(request, 'week_days/greeting.html')



def plan_for_week_day_by_number(response, week_day: int):
    days = list(week_days)
    if week_day > 7:
        return HttpResponseNotFound(f"Неправильный номер дня недели - {week_day}")
    day = days[week_day - 1]
    redirect_url = reverse('week_days', args=(day, ))
    return HttpResponseRedirect(redirect_url)
