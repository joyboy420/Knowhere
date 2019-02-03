from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    image = models.ImageField(upload_to='category_gallery')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "categories"

class Company(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    owner = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "company_owner")
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='company_gallery')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Companies"

    def get_absolute_url(self):
        return reverse('category_list')
		#if want to redirect to its detail page then
        # return reverse('company_detail' ,kwargs = {'pk' : self.pk})

class Comment(models.Model):
    text = models.TextField(max_length = 4000)
    company = models.ForeignKey(Company, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text