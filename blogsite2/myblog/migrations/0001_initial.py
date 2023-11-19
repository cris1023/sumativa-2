# Generated by Django 4.2.4 on 2023-11-16 03:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=200)),
                ('texto', models.TextField()),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
