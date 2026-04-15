from django.db import models

# class Trainer(models.Model):
#     name = models.CharField(max_length=100)
#     specialization = models.CharField(max_length=100)
#     experience = models.IntegerField()
#     image = models.ImageField(upload_to='trainers/')

#     def __str__(self):
#         return self.name

# core/models.py
# from django.db import models

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='trainers/')  # folder inside MEDIA_ROOT

    def __str__(self):
        return self.name


# Create your models here.
