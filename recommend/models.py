from django.db import models

class Movies(models.Model):
    title=models.CharField(max_length=2000,default='Title')
    movie_id=models.IntegerField(primary_key=True)
    year=models.IntegerField()
    director=models.CharField(max_length=2000,default='Director')
    writer=models.CharField(max_length=2000,default='Writer')
    actor=models.CharField(max_length=2000,default='Actor')
    movie_type=models.CharField(max_length=2000,default='Type')
    country=models.CharField(max_length=2000,default='Country')
    language=models.CharField(max_length=2000,default='Language')
    length=models.IntegerField()
    score=models.FloatField()
    user_id=models.CharField(max_length=2000,default='User_ID')
    user_score=models.IntegerField()

    def __str__(self):
        return self.title