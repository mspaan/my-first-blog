from django.db import models
from django.utils import timezone

# class = object, models.Model = django model
class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

# def = function, self = this in js
    def publish(self):
        self.published_date = timezone.now()
        self.save()

# display the title of the post to know which post it is
# you can also do 'id' instead of 'title'
    def __str__(self):
        return self.title
