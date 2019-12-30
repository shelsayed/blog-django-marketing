from django.db import models

# Create your models here.
class Post(models.Model):
    catname = models.CharField(max_length= 200)
    catcontact = models.TextField()

    def __str__ (self):
        return  self.catname


# python manage.py makemigrations
# python manage.py sqlmigrate cat 0001
# python manage.py migrate


