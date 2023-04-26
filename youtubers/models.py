from django.db import models
from datetime import datetime
# Create your models here.
from ckeditor.fields import RichTextField

class Youtuber(models.Model):
    crew_choices =(
        ('solo','solo'),
        ('small','small'),
        ('large','large')
    )    
    camera_choices =(
        ('canon','canon'),
        ('sony','sony'),
        ('nikon','nikon'),
        ('fuji','fuji'),
        ('red','red'),
        ('panasonic','panasonic'),
        ('other','other')
    )
    category_choices =(
        ('coding','coding'),
        ('mobile_review','mobile_review'),
        ('vlogs','vlogs'),
        ('comedy','comedy'),
        ('education','education'),
        ('film_maker','film_maker'),
        ('cooking','cooking')
    )
    name  = models.CharField(max_length=255)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='media/youtubers/%Y/%m/')
    video_url = models.CharField(max_length=255)
    description = RichTextField()
    city  = models.CharField(max_length=255)
    age     = models.IntegerField()
    height  = models.IntegerField()
    crew    = models.CharField(choices=crew_choices,max_length=255)
    camera_type = models.CharField(choices=camera_choices,max_length=255)
    subs_count   = models.CharField(max_length=255)
    category     = models.CharField(choices=category_choices,max_length=255)
    is_featured  = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now,blank=True)