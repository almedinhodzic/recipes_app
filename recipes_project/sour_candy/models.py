from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        db_table = 'Categories'

    category_name = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name


class Recipe(models.Model):
    class Meta:
        db_table = 'Recipes'

    title = models.CharField(max_length=255, unique=True, blank=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    recipe_image = models.ImageField(null=True, blank=True, upload_to='images/',                            default='images/default-image-food.jpg')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
