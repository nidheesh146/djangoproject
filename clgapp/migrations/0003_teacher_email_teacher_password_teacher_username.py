# Generated by Django 5.1.2 on 2024-10-24 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clgapp', '0002_teacher_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='password',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='username',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
