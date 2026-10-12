from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CleanUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

    def clean_username(self):
        username = self.cleaned_data["username"].strip()

        if not username:
            raise forms.ValidationError("Username  cannot be empty.")

        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError("A user with username already exists.")

        return username
