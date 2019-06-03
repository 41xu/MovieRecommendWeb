import django,os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MovieRecommend.settings")
django.setup()


import pandas as pd
from recommend.models import Movies,Score



django.setup()

def saveToDatabase():
    data=pd.read_csv('data.csv')
    for i in range(len(data)):
        movie=Movies(
            title=data.loc[i]['title'],
            id=data.loc[i]['id'],
            year=data.loc[i]['year'],
            director=data.loc[i]['director'],
            writer=data.loc[i]['writer'],
            actor=data.loc[i]['actor'],
            type=data.loc[i]['type'],
            country=data.loc[i]['country'],
            language=data.loc[i]['language'],
            length=data.loc[i]['length'],
            score=data.loc[i]['score'],
            # user_id=data.loc[i]['user_id'],
            # user_score=data.loc[i]['user_score']
        )
        movie.save()
    for i in range(len(data)):
        score=Score(
            user_id=data.loc[i]['user_id'],
            user_score=data.loc[i]['user_score'],
            id=data.loc[i]['id']
        )
        score.save()

#
# if __name__=='__main__':
#     id=3711760
#     res=Movies.objects.get(id=id)
#     print(res.id,res.title)