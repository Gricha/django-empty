from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

from registration.forms import RegistrationFormUniqueEmail

from newproject.apps.account import models

import re

class CustomAuthenticationForm(AuthenticationForm):
  username = forms.CharField(
      max_length=255,
      label=u'E-mail')

class RegistrationFormUniqueEmailAndUsername(RegistrationFormUniqueEmail):
  username = forms.CharField(required=False, widget=forms.HiddenInput())

