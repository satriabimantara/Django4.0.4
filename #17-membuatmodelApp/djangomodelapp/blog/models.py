from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    # Mengganti Post object pada django admin dengan title post yang diinputkan user
    def __str__(self):
        return "{}".format(self.title)
