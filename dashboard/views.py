# from django.forms.widgets import Input
# from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count
from .models import DashboardModel
from .forms import DashboardForm


# Create your views here
def index(request):

	if request.method == 'POST':
		form = DashboardForm(request.POST)

		if form.is_valid():
			form.save()
			messages.success(request, ('Data telah berhasil ditambahkan!'))
		else:
			messages.error(request, 'Data form bermasalah!')

		return redirect("/")

	form = DashboardForm()


	queryset = DashboardModel.objects.values('birth_place').annotate(counter=Count('birth_place')).order_by('birth_place')
	labels = []
	counts = []
	for i in queryset:
		print(i)
		labels.append(i['birth_place'])
		counts.append(i['counter'])

	return render(request, 'dashboard/index.html', { 'form': form, 'labels': labels, 'counts': counts })