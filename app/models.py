from django.db import models
from django.contrib.auth.models import (
	AbstractBaseUser,
	PermissionsMixin,
	BaseUserManager,
)

class UserModelManager(BaseUserManager):

	def create_user(self,email,password,**other_field):
		user = self.model(
			email = self.normalize_email(email),
			**other_field
			)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self,email,password,**other_fields):
		new = self.create_user(email=self.normalize_email(email),password=password,**other_fields)
		new.is_active = True
		new.is_staff = True
		new.is_superuser = True
		new.is_active = True
		new.save(using=self._db)
		return new
		
class CustomUserModel(AbstractBaseUser):
	email = models.EmailField(verbose_name="email",max_length = 100 , unique = True )
	username = models.CharField(max_length = 50 )
	mobile_num = models.IntegerField()
	address = models.TextField(max_length=300)
	is_staff = models.BooleanField(default = False)
	is_active = models.BooleanField(default = True)
	is_superuser = models.BooleanField(default = False)
	is_admin = models.BooleanField(default = False)
	date_joined = models.DateTimeField(verbose_name = "date joined", auto_now_add = True )
	last_login = models.DateTimeField(verbose_name = "last login",auto_now_add=True)

	USERNAME_FIELD = "email"

	REQUIRED_FIELDS = ['username','mobile_num','address']

	objects = UserModelManager()

	def __str__(self):
		return self.username

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True
	