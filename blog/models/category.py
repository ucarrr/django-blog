from django.db import models
from autoslug import AutoSlugField

class CategoryModel(models.Model):
    name = models.CharField(max_length=255, blank=False,null=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    slug= AutoSlugField(populate_from='name', unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table='Category'
        #verbose_name_plural = 'Categories'