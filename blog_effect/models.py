from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=25)

    def __str__(self):
        return self.category_name

# class Blog(models.Model):
#     title = models.CharField(max_length=50)
#     abstract = models.CharField(max_length=150,blank=True)
#     description = models.CharField(max_length=10000,blank=True)
#     images1 = models.ImageField(null=True,blank=True)
#     images2 = models.ImageField(null=True,blank=True)
#     images3 = models.ImageField(null=True,blank=True)
#     imp_Links = models.CharField(max_length=250,blank=True)
#     references = models.CharField(max_length=400,blank=True)
#     category = models.ForeignKey(Category,on_delete=models.CASCADE)

class Blog(models.Model):
    title = models.CharField(max_length=50)
    abstract = models.CharField(max_length=150, blank=True)
    description = RichTextField(blank=True)
    images1 = models.ImageField(null=True, blank=True)
    images2 = models.ImageField(null=True, blank=True)
    images3 = models.ImageField(null=True, blank=True)
    imp_Links = models.CharField(max_length=250, blank=True)
    references = models.CharField(max_length=400, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)



    def __str__(self):
        return self.title
