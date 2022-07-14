from django.shortcuts import render
from datetime import datetime
from .models import Tracker
from .forms import TrackerForm
from django.http import HttpResponseRedirect


def home(request):
	now = datetime.now()
	current_year = now.year

	return render(request, 'tracker/home.html', {
		"current_year": current_year,
		})

def admin(request):
	now = datetime.now()
	current_year = now.year

	return render(request, 'tracker/admin.html', {
		"current_year": current_year,
		})

def it(request):
	now = datetime.now()
	current_year = now.year

	return render(request, 'tracker/it.html', {
		"current_year": current_year,
		})

def production(request):
	now = datetime.now()
	current_year = now.year

	return render(request, 'tracker/production.html', {
		"current_year": current_year,
		})

def sales(request):
	sales_orders = Tracker.objects.all()
	now = datetime.now()
	current_year = now.year

	submitted = False
	if request.method == "POST":
		form = TrackerForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/tracker/sales?submitted=True')
	else:
		form = TrackerForm
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'tracker/sales.html', {
		"current_year": current_year, "sales_orders": sales_orders, "form":form, "submitted":submitted
		})