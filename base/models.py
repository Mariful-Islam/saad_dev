from django.db import models

# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200)
    github = models.CharField(max_length=250)
    file = models.FileField()
    image = models.ImageField()
    stack = models.CharField(max_length=500)
    requirement = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    review = models.TextField()

    def __str__(self):
        return self.name


class Partnership(models.Model):
    company_name = models.CharField(max_length=40)
    image = models.ImageField()

    def __str__(self):
        return self.company_name


class Myprofile(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    job = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    github = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Experience(models.Model):
    year = models.CharField(max_length=20)
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=50)
    job_role = models.TextField()

    def __str__(self):
        return self.company_name
