from django.contrib.auth.forms import UserCreationForm

from .models import CustomUserModel



class RegistrationForm(UserCreationForm):
	class Meta :
		model = CustomUserModel

		fields = '__all__'