from django.db import models


class Students(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    date_of_birth = models.DateField()
    age = models.IntegerField()

    class Meta:
        db_table = "Wanafunzi"


class Teachers(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)


class Parents(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

    def __str__(self):
        return self.FirstName


class Post(models.Model):
    Title = models.CharField(max_length=20)
    Description = models.TextField(max_length=250)
    Author = models.CharField(max_length=20)
    Created = models.DateTimeField(auto_now_add=True)

