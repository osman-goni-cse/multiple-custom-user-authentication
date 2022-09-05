from django import forms
from django.contrib.auth.models import User
from registration_app.models import AddCircular, ApplicantRegister, Account, AddCircular
from django.core.exceptions import ValidationError

class AccountForm(forms.ModelForm):
  # password = forms.CharField(widget=forms.PasswordInput())
  class Meta():
    model = Account
    fields = ('email', 'password')

  # def clean_email(self):
  #   email = self.cleaned_data["email"]
  #   if User.objects.filter(email=email).exists():
  #       raise ValidationError("An user with this email already exists!")
  #   return email 


class ApplicantRegisterForm(forms.ModelForm):
  # profile_pic = forms.ImageField()

  # def clean_profile_pic(self):
  #   pic_size = self.cleaned_data["profile_pic"]
  #   pic_size = pic_size.size
  #   print('pic', pic_size)
  #   if pic_size > 204800:
  #     raise forms.ValidationError("The maximum file size that can be uploaded is 200KB")
  #   else:
  #     return pic_size
  class Meta():
    model = ApplicantRegister
    # fields = '__all__'
    exclude = ['user', 'is_active']


class AddCircularForm(forms.ModelForm):
  class Meta():
    model = AddCircular
    exclude = ['user', ]    
    
    
    