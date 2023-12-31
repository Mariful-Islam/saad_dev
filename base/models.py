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

    def get_stack_list(self):
        stacks = self.stack.split(',')
        return stacks


class ProjectStatstics(models.Model):

    ONGOING_STATUS = 1
    COMPLETED_STATUS = 2
    STATUS_CHOICES = (
        (ONGOING_STATUS, 'Ongoing'),
        (COMPLETED_STATUS, 'Completed')
    )

    name = models.CharField(max_length=50)
    brief = models.CharField(max_length=100)
    status = models.IntegerField(
        choices=STATUS_CHOICES, default=ONGOING_STATUS)
    github = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_status(self):
        if self.status == 1:
            return 'Ongoing'
        elif self.status == 2:
            return 'Completed'


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


class Contact(models.Model):
    INBOX_STATUS = 1
    DRAFT_STATUS = 2
    SENT_STATUS = 3
    SPAM_STATUS = 4

    STATUS_CHOICES = (
        (INBOX_STATUS, 'Inbox'),
        (DRAFT_STATUS, 'Draft'),
        (SENT_STATUS, 'Sent'),
        (SPAM_STATUS, 'Spam')
    )

    username = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    category = models.IntegerField(
        choices=STATUS_CHOICES, default=INBOX_STATUS)

    def __str__(self):
        return self.username

    def get_category(self):
        if self.category == 1:
            return 'Inbox'
        elif self.category == 2:
            return 'Draft'
        elif self.category == 3:
            return 'Sent'
        elif self.category == 4:
            return 'Spam'

    class Meta:
        ordering = ['-time']
