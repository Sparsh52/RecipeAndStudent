# Generated by Django 4.2.5 on 2023-09-16 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0002_recepie_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='recepie',
            name='recipe_view_count',
            field=models.IntegerField(default=1),
        ),
    ]
