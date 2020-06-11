# Generated by Django 3.0.7 on 2020-06-11 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameGrade', models.CharField(max_length=50)),
                ('timeTable', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('dateCreate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
