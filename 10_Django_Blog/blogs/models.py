from django.db import models
from datetime import date

class Blogs(models.Model):
    blog_id = models.AutoField
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=20, default="")
    desc = models.CharField(max_length=3000, default="")
    created_date = models.DateTimeField(default=date.today)

    def __str__ (self):
        return self.title 