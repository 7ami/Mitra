from django.db import models

# Create your models here.


class Accommo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=600)
    date = models.DateField()
    img = models.ImageField(upload_to="companies/images", default="")

    def __str__(self):
        return self.name


class Token(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=600)
    date = models.DateField()
    img = models.ImageField(upload_to="companies/images", default="")

    def __str__(self):
        return self.name


class Tour(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    #price = models.IntegerField(default=0)
    desc = models.CharField(max_length=600)
    #date = models.DateField()
    img = models.ImageField(upload_to="companies/images/tour", default="")

    def __str__(self):
        return self.name


class Guide(models.Model):
    id=models.AutoField(primary_key=True)
    image=models.ImageField(upload_to='guidess/',default='')
    name=models.CharField(max_length=20)
    rating=models.CharField(max_length=20)
    lan=models.CharField(max_length=200)
    qualification=models.CharField(max_length=200)
    category=models.CharField(max_length=200,default='Kathmandu')

    def __str__(self):
        return self.name

