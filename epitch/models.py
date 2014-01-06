from django.db import models

class Registration(models.Model):
	team_name = models.CharField(max_length=200, blank=False, unique=True)
	email_id = models.CharField(max_length=200, blank=False, unique=True)
	participant1 = models.CharField(max_length=200, blank=False)
	participant2 = models.CharField(max_length=200, blank=False)
	participant3 = models.CharField(max_length=200, blank=True)
	participant4 = models.CharField(max_length=200, blank=True)
	contact_number = models.CharField(max_length=12, blank=False)
	university = models.CharField(max_length=200, blank=False)

