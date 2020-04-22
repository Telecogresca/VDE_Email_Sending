from django.db import models


# Create your models here.
class Torn(models.Model):
	date=models.CharField("data", max_length=150, blank=True)
	day_of_week=models.CharField("dia", max_length=150, blank=True)
	num_day=models.CharField("numDia", max_length=15, blank=True)
	start_h=models.CharField("hInici", max_length=15, blank=True)
	finish_h=models.CharField("hFinal", max_length=15, blank=True)
	kapo1= models.CharField("kapo1", max_length=150, blank=True)
	kapo2=models.CharField("kapo2", max_length=150, blank=True)
	email1= models.EmailField("email1", blank=True)
	email2=models.EmailField("email2", blank=True)
	def __str__(self):
		return "%s [%s-%s]-->    %s i %s" % (self.date, self.start_h, self.finish_h, self.kapo1, self.kapo2)



	
