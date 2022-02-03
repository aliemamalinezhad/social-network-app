from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, phone, password, first_name, last_name, **extra_fields):
        if not email:
            raise ValueError('User name must have an email')
        if not username:
            raise ValueError('User name must have an username')
        if not phone:
            raise ValueError('User name must have an phone')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          phone=phone, first_name=first_name,
                          last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, username, phone, password, first_name, last_name, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, username, phone, password, first_name, last_name, **extra_fields)
