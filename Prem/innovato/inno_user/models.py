from django.db import models

# Create your models here.
class Comment(models.Model):
    cmt_id = models.AutoField(primary_key=True)
    cmt_user  = models.CharField(max_length=30, default='')
    cmt_msg = models.CharField(max_length=30, default='')
    cmt_vid = models.IntegerField(default=0)
    def __str__(self):
        return self.cmt_user

class Video_up(models.Model):
    v_id = models.AutoField(primary_key=True)
    v_title = models.CharField(max_length=30, default='')
    v_file = models.FileField(upload_to='inno_user/videos/') #media/video
    v_desc = models.CharField(max_length=120, default='')
    v_user = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.v_title

class like(models.Model):
    l_id = models.AutoField(primary_key=True)
    l_postid =models.IntegerField(default=0)
    l_user = models.CharField(max_length=20,default='')

    def __str__(self):
        return self.l_user

    