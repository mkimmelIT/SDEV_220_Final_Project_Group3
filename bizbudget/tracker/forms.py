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
			'requester': '',
			'description': '',
			'quantity': '',
			'price': '',
		}
		widgets = {
			'department': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Department'}),
			'date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Date YYYY-MM-DD'}),
			'requester': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Requester Name'}),
			'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Item Description'}),
			'quantity': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Quantity'}),
			'price': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Price'}),
		}
