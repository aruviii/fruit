from django.db import models

from allauth.account.forms import SignupForm

from django import forms

from django.contrib.auth.models import AbstractUser

from .models import *

class Products(models.Model):
    CHOICES = (
        ("fruits","fruits"),
        ("vegetables","vegetables"),
        ("groceries","groceries")
        )
    product_name = models.CharField(max_length=200)
    price = models.FloatField()
    category = models.CharField(choices=CHOICES,max_length=200)
    pic = models.CharField(max_length=200)

    def __str__(self):
        return self.product_name

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=100,blank=False,null=False)
    address = models.TextField(max_length=300,blank=False,null=False)
    balance = models.FloatField(null=True,blank=True)
    coupon = models.FloatField(null=True,blank=True)

class CustomSignupForm(SignupForm):
    phone = forms.CharField()
    address = forms.CharField(widget=forms.Textarea)
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.phone = self.cleaned_data['phone']
        user.address = self.cleaned_data['address']
        user.save()
        return user
