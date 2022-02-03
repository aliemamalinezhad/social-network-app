from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, phone, first_name, last_name, password=None):
        if not email:
            raise ValueError('User name must have an email')
        if not username:
            raise ValueError('User name must have an username')
        if not phone:
            raise ValueError('User name must have an phone')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          phone=phone, first_name=first_name,
                          last_name=last_name)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, username, phone, first_name, last_name, password):

        su_user = self.create_user(email=email, username=username,
                                   phone=phone, first_name=first_name,
                                   last_name=last_name, password=password)
        su_user.is_staff = True
        su_user.is_superuser = True
        su_user.is_active = True

        if su_user.is_staff is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if su_user.is_superuser is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        if su_user.is_active is not True:
            raise ValueError(_('Superuser must have is_active=True.'))

        su_user.save()
        return su_user

