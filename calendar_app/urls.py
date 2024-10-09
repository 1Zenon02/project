from django.urls import path

from . import views
from .views import add_event_view, calendar_view

urlpatterns = [
    path('', views.calendar_view, name='calendar'),
    path('add/', views.add_event, name='add_event'),
    path('', views.monthly_calendar_view, name='monthly_calendar'),

    path('', calendar_view, name='calendar_view'),

    path('calendar/add/<int:day>/<int:month>/<int:year>/', add_event_view, name='add_event'),
]