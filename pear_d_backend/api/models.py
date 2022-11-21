from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
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
    
    def get_price_level(self):
        return self.price_level
    
    def get_rating(self):
        return self.rating