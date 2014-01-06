from django.forms import ModelForm, EmailField, RegexField
from epitch.models import Registration

class RegistrationForm(ModelForm):
	contact_number = RegexField(r'^\d+$')
	email_id = EmailField()

	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)
		for myField in self.fields:
			self.fields[myField].widget.attrs['class'] = 'form-control'
	class Meta:
		model = Registration
		fields = '__all__'

