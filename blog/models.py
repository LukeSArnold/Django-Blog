from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    content = models.TextField()
    posted = models.DateTimeField("date published")

    def __str__(self):
        return self.title
 
class Comments(models.Model):
    blog = models.ForeignKey('blog', on_delete = models.CASCADE)
    commenter = models.CharField(max_length = 200)
    email = models.EmailField(max_length=254)
    content = models.TextField()
    posted = models.DateTimeField("date published")

    def __str__(self):
        return self.commenter


# Create your models here.
