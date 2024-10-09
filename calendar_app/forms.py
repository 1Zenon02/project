from django import forms
from .models import WorkEvent

class WorkEventForm(forms.ModelForm):
    class Meta:
        model = WorkEvent
        fields = ['title', 'description', 'start_time', 'end_time']

