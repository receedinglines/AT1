# Generated by Django 5.0.2 on 2024-04-04 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]
