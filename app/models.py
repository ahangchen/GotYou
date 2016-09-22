from django.db import models


# Create your models here.

class OSPaperInfo(models.Model):
    src = models.IntegerField(default=0)
    stu_name = models.CharField(max_length=20)
    paper_name = models.CharField(max_length=200)


class DBTalkInfo(models.Model):
    stu_names = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)