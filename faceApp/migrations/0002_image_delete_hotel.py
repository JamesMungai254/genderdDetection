# Generated by Django 5.0.7 on 2024-07-16 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faceApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50)),
                ('img', models.ImageField(default=None, upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Hotel',
        ),
    ]
