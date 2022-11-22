from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import json
import uuid

def generate_user_id():
    return uuid.uuid4().hex

# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("Email address cannot be empty")
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save()

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_dev = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    email = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    prefer_price = models.IntegerField(default=0, null=False)
    prefer_philanthropic = models.BooleanField(default=False, null=False)
    prefer_env_conscious = models.BooleanField(default=False, null=False)
    prefer_minority = models.BooleanField(default=False, null=False)
    dark_mode = models.BooleanField(default=False, null = False)
    favorites = models.JSONField(blank=True, null=False)


    def __str__(self): 
        return json.dumps(
            {
                "email": self.email,
                "prefer_price": self.prefer_price,
                "prefer_philanthropic": self.prefer_philanthropic,
                "prefer_env_conscious": self.prefer_env_conscious,
                "prefer_minority": self.prefer_minority,
                "dark_mode": self.dark_mode,
            }
        )


    def get_email(self):
        return self.email

    