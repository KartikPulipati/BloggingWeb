from django.db import models
from django.contrib.auth.models import User
class blog(models.Model):
    title = models.CharField(max_length=100)
    blog = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
