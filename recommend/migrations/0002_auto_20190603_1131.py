# Generated by Django 2.2.1 on 2019-06-03 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('user_id', models.CharField(default='User_ID', max_length=2000, primary_key=True, serialize=False)),
                ('user_score', models.IntegerField(default=0.0)),
                ('id', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='movies',
            name='movie_id',
        ),
        migrations.RemoveField(
            model_name='movies',
            name='name',
        ),
        migrations.AddField(
            model_name='movies',
            name='actor',
            field=models.CharField(default='Actor', max_length=2000),
        ),
        migrations.AddField(
            model_name='movies',
            name='country',
            field=models.CharField(default='Country', max_length=2000),
        ),
        migrations.AddField(
            model_name='movies',
            name='director',
            field=models.CharField(default='Director', max_length=2000),
        ),
        migrations.AddField(
            model_name='movies',
            name='language',
            field=models.CharField(default='Language', max_length=2000),
        ),
        migrations.AddField(
            model_name='movies',
            name='length',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movies',
            name='score',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='movies',
            name='title',
            field=models.CharField(default='Title', max_length=2000),
        ),
        migrations.AddField(
            model_name='movies',
            name='type',
            field=models.CharField(default='Type', max_length=2000),
        ),
        migrations.AddField(
            model_name='movies',
            name='writer',
            field=models.CharField(default='Writer', max_length=2000),
        ),
        migrations.AddField(
            model_name='movies',
            name='year',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='movies',
            name='id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
