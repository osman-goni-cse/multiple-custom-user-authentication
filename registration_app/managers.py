from django.contrib.auth.models import BaseUserManager


class ApplicantRegisterManager(BaseUserManager):

    """ User Model Manager """
    def create_user(self, email, password=None, is_staff=False, is_superuser=False, is_active=False):

        if not email:
            raise ValueError('Users must have email Address')
        if not password:
            raise ValueError('User must have Password')
        
        
        user_obj = self.model(
            email=self.normalize_email(email),
        )
        user_obj.set_password(password)
        user_obj.is_staff = is_staff
        user_obj.is_superuser = is_superuser
        user_obj.is_active = is_active
        user_obj.save(using=self._db)

    
    def create_superuser(self, email , password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_superuser=True,
            is_active=True
        )
        return user