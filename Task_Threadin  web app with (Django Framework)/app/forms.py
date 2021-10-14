from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):

    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Username'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class BootstrapAuthenticationForm(AuthenticationForm):

    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class':'form-control',
                                   'placeholder': 'Username'}))

    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

    confirmpassword = forms.CharField(label=("Confirm Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Confirm Password'}))


    firstname = forms.CharField(label=("First Name"),
                                widget=forms.TextInput({
                                    'class': 'form-control',
                                    'placeholder': 'First Name'}))


    surname = forms.CharField(label=("Surname"),
                                widget=forms.TextInput({
                                    'class': 'form-control',
                                    'placeholder': 'Surname'}))


    mobile = forms.IntegerField(label=("Mobile Number"),
                                widget=forms.TextInput({
                                    'class': 'form-control',
                                    'placeholder': 'Mobile Number'}))

    IDnumber = forms.CharField(label=("ID Number"),
                                widget=forms.TextInput({
                                    'class': 'form-control',
                                    'placeholder': 'SA valid ID Number'}))

    email = forms.EmailField(label=("E-mail Address"))

    address = forms.CharField(label=("Address"),
                                widget=forms.TextInput({
                                    'class': 'form-control',
                                    'placeholder': 'address'}))

    copyid = forms.ImageField()
    
    proofofaddress = forms.ImageField()


