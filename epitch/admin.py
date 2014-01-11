from django.contrib import admin
from epitch.models import Registration

class RegistrationAdmin(admin.ModelAdmin):
	list_display = ('team_name', 'email_id', 'contact_number', 'university' , 'participant1' , 'participant2', 'participant3', 'participant4')
	list_filter = ['team_name', 'email_id', 'contact_number', 'university' , 'participant1' , 'participant2', 'participant3', 'participant4']
	search_fields = ['team_name', 'email_id', 'contact_number', 'university' , 'participant1' , 'participant2', 'participant3', 'participant4']
admin.site.register(Registration, RegistrationAdmin)
