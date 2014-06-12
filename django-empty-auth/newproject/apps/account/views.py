from django.contrib import messages
from django.conf import settings
from django.contrib.auth import authenticate

from registration import signals
from registration.views import RegistrationView as BaseRegistrationView

from models import CustomUser
from forms import RegistrationFormUniqueEmailAndUsername
from newproject import settings

class CustomRegistrationView(BaseRegistrationView):
  """
  A registration backend which implements the simplest possible
  workflow: a user supplies an email, email address and password
  (the bare minimum for a useful account), and is immediately signed
  up and logged in).
  """
  form_class = RegistrationFormUniqueEmailAndUsername

  def register(self, request, **cleaned_data):
    email, password = cleaned_data['email'], cleaned_data['password1']
    CustomUser.objects.create_user(email, password)

    new_user = authenticate(username=email, password=password)
    signals.user_registered.send(sender=self.__class__,
                                 user=new_user,
                                 request=request)
    return new_user

  def registration_allowed(self, request):
    """
    Indicate whether account registration is currently permitted,
    based on the value of the setting ``REGISTRATION_OPEN``. This
    is determined as follows:

    * If ``REGISTRATION_OPEN`` is not specified in settings, or is
    set to ``True``, registration is permitted.

    * If ``REGISTRATION_OPEN`` is both specified and set to
    ``False``, registration is not permitted.
    """
    return getattr(settings, 'REGISTRATION_OPEN', True)

  def get_context_data(self, *args, **kwargs):
    context = super(CustomRegistrationView, self).get_context_data(*args, **kwargs)
    if 'next' in self.request.GET:
      context['next'] = self.request.GET['next']
    return context

  def get_success_url(self, *args, **kwargs):
    return 'registration_complete'
