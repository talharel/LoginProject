from django import forms
from django.contrib.auth.models import User
from LoginApp.models import UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput()) # Because we need to edit the password before save in db.

    class Meta:
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):

    class Meta:
        model = UserProfileInfo
        fields = ('portfolioSite','profilePicture')
