from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactForm(forms.Form):
    fullName = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Your full name",
            "id": "form_full_name"}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            "class": "form-control",
            "placeholder": "Email",
            "id": "form_email",
        }))
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Your Content",
            "id": "form_content"}))


def clean_email(self):
    email = self.cleaned_data.get("email")
    if not "gmail.com" in email:
        raise forms.ValidationError("Email has to be gmail.com")
    return email


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "id": "form_username",
        }))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class": "form-control",
            "id": "form_password",
            "input_type": "password"
        }))


class RegisterForm(forms.Form):
    email = forms.CharField(label="Email", widget=forms.EmailInput(
        attrs={
            "class": "form-control",
            "id": "form_email",
        }))

    username = forms.CharField(label="Username", widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "id": "form_username",
        }))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={
            "class": "form-control",
            "id": "form_password",
        }))
    confirm_password = forms.CharField(
        label='Confirm Password',  widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "form_confpassword",
            }))

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if confirm_password != password:
            raise forms.ValidationError("Passwords must match.")
        return data

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is already taken.")
        return username
