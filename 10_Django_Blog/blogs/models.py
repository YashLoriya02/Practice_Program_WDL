from django.db import models

class Blogs(models.Model):
    blog_id = models.AutoField
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=20, default="")
    desc = models.CharField(max_length=3000, default="")

    def __str__ (self):
        return self.title 