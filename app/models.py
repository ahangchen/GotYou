from django.db import models


# Create your models here.

class OSPaperInfo(models.Model):
    src = models.IntegerField(default=0)
    stu_name = models.CharField(max_length=20)
    paper_name = models.CharField(max_length=200)