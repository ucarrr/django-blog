from django.db import models
from autoslug import AutoSlugField
from blog.models import CategoryModel
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class TextModel(models.Model):
    title=models.CharField(max_length=50)
    content = RichTextField()
    image = models.ImageField(upload_to='text_image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    slug= AutoSlugField(populate_from='title', unique=True)
    categories=models.ManyToManyField(CategoryModel, related_name="Text")
    author = models.ForeignKey(User, on_delete=models.CASCADE ,related_name="texts")
    
    class Meta:
        db_table='Text'
        
    def __str__(self):
        return self.title        
