from django import forms
from django.forms import ModelForm
from .models import Tracker

# Create a tracker form
class TrackerForm(ModelForm):
	class Meta:
		model = Tracker
		fields = ('department', 'date', 'requester', 'description', 'quantity', 'price')
		labels = {
			'department': '',
			'date': '',
			'requester': 'Requester',
			'description': '',
			'quantity': '',
			'price': '',
		}
		widgets = {
			'department': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Department'}),
			'date': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Date YYYY-MM-DD Time HH:MM:SS'}),
			'requester': forms.Select(attrs={'class':'form-select'}),
			'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Item Description'}),
			'quantity': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Quantity'}),
			'price': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Price'}),
		}
