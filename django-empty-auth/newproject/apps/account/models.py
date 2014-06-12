from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser
from django.db import models

class CustomUserManager(BaseUserManager):
  def create_user(self, email, password):
    user = CustomUser(username=email, email=email)
    user.set_password(password)
    user.is_active = True
    user.save()

    return user

class CustomUser(User):
  """
  CustomUser not needed, but created with vision of expanding model
  in the future
  """
  objects = CustomUserManager()

  def __str__(self):
    return 'pk=%s username=%s, email=%s' % (self.pk, self.username, self.email)
