from django.db import models

class Movies(models.Model):
    title=models.CharField(max_length=2000,default='Title')
    id=models.IntegerField(primary_key=True,default=0)
    year=models.IntegerField(default=0000)
    director=models.CharField(max_length=2000,default='Director')
    writer=models.CharField(max_length=2000,default='Writer')
    actor=models.CharField(max_length=2000,default='Actor')
    type=models.CharField(max_length=2000,default='Type')
    country=models.CharField(max_length=2000,default='Country')
    language=models.CharField(max_length=2000,default='Language')
    length=models.IntegerField(default=0)
    score=models.FloatField(default=0.0)
    # user_id=models.CharField(primary_key=True,max_length=2000,default='User_ID')
    # user_score=models.IntegerField()

    def __str__(self):
        return self.title

class Score(models.Model):
    user_id=models.CharField(primary_key=True,max_length=2000,default="User_ID")
    user_score=models.IntegerField(default=0.0)
    id=models.IntegerField(default=0)
