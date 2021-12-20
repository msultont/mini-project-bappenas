from django import forms
from django.forms import fields
from .models import DashboardModel

class DashboardForm(forms.ModelForm):
	class Meta:
		model = DashboardModel
		fields = "__all__"