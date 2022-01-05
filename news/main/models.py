from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

class New(models.Model):
    category = models.ForeignKey(Category,on_delete=models.RESTRICT)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    file = models.FileField(verbose_name="Photo/Video",default=None)
    added_at = models.DateTimeField(auto_now_add=True)