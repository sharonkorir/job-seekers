# Generated by Django 4.0.4 on 2022-04-22 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seekers', '0004_remove_comment_resume_comment_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=150, null=True),
        ),
    ]