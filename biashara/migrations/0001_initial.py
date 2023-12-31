# Generated by Django 3.2.23 on 2023-11-02 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=300)),
                ('lastName', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=36)),
            ],
        ),
    ]
