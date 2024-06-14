# Generated by Django 5.0.6 on 2024-06-14 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='josaa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute', models.CharField(max_length=255)),
                ('branch', models.CharField(max_length=255)),
                ('quota', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('opening_rank', models.IntegerField()),
                ('closing_rank', models.IntegerField()),
                ('preparatory', models.BooleanField()),
            ],
        ),
    ]