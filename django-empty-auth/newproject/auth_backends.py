from django.contrib.auth.backends import ModelBackend

from newproject.apps.account.models import CustomUser

class CustomUserModelBackend(ModelBackend):
  def authenticate(self, username=None, password=None):
    try:
      user = self.user_class.objects.get(email__iexact=username)
      if user.check_password(password):
        return user
    except self.user_class.DoesNotExist:
      return None

  def get_user(self, user_id):
    try:
      return self.user_class.objects.get(pk=user_id)
    except self.user_class.DoesNotExist:
      return None

  @property
  def user_class(self):
    return CustomUser
