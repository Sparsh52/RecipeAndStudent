# Generated by Django 4.2.5 on 2023-09-15 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recepie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recepie_name', models.CharField(max_length=100)),
                ('recepie_description', models.TextField()),
                ('recepie_image', models.ImageField(upload_to='recepie')),
            ],
        ),
    ]
