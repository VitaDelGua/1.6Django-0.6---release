# Generated by Django 5.1.4 on 2024-12-25 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalculateHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.IntegerField()),
                ('b', models.IntegerField()),
                ('result', models.IntegerField()),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]
