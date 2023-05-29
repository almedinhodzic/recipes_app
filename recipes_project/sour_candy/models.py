from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    class Meta:
        db_table = 'Recipes'

    title = models.CharField(max_length=255, unique=True, blank=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=255, blank=False, null=False)
    recipe_image = models.ImageField(null=True, blank=True, upload_to='images/profile/',
                                     default='images/profile/default.jpg')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='images/',
                                      default='images/default-image-food.jpg')

    def __str__(self):
        return str(self.user)
