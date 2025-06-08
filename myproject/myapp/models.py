from django.db import models

# Create your models here.

class Product(models.Model):
    p_photo = models.ImageField(upload_to='product')
    p_name = models.CharField()
    p_color = models.CharField()
    p_size = models.CharField()
    p_prize = models.PositiveIntegerField()
    p_qty = models.PositiveIntegerField()
    p_description = models.TextField()
    p_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.p_name
