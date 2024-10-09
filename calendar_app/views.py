import calendar
from datetime import datetime
from django.utils import timezone
from django.shortcuts import redirect, render
from .forms import WorkEventForm
from .models import WorkEvent


from django.shortcuts import render, redirect
from django.utils import timezone
from .models import WorkEvent
from .forms import WorkEventForm
import calendar
from collections import defaultdict

def calendar_view(request):
    today = timezone.now()
    month = today.month
    year = today.year

    # Creating a monthly calendar
    month_days = calendar.monthcalendar(year, month)

    # Get all events for the current month
    events = WorkEvent.objects.filter(start_time__year=year, start_time__month=month)
    events_dict = defaultdict(list)
    for event in events:
        events_dict[event.start_time.day].append(event)

    return render(request, 'calendar_app/calendar.html', {
        'month_days': month_days,
        'year': year,
        'month': month,
        'events_dict': events_dict,
    })

def add_event_view(request, day, month, year):
    if request.method == 'POST':
        form = WorkEventForm(request.POST)
        if form.is_valid():
            work_event = form.save(commit=False)
            work_event.start_time = timezone.datetime(year, month, day, 0, 0)
            work_event.end_time = work_event.start_time + timezone.timedelta(hours=1)
            work_event.save()
            return redirect('calendar_view')
    else:
        form = WorkEventForm()

    return render(request, 'calendar_app/add_event.html', {'form': form, 'day': day, 'month': month, 'year': year})


def add_event_view(request, day, month, year):
    if request.method == 'POST':
        form = WorkEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.start_time = timezone.datetime(year, month, day)  # Set the event start time
            event.save()
            return redirect('calendar_view')  # Redirect to the calendar view after saving
    else:
        form = WorkEventForm()

    return render(request, 'calendar_app/add_event.html', {
        'form': form,
        'day': day,
        'month': month,
        'year': year
    })


def add_event(request):
    return None