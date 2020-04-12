# Generated by Django 3.0.5 on 2020-04-08 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('amazon_url', models.URLField()),
                ('author', models.CharField(max_length=40)),
                ('genre', models.CharField(max_length=40)),
            ],
        ),
    ]
