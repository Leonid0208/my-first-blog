from django.db import models
from django.utils import timezone
from django.conf import settings
<<<<<<< HEAD
# Create your models here.
=======
>>>>>>> b762339a803963f62f6cc0aefecb1bf0a8ef6c76


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
