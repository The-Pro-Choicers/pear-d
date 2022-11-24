from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import json
import uuid

def generate_user_id():
    return uuid.uuid4().hex

# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError("Email address cannot be empty")
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, name, password, **extra_fields)


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    prefer_price = models.IntegerField(default=1, null=False)
    prefer_philanthropic = models.BooleanField(default=False, null=False)
    prefer_env_conscious = models.BooleanField(default=False, null=False)
    prefer_minority = models.BooleanField(default=False, null=False)
    dark_mode = models.BooleanField(default=False, null = False)
    favorites = models.JSONField(blank=True, null=False, default={})

    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

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

class Restaurant(models.Model):
    # model reference: https://docs.djangoproject.com/en/3.1/ref/models/fields/#model-field-types
    # places API information reference: https://developers.google.com/maps/documentation/places/web-service/details

    # general information
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    photo_ref = models.CharField(max_length=128, unique=True) # corresponds to a restaurant's "photo_reference" which is used to make an API call: https://www.youtube.com/watch?v=pcKgiN5FRj4
    price_level = models.IntegerField(null=False) # integer from 0 to 4; see API specifications
    rating = models.DecimalField(null=False, max_digits=2, decimal_places=1) # float from 1.0 to 5.0; see API specifications
    url = models.CharField(max_length=128, unique=True) # the URL of the website (the google maps URL)
    env_conscious = models.BooleanField(null=False, default=False)
    minority = models.BooleanField(null=False, default=False)
    philanthropic = models.BooleanField(null=False, default=False)
    
    # return function for the whole object itself
    def __str__(self):
        return {
            "name": self.name,
            "address": self.address,
            "photo_ref": self.photo_ref,
            "price_level": self.price_level,
            "rating": self.rating,
            "url": self.url,
            "env_conscious": self.env_conscious,
            "minority": self.minority,
            "philanthropic": self.philanthropic
        }

    # specific functions for returning values for sorting purposes
    def get_env_conscious(self):
        return self.env_conscious
    
    def get_minority(self):
        return self.minority
    
    def get_philanthropic(self):
        return self.philanthropic
    


