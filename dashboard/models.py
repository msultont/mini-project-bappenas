from django.db import models

# Create your models here.
class DashboardModel(models.Model):

	CHOICES = (
		('Islam', 'Islam'),
		('Katholik', 'Katholik'),
		('Protestan', 'Protestan'),
		('Hindu', 'Hindu'),
		('Buddha', 'Buddha')
	)

	full_name = models.CharField(max_length=30)
	birth_place = models.CharField(max_length=30)
	birth_date = models.DateTimeField()
	place = models.CharField(max_length=25)
	religion = models.CharField(max_length=25, choices=CHOICES)

	def __str__(self):
		return self.full_name